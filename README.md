
# S2D : SejongTree To Dependency
세종 구문 분석 말뭉치의 의존 구문 구조로의 변환 도구

# Document : SejongTree2Dep.pdf

# Requirement
- python 3.6
- tqdm
- hgtk

# Execution
> (rigid head): python SejongToDependency.py -root_dir corpus_folder_path -save_file result -pos_list ./Rules/pos_list.txt -head_initial ./Rules/linear_rules.txt -head_initial_symbol ./Rules/symbol_rules.txt

> (non-rigid head): python SejongToDependency.py -root_dir corpus_folder_path -save_file result -pos_list ./Rules/pos_list.txt -head_initial ./Rules/linear_rules.txt -head_initial_symbol ./Rules/symbol_rules.txt


    Paramters
    -root_dir: 세종 코퍼스 폴더 위치
    -file_name(optional): 세종 코퍼스 파일 이름(하나의 세종 코퍼스 파일만 읽고자 할 때)
    -save_file: 의존 구문 구조 저장할 파일 이름
    -pos_list: 품사 정보 파일
    -head_initial: head-initial 예외 규칙(구분자 : \t)
    -head_initial_symbol: head-initial 예외 규칙 중 심볼과 기능어 규칙(구분자 : \t)
    -non_rigid_head(optional): Non-rigid Head Final에만 사용



# Format : CONLL-U
*예제:* 
엠마누엘 웅가로는 "실내 장식품을 디자인할 때 옷을 만들 때와는 다른 해방감을 느낀다"고 말한다.

- **Rigid Head-final Version**

    |  ID  |    FORM    |    LEMMA    |  UPOSTAG  |    XPOSTAG    | FEATS |  HEAD  |    DEPREL    | DEPS |     MISC     |
    |:----:|:----------:|:-----------:|:---------:|:-------------:|:-----:|:------:|:------------:|:----:|:------------:|
    |   1  |  엠마누엘   |   엠마누엘   |  PROPN    |    NNP        |   -   |    2   |    NP        |  -   |      -       |
    |   2  |  웅가로는   |   웅가로 는  |  PROPN    |    NNP JX     |   -   |   16   |    NP_SBJ    |  -   |      -       |
    |   3  |   "        |    "        |  PUNCT    |    SS         |   -   |   14   |    L         |  -   |SpaceAfter=No |
    |   4  |  실내      |   실내       |  NOUN     |    NNG        |   -   |    5   |    NP        |  -   |      -       |
    |   5  |  장식품을   |   장식품을   |  NOUN     |    NNG JKO    |   -   |    6   |    NP_OBJ    |  -   |      -       |
    |   6  |  디자인할   | 디자인 하 ㄹ |  VERB     |    NNG XSV ETM|   -   |    7   |    VP_MOD    |  -   |      -       |
    |   7  |  때        |   때        |  NOUN     |    NNG        |   -   |   13   |    NP_AJT    |  -   |      -       |
    |   8  |  옷을      |    옷 을     |  NOUN     |    NNG JKO    |   -   |    9   |    NP_OBJ    |  -   |      -       |
    |   9  |  만들      |   만들 ㄹ    |  VERB     |    VV ETM     |   -   |   10   |    VP_MOD    |  -   |      -       |
    |  10  |  때와는     |   때 와 는   |  NOUN    |    NNG JKB JX |   -   |   11    |    NP_SBJ   |  -   |      -       |
    |  11  |  다른      |   다르 ㄴ    |  ADJ      |    VA ETM     |   -   |   12   |    VP_MOD    |  -   |      -       |
    |  12  |  해방감을   |   해방감 을  |  NOUN     |    NNG JKO    |   -   |   13   |    NP_OBJ    |  -   |      -       |
    |  13  |  느낀다     |   느끼 ㄴ다  |  VERB     |    VV EC      |   -   |   14   |    VP        |  -   |SpaceAfter=No |
    |  14  |   "        |    "        |  PUNCT    |    SS         |   -   |   15   |    VP        |  -   |SpaceAfter=No |
    |  15  |  고        |   고        |  ADP      |    JKQ        |   -   |   16   |    VP_CMP    |  -   |      -       |
    |  16  |  말한다.    |   말 하 ㄴ다|  VERB     |   NNG XSV EF SF|   -   |    0   |    ROOT        |  -   |      -       |

- **Non-rigid Head final Version**

    |  ID  |    FORM    |    LEMMA    |  UPOSTAG  |    XPOSTAG    | FEATS |  HEAD  |    DEPREL    | DEPS |     MISC     |
    |:----:|:----------:|:-----------:|:---------:|:-------------:|:-----:|:------:|:------------:|:----:|:------------:|
    |   1  |  엠마누엘   |   엠마누엘   |  PROPN    |    NNP        |   -   |    2   |    NP        |  -   |      -       |
    |   2  |  웅가로는   |   웅가로 는  |  PROPN    |    NNP JX     |   -   |   16   |    NP_SBJ    |  -   |      -       |
    |   3  |   "        |    "        |  PUNCT    |    SS         |   -   |   13   |    L         |  -   |SpaceAfter=No |
    |   4  |  실내      |   실내       |  NOUN     |    NNG        |   -   |    5   |    NP        |  -   |      -       |
    |   5  |  장식품을   |   장식품을   |  NOUN     |    NNG JKO    |   -   |    6   |    NP_OBJ    |  -   |      -       |
    |   6  |  디자인할   | 디자인 하 ㄹ |  VERB     |    NNG XSV ETM|   -   |    7   |    VP_MOD    |  -   |      -       |
    |   7  |  때        |   때        |  NOUN     |    NNG        |   -   |   13   |    NP_AJT    |  -   |      -       |
    |   8  |  옷을      |    옷 을     |  NOUN     |    NNG JKO    |   -   |    9   |    NP_OBJ    |  -   |      -       |
    |   9  |  만들      |   만들 ㄹ    |  VERB     |    VV ETM     |   -   |   10   |    VP_MOD    |  -   |      -       |
    |  10  |  때와는     |   때 와 는   |  NOUN    |    NNG JKB JX |   -   |   11    |    NP_SBJ   |  -   |      -       |
    |  11  |  다른      |   다르 ㄴ    |  ADJ      |    VA ETM     |   -   |   12   |    VP_MOD    |  -   |      -       |
    |  12  |  해방감을   |   해방감 을  |  NOUN     |    NNG JKO    |   -   |   13   |    NP_OBJ    |  -   |      -       |
    |  13  |  느낀다     |   느끼 ㄴ다  |  VERB     |    VV EC      |   -   |   16   |    VP_CMP    |  -   |SpaceAfter=No |
    |  14  |   "        |    "        |  PUNCT    |    SS         |   -   |   13   |    R         |  -   |SpaceAfter=No |
    |  15  |  고        |   고        |  ADP      |    JKQ        |   -   |   13   |    X_CMP     |  -   |      -       |
    |  16  |  말한다.    |   말 하 ㄴ다|  VERB     |   NNG XSV EF SF|   -   |    0   |    ROOT        |  -   |      -       |
