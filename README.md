# MudYom (มัดย้อม)

MudYom is a module for pre/post-processing text. It combines, aka มัด, words that should be together into one token. This process is done according to a user-defined dictionary.

****

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

## Acknowledgements
- The implementation of this module is majorily drawn from [Wongnai's post][post], written by [Ekkalak Thongthanomkul][noom].

[post]: https://life.wongnai.com/wongnai-search-improvement-using-machine-learning-part1-e0777b65979e
[noom]: https://github.com/Ekkalak-T