# Kendrick Lamar Writeup
If you read each row from left to right in order (either by discerning the letter, or matching the color), you will get the sequence `CATGACGATTCATAGGCTACGTCTTAGTGAAGCTCTCTCAGCATAGATCACAGCCATATCATAATATACACG`. If you put this in the [DNA Writer decoder](https://earthsciweb.org/js/bio/dna-writer/), it will print out `BYUCTF.1TS 1N 0UR BL00D.` Replace `.` for curly braces and spaces for `_` and you'll get the flag.


What made this difficult is that there are a multitude of various tools to encode and decode text with DNA sequence code. This specific one allows you to go from just the color to the plaintext. The hint: 
```
first you have two types of information given, one is to help you confirm what this cipher is using. 
the other is really the only way you can solve the problem given the picture quality.
the tricky part of this problem is finding the specific tool that will work.
in this case its a simple 9 year old tool written by a guy with initials L. U
```

provides a few different pieces of info: First. the  two types of info are the colors and letters. The letters are to confirm the cipher, but you really need to use the colors as you can't see every leter perfectly. If you view the link above, you will see that all the information checks out at the footer of the website for the hints about who made the tool. 

**Flag** - `byuctf{1ts_1n_0ur_Bl00d}`
