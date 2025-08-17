#!/usr/bin/env python

import base64
from PIL import Image
import fileinput
from io import BytesIO

def getBase64(pngfile,x,y,width,height):
    im=Image.open(pngfile)
    buffered=BytesIO()
    im.crop((x,y,x+width,y+height)).save(buffered,format="PNG")
    return base64.b64encode(buffered.getvalue()).decode('ascii')

print('<defs>')
blockSize=1
for line in fileinput.input():
    if line[0]=="#":
        continue
    if line[0]=="%":
        blockSize=int(line.removeprefix("%"))
    line=line.rstrip()
    params=line.split(" ")
    if len(params)<6:
        continue
    b64string = getBase64(params[0],int(params[1])*blockSize,int(params[2])*blockSize,int(params[3])*blockSize,int(params[4])*blockSize)
    print('    <image id ="'+params[5]+'"x="0" y="0" width="'+str(int(params[3])*blockSize)+'" height="'+str(int(params[4])*blockSize)+'" href="data:image/png;base64,'+b64string+'"/>')
print('</defs>')
