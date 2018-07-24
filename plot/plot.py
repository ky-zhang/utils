import numpy
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import argparse
from PIL import Image

parser = argparse.ArgumentParser()

parser.add_argument('-input', default = '', help = 'input file')
parser.add_argument('-label', default = '', help = 'label file')
parser.add_argument('-output', default = '', help = 'output file')
parser.add_argument('-range', default = '', help = 'axis range')

args = parser.parse_args()

label = []
if args.label != '':
    for line in open(args.label):
        label.append(line.strip())

N = M = 0
all_data = {}
for i, line in enumerate(open(args.input)):
    vec = line.strip().split(' ')
    if i == 0:
        N = int(vec[0])
        M = int(vec[1])
    elif i <= N:
        if args.label == '':
            label.append(0)
        all_data.setdefault(label[i-1], []).append((float(vec[-2]), float(vec[-1])))

colors = plt.cm.rainbow(numpy.linspace(0, 1, len(all_data)))

for color, ll in zip(colors, sorted(all_data.keys())):
    x = [t[0] for t in all_data[ll]]
    y = [t[1] for t in all_data[ll]]
    #plt.plot(x, y, '.', color = color, ms = 1)
    plt.scatter(x, y, color = color, s= 1, marker= '.',linewidth = 0 )

if args.range != '':
    l = abs(float(args.range))
    plt.xlim(-l, l)
    plt.ylim(-l, l)

plt.axis('off')
plt.savefig(args.output, dpi = 500)
plt.close("all")

img = Image.open(args.output+".png")
img = img.convert("RGBA")
datas = img.getdata()
newData = list()
for item in datas:
    if item[0] >220 and item[1] > 220 and item[2] > 220:
        newData.append(( 255, 255, 255, 0))
    else:
        newData.append(item)

img.putdata(newData)
img.save(args.output+".png","PNG")
