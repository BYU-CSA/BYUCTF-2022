# The Most Worthy Distinction of Pain
This challenge takes in text (ie `thisistext`), combines each two letters pairwise (`th is is te xt`), gets their combined encoding (`0x7468 0x2069 0x7320 0x6973 0x2074 0x6520 0x7874`), and gets that nth word from the dictionary. As it turns out, that's mostly the `d`s of this particular dictionary.

It can be solved by taking each word, finding its position in the dictionary, taking the `0xff00` mask for the first letter the word represents, and the mask `0x00ff` for the second letter.

**Flag** - `byuctf{what_an_inefficient_code_ug2Ko8Cz}`