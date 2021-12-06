from sys import stdin

wide = 25
tall = 6

layerlen = wide*tall

layerstart = '2'*layerlen

def layerPrint(s):
  a = []
  for c in s:
    if c == '1':
      a.append('■')
    else:
      a.append(' ')
  s = ''.join(a)
  i = 0
  while i < len(s):
    print(s[i:i+wide])
    i += wide

image = stdin.readline()
imagelen = len(image)
i = layerlen
while i < imagelen:
  layer = image[i-layerlen:i]
  newimage = []
  for a,b in zip(layer,layerstart):
    if b == '2':
      newimage.append(a)
    else:
      newimage.append(b)
  layerstart = ''.join(newimage)
  i += layerlen

layerPrint(layerstart)
