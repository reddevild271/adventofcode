from sys import stdin

wide = 25
tall = 6

layerlen = wide*tall

fewest = layerlen
answer = 0

image = stdin.readline()
imagelen = len(image)
i = layerlen
while i < imagelen:
  layer = image[i-layerlen:i]
  zerocount = layer.count('0')
  if zerocount < fewest:
    fewest = zerocount
    answer = layer.count('1')*layer.count('2')
  i += layerlen

print(answer)
