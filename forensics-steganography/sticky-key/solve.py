alt = 'ÅıÇÎ´Ï˝ÓˆÔÒÂ˜Ø∏Œ‰Íˇ¨◊„˛Á¸å∫ç∂´ƒ©˙ˆ∆˚¬µ˜øπœ®ß†¨√∑≈¥Ω¡™£¢∞§¶•ªº–≠⁄€‹›ﬁﬂ‡°·‚—±”’ ≥≤æ'
char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890-=!@#$%^&*()_+{} .,\''

key = dict()
for i in range(len(alt)):
    key[alt[i]] = char[i]

message = """Subject: ˆ ˇ˙ˆ˜˚ Â¥ ´¥∫øå®∂ ˆß ∫®ø˚´˜
Contents: ˆ †˙ˆ˜˚ µ¥ ˚´¥∫øå®∂ ˆß ∫®ø˚´˜≥ ˆ ∑åß π¬å˜˜ˆ˜© †ø †´¬¬ ¥ø¨ †˙ˆß ∫¨† ˆæµ ˜ø† ß¨®´ ˙ø∑ ¥ø¨ ∑ˆ¬¬ ®´å∂ ˆ†≥ Óøπ´ƒ¨¬¬¥ ¥ø¨ çå˜ ƒˆ˜∂ å ∑å¥≥ ∫¥¨ç†ƒ”∂ø˜†—¬´å√´—ßø∂å—∫¥—¥ø¨®—˚´¥∫øå®∂’
"""

for c in message:
    if c in key:
        print(key[c], end='')
    else:
        print(c, end='')
