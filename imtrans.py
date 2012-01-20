# -*- coding: utf-8 -*-

from PIL import Image
import simplejson

WIDTH = HEIGHT = 32
"""	this.canvas.width = this.im.naturalWidth;
	this.canvas.height = this.im.naturalHeight;
	this.context.drawImage(this.im,0,0);
	var chunks = [];
	// Trossos d'alçada
	for (var r=0; r<this.canvas.height; r += HEIGHT) {
		var tmplist = [];
		for (var h=0; h<this.canvas.width; h += WIDTH) { // Trossos horitzontals
			var data = this.context.getImageData(h,r,h+WIDTH,r+HEIGHT).data;
			var sum = 0;
			var rg = 0;
			var g = 0;
			var b = 0;
			for (var i=0; i<data.length; i += 4) {
				rg += data[i];
				g += data[i+1];
				b += data[i+2];
				sum += 1;
			}
			tmplist[tmplist.length] = [Math.round(rg/sum),Math.round(g/sum),Math.round(b/sum)];
		}
		chunks[chunks.length] = tmplist;
	}"""

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
    ImTrans("../RomaMedieval/DSC04206.JPG").transform()
