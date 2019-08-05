from fire import Fire

import fast_gazetteer as fg

def main(input, dictionary, output):
    print("Input: %s" % input)
    print("Dictionary: %s" % dictionary)

    dictionary = fg._load_dict(dictionary)

    with open(input, "r") as fin:
        for l in fin:
            l = l.strip()
            gazz = fg.gazetteer(l, dictionary)
            print(gazz)

if __name__ == "__main__":
    Fire(main)
