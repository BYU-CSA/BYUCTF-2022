# Wordle Writeup
This is wordle but with a twist. Instead of returning which character is correct or not, it returns a hash of the 5 emojis `['⬛', '🟨', '🟩']` that are used to show if the letters are correct or not. If you simply brute force all combinations of emojis, you can which of your letters are correct. Once you solve the wordle, you'll get the flag.

Proof of Concept:
```python
import hashlib

my_hash = input("Hash:")

allChars = ['⬛', '🟨', '🟩']

allHashes = {}
for char1 in allChars:
    for char2 in allChars:
        for char3 in allChars:
            for char4 in allChars:
                for char5 in allChars:
                    strToHash = char1 + char2 + char3 + char4 + char5
                    hash = hashlib.md5(strToHash.encode('utf-8')).hexdigest()
                    allHashes[hash] = strToHash

print(allHashes[my_hash])
```

**Flag** - `byuctf{b@c0n_grease}`

## Hosting
To run the web server, use the following command:

```bash
sudo pip3 install -r src/requirements.txt && python3 src/app.py
```