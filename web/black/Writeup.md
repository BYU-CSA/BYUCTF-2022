# Black Writeup
This website was designed with Vue, which made the HTML difficult to read and the JavaScript obfuscated. However, if you play around with the page, random photos will pop up if you put your mouse over them. Opening up these photos in a new tab will reveal sections of a QR code. Further inspection of the page will reveal the DIVs that will give the photo URIs if moused over. Once all the sections of the QR code are found, it can be assembled and scanned. This brings you to http://black.byuctf.xyz/index_/, another similar-looking page. If you look in the Network tab, a video was loaded onto the page (2 pixels wide, I believe). If you open the video in another tab, you'll be rickrolled :devil:! 

HOWEVER, upon further inspection, 7 words are placed randomly throughout the video, so you must watch the video all the way through and get the words :devilx2:! These are words to the Canadian national anthem (or something like that), and so you must order the words to match. That is the flag. 

**Flag**: `byuctf{Oh Canada Our Home And Native Land}`

## Hosting
The video `loadButton.mp4` is too big to include in Git, but is located [here](https://app.box.com/s/rbdoh3eyhcli15pkavvtvjzidaol8t4t) and should be downloaded and appear in the `files/` directory. It should also be downloaded, moved to the `files/_nuxt/videos/` and called `loadButton.85316c6.mp4`.