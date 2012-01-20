# -*- coding: utf-8 -*-

from PIL import Image
import simplejson

WIDTH = HEIGHT = 32

class ImTrans:
    def __init__(self, im):
        self.im = im

    def getMean(self,data):
        pixels = data.getdata()
	r,g,b,s = 0,0,0,0
        for p in pixels:
            r += p[0]
            g += p[1]
            b += p[2]
            s += 1
        return (r/s,g/s,b/s)

    def transform(self):
        i = Image.open(self.im)
        pix = i.load()
        wi,he = i.size
        chunks = []
	for r in range(0,he,HEIGHT):
            tmplist = []
            for h in range(0,wi,WIDTH):
                data = i.crop((h,r,h+WIDTH,r+HEIGHT))
		tmplist.append(self.getMean(data))
            chunks.append(tmplist)
        print "chunks = ",simplejson.dumps(chunks),";"
	print "imW = ",wi,";"
	print "imH = ",he,";"

if __name__ == '__main__':
    ImTrans("../RomaMedieval/DSC04105.JPG").transform()
