import re

import numpy as np

from mudyom.trie import Trie

DEFAULT_SEPARATOR = "|"

class MudYom:
    def __init__(self, vocabs):
        self.trie = _build_trie_from_vocabs(vocabs)
        self.trie_regex = _build_regex_from_trie(self.trie)
    
    def yom(self, txt):
        new_txt = gazetteer(txt,  self.trie_regex)

        return new_txt

def _build_trie_from_vocabs(vocabs):
    trie = Trie()

    for v in vocabs:
        trie.add(v)

    return trie

def _load_dict(filepath):
    vocabs = []

    with open(filepath, "r") as f:
        for v in f:
            vocabs.append(v.strip())

    return vocabs

def _build_regex_from_trie(trie):
    return re.compile(r'(' + trie.pattern() + ')', re.I)

def _binary_representation(txt, tokens):
    reps = [1] + [0] * (len(txt) - 1)

    ix = 0
    for t in tokens[:-1]:
        ix += len(t)
        reps[ix] = 1

    return reps

def _find_matches(txt, rx):
    matches = []
    for m in re.finditer(rx, txt):
        matches.append((m.start(), m.end()))

    return matches

def _find_starting_word_position(bin_reps):
    positions = []
    for i, l in enumerate(bin_reps):
        if l == 1:
            positions.append(i)

    return positions

def gazetteer(tokenized_txt, rx, sep=DEFAULT_SEPARATOR):
    txt = tokenized_txt.replace(sep, "")
    bin_reps = np.array(_binary_representation(txt, tokenized_txt.split(sep)))

    matches = _find_matches(txt, rx)
    for st_ix, end_ix in matches:
        bin_reps[(st_ix+1):(end_ix)] = 0
        bin_reps[st_ix] = 1

    starting_pos = _find_starting_word_position(bin_reps)

    starting_ix = starting_pos
    ending_ix = starting_pos[1:] + [bin_reps.shape[0]]

    newly_tokenized = []
    for st_ix, end_ix in zip(starting_ix, ending_ix):
        newly_tokenized.append(txt[st_ix:end_ix])

    return sep.join(newly_tokenized)