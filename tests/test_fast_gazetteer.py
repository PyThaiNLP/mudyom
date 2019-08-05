import pytest
import numpy as np

import fast_gazetteer as fg

@pytest.mark.parametrize("txt,tokenized,expected", [
    (["thisisacat", "this|is|a|cat", "1000101100"]),
])
def test_binary_representation(txt, tokenized, expected):
    actual = fg._binary_representation(txt, tokenized.split("|"))

    assert actual == np.array(list(expected)).astype(int).tolist()

@pytest.mark.parametrize("tokenized_txt,dictionary,expected", [
    (["this|is|kit|kat", ["kitkat"], "this|is|kitkat"]),
    (["kit|kat|is|always|kitkat", ["kitkat"], "kitkat|is|always|kitkat"]),
])
def test_gazetteer(tokenized_txt, dictionary, expected):
    actual = fg.gazetteer(tokenized_txt, dictionary)
    assert actual == expected

@pytest.mark.parametrize("txt,vocab,expected", [
    (["thisiskitkat", "kitkat", [(6, 12)]]),
    (["kitkatisalwayskitkat", "kitkat", [(0, 6), (14, 20)]]),
])
def test_find_matches(txt, vocab, expected):
    actual = fg._find_matches(txt, vocab)
    assert actual == expected