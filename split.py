#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import print_function

import os
import re
import sys
import json
import random
import logging
import argparse
import unicodedata as ucd


def load_data(filename, valid_rate=10, test_rate=10):
    if not filename:
        logging.error("invalid file name")
        return
    tokens = []
    sentences = []
    with open(filename) as ifp:
        for line in ifp:
            line = line.strip()
            if line.startswith("#"):
                continue
            if line:
                fields = line.split("\t")
                fields[2] = fields[2].replace("++", "+PLS").replace("+", " ").replace("PLS", "+")
                tokens.append("\t".join(fields))
            else:
                if 1 < len(tokens) <= 50:
                    sentences.append(tokens)
                tokens = []

    total_count = len(sentences)

    random.shuffle(sentences)

    # test_count = int(len(sentences)*(test_rate%100)/100) if test_rate else 0
    # valid_count = int(len(sentences)*(valid_rate%100)/100) if valid_rate else 0
    test_count = 1000
    valid_count = 1000
    train_count = len(sentences) - valid_count - test_count
    valid_data = sentences[-valid_count:]
    sentences = sentences[0:-valid_count]
    test_data = sentences[-test_count:]
    sentences = sentences[0:-test_count]
    train_data = sentences[0:train_count]

    logging.info("splitting %d sentences into %d train / %d validate / %d test",
                 total_count, len(train_data), len(valid_data), len(test_data))

    return train_data, valid_data, test_data


def save_data(filename, data):
    if not data:
        return
    with open(filename, "w") as ofp:
        for sent in data:
            print("\n".join(sent), file=ofp)
            print("", file=ofp)


train, valid, test = load_data(sys.argv[1])
prefix = sys.argv[2] if len(sys.argv) > 2 else sys.argv[1].split(".")[-2]

os.makedirs("temp", exist_ok=True)
save_data(f"temp/{prefix}.train.txt", train)
save_data(f"temp/{prefix}.valid.txt", valid)
save_data(f"temp/{prefix}.test.txt", test)
