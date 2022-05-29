from PIL import Image, ImageChops

CODE_SIZE = 27

tmp_qr = Image.new(mode='1', size=(CODE_SIZE, CODE_SIZE), color=1)
qr_flag = Image.new(mode='1', size=(CODE_SIZE, CODE_SIZE), color=1)

with Image.open('xqr.png') as image:
	IMAGE_SIZE = image.size[0]
	for start_y in range(0, IMAGE_SIZE, CODE_SIZE):
		for start_x in range(0, IMAGE_SIZE, CODE_SIZE):
			for y in range(0, CODE_SIZE):
				for x in range(0, CODE_SIZE):
					p = image.getpixel((start_x + x, start_y + y))
					tmp_qr.putpixel((x, y), p)
			if start_x == start_y == 0:
				qr_flag = tmp_qr.copy()
			else:
				qr_flag = ImageChops.logical_xor(qr_flag, tmp_qr)

qr_flag.save('flag.png')
