import PIL
from PIL import Image

def blur(fileName,combine=False):
	preAA = Image.open(fileName)
	width,height =preAA.size
	postAA = Image.new('RGB',(width,height),(255,255,255))

	for column in range(width):
		for row in range(height):

			redTw,greenTw,blueTw = preAA.getpixel(((column+1)%width,row))
			redTh,greenTh,blueTh = preAA.getpixel(((column-1)%width,row))

			redFo,greenFo,blueFo = preAA.getpixel((column,(row+1)%height))
			redFi,greenFi,blueFi = preAA.getpixel((column,(row-1)%height))

			redAve = int((redTw+redTh+redFo+redFi)/4)
			greenAve = int((greenTw+greenTh+greenFo+greenFi)/4)
			blueAve = int((blueTw+blueTh+blueFo+blueFi)/4)

			postAA.putpixel((column,row),(redAve,greenAve,blueAve))

	if not combine:
		postAA.save(fileName[:len(fileName)-4]+'_output.PNG','png')
	else:
		combined = Image.new('RGB',(width,height),(255,255,255))

		for column in range(width):
			for row in range(height):

				redPre,greenPre,bluePre = preAA.getpixel((column,row))
				redPost,greenPost,bluePost = postAA.getpixel((column,row))

				redAve = (redPre+redPost)/2
				greenAve=(greenPre+greenPost)/2
				blueAve=(bluePre+bluePost)/2

				combined.putpixel((column,row),(redAve,greenAve,blueAve))

		combined.save(fileName[:len(fileName)-4]+'_output.PNG','png')