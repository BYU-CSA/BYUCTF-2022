# Blue 3 Writeup
This challenge was created by taking a flag, splitting it into individual characters, and adding 1 to a random color channel in a pixel in a section. The sectioning would be as follows, if the flag were `ctf{123}`:

```
blue.png
┌─┬──────────────┐
│c│              │
├─┼─┐            │
│ │t│            │
│ └─┼─┐          │
│   │f│          │
│   └─┼─┐        │
│     │{│        │
│     └─┼─┐      │
│       │1│      │
│       └─┼─┐    │
│         │2│    │
│         └─┼─┐  │
│           │3│  │
│           └─┼─┐│
│             │}││
│             └─┘│
└────────────────┘
```

The result is some slightly-not-the-same blue along the diagonal. It is created using a base image of solid blue (made on-the-fly) in [`create.py`](./create.py) which grabs text from [`flag.txt`](./flag.txt).

It can be solved by guessing the proper length of the flag, adding up all the differences in each section to make a character from an ASCII code, and seeing if that matches our flag format. (See [`solve.py`](./solve.py).)

Hard mode is giving out `blue.png` alone. Easy mode is giving out `create.py` as well. I think there are some participants who might like another blue challenge, which is why I left it off. (Also, the original was like this.)

**Flag** - `byuctf{more_blue_steganography_da_ba_dee_nkiY9CyP}`