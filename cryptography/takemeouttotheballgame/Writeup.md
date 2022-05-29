# Take Me Out to the Ball Game Writeup
There is a kind of clue in the instructions, it is not obvious though. When a grand slam happens, there are 4 runs completed because the bases are loaded... Bases... When presented with this flag, the competitor needs to be able to determine what type of encoding it is. It is a base29 encoding. After decoding that, the competitor has a bunch of ascii hex values that represent the flag. All they need to do is make the conversion from ascii to text, and they have the flag. My intent is to teach that there are other types of base encodings than the ones we are most familiar with. 

**Both cyberchef and dcode.fr cannot recognize the base29 cipher. I would recommend not giving any clues about it and making it self-loathing :) 

**Flag** - `byuctf{4ll_th3_b4s3s_4r3_10ad3d!}`