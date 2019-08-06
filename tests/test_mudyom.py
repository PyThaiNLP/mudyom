import pytest
import numpy as np

import mudyom as my

@pytest.mark.parametrize("txt,tokenized,expected", [
    (["thisisacat", "this|is|a|cat", "1000101100"]),
])
def test_binary_representation(txt, tokenized, expected):
    actual = my._binary_representation(txt, tokenized.split("|"))

    assert actual == np.array(list(expected)).astype(int).tolist()

@pytest.mark.parametrize("tokenized_txt,vocabs,expected", [
    (["this|is|kit|kat", ["kitkat"], "this|is|kitkat"]),
    (["kit|kat|is|always|kitkat", ["kitkat"], "kitkat|is|always|kitkat"]),
])
def test_gazetteer(tokenized_txt, vocabs, expected):
    my_obj = my.MudYom(vocabs)

    actual = my_obj.yom(tokenized_txt)
    assert actual == expected

@pytest.mark.parametrize("txt,vocabs,expected", [
    (["thisiskitkat", ["kitkat"], [(6, 12)]]),
    (["kitkatisalwayskitkat", ["kitkat"], [(0, 6), (14, 20)]]),
])
def test_find_matches(txt, vocabs, expected):
    trie = my._build_trie_from_vocabs(vocabs)
    rx = my._build_regex_from_trie(trie)

    actual = my._find_matches(txt, rx)
    assert actual == expected