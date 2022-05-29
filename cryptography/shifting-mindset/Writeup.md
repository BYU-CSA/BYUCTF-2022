# Shifting Mindset Writeup
So the keyword here is "shifting". If the player emphasizes that word, they can think about how the word "shifting" literally means that the person was holding down shift while typing out this cipher. If a standard American keyboard is used, and the same keystrokes were hit without holding down the shift button, it would lead to the following numbers:

`9 20 8 9 14 11 13 25 19 8 9 6 20 11 5 25 9 19 19 20 21 3 11`

This is then just a standard A1Z26 cipher where each number n represents the letter in the nth position of the english alphabet. This leads to the message

`ithinkmyshiftkeyisstuck`

Wrap that in the `byuctf{}` flag format and they're done!

Accepted flags:

`byuctf{ithinkmyshiftkeyisstuck}`
`byuctf{i_think_my_shift_key_is_stuck}`
