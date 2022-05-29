# Fun Fact Writeup

**Flag** - `byuctf{0rc4s-4r3-c00l}`


## Playtest Notes

#### Daniel Taylor
Script for solving it once you have decoded the B64 and obtained the encrypted flag:

```python
import string
string.printable

alpha = '0123456789abcdefghijklmnopqrstuvwxyz-'
enc = 'gfedcba`on6543210?>=<;:98\'&%$#"! /.-z'

key = dict()
for i in range(len(alpha)):
	key[enc[i]] = alpha[i]

flag_enc = 'g%4c$zc%dz4gg;'
for c in flag_enc:
	print(key[c], end='')
print()
```

`enc` can be obtained by submitting `alpha` as a flag and looking at the encrypted value.  I originally had some extra characters and was missing `-`, but was able to figure out what was missing through trial and error (e.g. a `KeyError: 'z'` message showed me that I was missing the character that decoded to `-` originally.

If we wanted to make the challenge a little more difficult, we could remove the line that prints out the encrypted input so that people would need to modify the code a little to make it do that.
