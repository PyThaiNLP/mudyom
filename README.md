# MudYom (มัดย้อม)

MudYom is a module for pre/post-processing text. It combines, aka มัด, words that should be together into one token. This process is done according to a user-defined dictionary.

****

## Usage (WIP)
```
mudyom-cli --input "..." --dictionary "..." --output "..."
```
**Remark:** Vocabs in the dictionary should be sorted from longest to shortest one.

### Example
```
# input.txt
ฉัน|ขวัญ|หนี|ตี|ฝ่อ|ใจ|สลาย

# dictionary.txt
ตีฝ่อ
หลบลี้
คิดถึง

# output.txt
ฉัน|ขวัญ|หนี|ตีฝ่อ|ใจ|สลาย
```

## Acknowledgements
- The implementation of this module is majorily drawn from [Wongnai's post][post], written by Noom..

[post]: https://life.wongnai.com/wongnai-search-improvement-using-machine-learning-part1-e0777b65979e