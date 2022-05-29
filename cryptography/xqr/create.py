import qrcode, time, os
from string import ascii_letters, digits
from random import choice
from PIL import Image, ImageChops

START_TIME = time.time()

VALID_CHARS = ascii_letters + digits + '{_}'

FLAG = 'byuctf{x0r_i5_u5eful}'

QR_FLAG = qrcode.QRCode(box_size=1, border=1)
QR_FLAG.add_data(FLAG)
QR_FLAG = QR_FLAG.make_image()

CODE_SIZE = QR_FLAG.size[0]
CODES_PER_EDGE = 101
IMAGE_SIZE = CODE_SIZE * CODES_PER_EDGE

image = Image.new(mode='1', size=(IMAGE_SIZE, IMAGE_SIZE), color=1)
pixels = image.load()
keystone = QR_FLAG

generated_count = 0

for start_y in range(0, IMAGE_SIZE, CODE_SIZE):
	for start_x in range(0, IMAGE_SIZE, CODE_SIZE):
		generated_count += 1
		if start_x == start_y == (CODES_PER_EDGE // 2) * CODE_SIZE:
			continue
		qr = qrcode.QRCode(box_size=1, border=1)
		qr.add_data(''.join([choice(VALID_CHARS) for _ in range(len(FLAG))]))
		qr = qr.make_image()
		keystone = ImageChops.logical_xor(keystone, qr)
		qr_pixels = qr.load()
		for y in range(0, CODE_SIZE):
			for x in range(0, CODE_SIZE):
				val = qr_pixels[x, y]
				pixels[start_x + x, start_y + y] = val
	os.system('clear')
	print(f'Progress: {generated_count}/{CODES_PER_EDGE**2} QRs Generated')
	print(f'Time Elapsed: {int(time.time() - START_TIME)} seconds')

start_x = start_y = (CODES_PER_EDGE // 2) * CODE_SIZE

keystone_pixels = keystone.load()
for y in range(0, CODE_SIZE):
	for x in range(0, CODE_SIZE):
		val = keystone_pixels[x, y]
		pixels[start_x + x, start_y + y] = val

image.save('xqr.png')
