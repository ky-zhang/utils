import os
import numpy
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import argparse
from PIL import Image

parser = argparse.ArgumentParser()

parser.add_argument('-input', default = '', help = 'input file folder')
parser.add_argument('-label', default = '', help = 'label file')
parser.add_argument('-output', default = '', help = 'output file folder')
parser.add_argument('-range', default = '', help = 'axis range')

args = parser.parse_args()

label = []
if args.label != '':
    for line in open(args.label):
        label.append(line.strip())

files = os.listdir(args.input)
for file in files:
    filepath = os.path.join("%s%s" %(args.input, file))
    out_png_path = os.path.join("%s%s" %(args.output, file))
    out_png_path = out_png_path.replace("txt", "png")
    N = M = 0
    all_data = {}
    for i, line in enumerate(open(filepath)):
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
        plt.plot(x, y, '.', color = color, markersize = 1)
    if args.range != '':
        l = abs(float(args.range))
        plt.xlim(-l, l)
        plt.ylim(-l, l)
    # 坐标轴
    plt.axis('off')
    plt.savefig(out_png_path, dpi = 300)
    plt.close("all")

    # 背景透明
    # img = Image.open(out_png_path)
    # img = img.convert("RGBA")
    # datas = img.getdata()
    # newData = list()
    # for item in datas:
    #     if item[0] >220 and item[1] > 220 and item[2] > 220:
    #         newData.append(( 255, 255, 255, 0))
    #     else:
    #         newData.append(item)
    
    # img.putdata(newData)
    # img.save(out_png_path,"PNG")

