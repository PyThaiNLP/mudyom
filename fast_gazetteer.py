import re

import numpy as np

DEFAULT_SEPARATOR = "|"

def _load_dict(filepath):
    vocabs = []

    with open(filepath, "r") as f:
        for v in f:
            vocabs.append(v.strip())

    # sort longest last
    return vocabs

def _binary_representation(txt, tokens):
    reps = [1] + [0] * (len(txt) - 1)

    ix = 0
    for t in tokens[:-1]:
        ix += len(t)
        reps[ix] = 1

    return reps

def _find_matches(txt, vocab):
    matches = []
    for m in re.finditer(vocab, txt):
        matches.append((m.start(), m.end()))

    return matches

def _find_starting_word_position(bin_reps):
    positions = []
    for i, l in enumerate(bin_reps):
        if l == 1:
            positions.append(i)

    return positions

def gazetteer(tokenized_txt, dictionary, sep=DEFAULT_SEPARATOR):
    txt = tokenized_txt.replace(sep, "")
    bin_reps = np.array(_binary_representation(txt, tokenized_txt.split(sep)))

    for v in dictionary:
        matches = _find_matches(txt, v)
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