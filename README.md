# MudYom (มัดย้อม)

[![](https://travis-ci.org/heytitle/mudyom.svg?branch=master)](https://travis-ci.org/heytitle/mudyom)

MudYom is a module for pre/post-processing text. It combines, aka มัด, words that should be together into one token. This process is done according to a user-defined dictionary.

****
## Installation
Because it's still in `beta`, installation has to be done via
```
$ pip install git@github.com:heytitle/mudyom.git
```

## Usage (WIP)
```
$ mudyom-cli --input "..." --dictionary "..." --output "..."
```
**Remark:** Vocabs in the dictionary should be sorted from longest to shortest one.

If not, you can use the command line below to sort the dictionary:
```
$ cat dictionary.txt | awk '{ print length, $0 }' | sort -g -r | cut -d" " -f2  > sorted_dictionary.txt
```

### Example
```
# input.txt
ฉัน|ขวัญ|หนี|ตี|ฝ่อ|ใจ|สลาย

# dictionary.txt
หลบลี้
คิดถึง
ตีฝ่อ

# output.txt
ฉัน|ขวัญ|หนี|ตีฝ่อ|ใจ|สลาย
```

## Public Dictionaries
| Name | Vocaburary Size | Author |
|---|---|---|
| [Food and Restuarant menues][wongnai]| ~400k |  Wongnai  |
| [Names and Acronyms][commonnames]| ~2k | Thachaparn Bunditlurdruk |
| Name Entity in BEST | .. | .. |

## Acknowledgements
- The implementation of this module is majorily drawn from [Wongnai's post][post], written by [Ekkalak Thongthanomkul][noom].

[post]: https://life.wongnai.com/wongnai-search-improvement-using-machine-learning-part1-e0777b65979e
[noom]: https://github.com/Ekkalak-T
[wongnai]: https://github.com/wongnai/wongnai-corpus/blob/master/search/food_dictionary.txt
[commonnames]: https://gist.github.com/heytitle/a42a1ff819c61052ecd9aa3d1593371a