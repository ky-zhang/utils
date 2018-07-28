#coding=utf-8
import GraphLayout as gl
import argparse
import networkx as nx
import pylab
import numpy as np
import argparse
import os
import time
import sys
import evaluation as ev
import warnings
from PIL import Image
import codecs

def fxn():
    warnings.warn("deprecated", DeprecationWarning)

class ShowProcess():

    i = 0
    max_steps = 0
    max_arrow = 50

    def __init__(self, max_steps):
        self.max_steps = max_steps
        self.i = 0


    def show_process(self, i=None):
        if i is not None:
            self.i = i
        else :
            self.i += 1
        num_arrow = int(self.i * self.max_arrow / self.max_steps)
        num_line = self.max_arrow - num_arrow
        percent = self.i * 100.0 / self.max_steps
        process_bar = '[' + '>' * num_arrow + '-' * num_line + ']'\
                      + '%.2f' % percent + '%' + '\r'
        sys.stdout.write(process_bar)
        sys.stdout.flush()

    def close(self, words='done'):
        print words
        self.i = 0

def txtToPng(infolder, outfolder, edgesfile):
    files = os.listdir(infolder)
    process_bar = ShowProcess(len(files))
    for file in files:
        process_bar.show_process()
        time.sleep(0.05)
        filepath = os.path.join("%s%s" %(infolder, file))
        out_png_path = os.path.join("%s%s" %(outfolder, file))
        out_png_path = out_png_path.replace("txt", "png")
        f = open(filepath)
        line = f.readline()
        G=nx.Graph()
        index = -1
        while line:
            index = index + 1
            if index == -1:
                continue

            line = f.readline()
            ll = line.split(' ')
            if len(ll) < 3:
                continue

            i = float(ll[1])
            j = float(ll[2])
            G.add_node(index ,pos=(i,j))
        f.close()


        f = open(edgesfile)
        line = f.readline()
        lint = f.readline()
        while line:
            line = f.readline()
            ll = line.split(' ')
            if len(ll) < 3:
                continue
            i = int(ll[0])
            j = int(ll[1])
            if i == j:
                continue
            G.add_edges_from([(i,j)])
        f.close()
        pos=nx.get_node_attributes(G,'pos')
        nx.draw(G,pos, node_color='white', edge_color='black', node_size=0, alpha=1, width = 0.2)
        pylab.title('Self_Define Net',fontsize=15)
        pylab.savefig(out_png_path, dpi = 800)
        img = Image.open(out_png_path)
        img = img.convert("RGBA")
        datas = img.getdata()
        newData = list()
        for item in datas:
            if item[0] >220 and item[1] > 220 and item[2] > 220:
                newData.append(( 255, 255, 255, 0))
            else:
                newData.append(item)
        img.putdata(newData)
        img.save(out_png_path,"PNG")
        pylab.close('all')
    process_bar.close('done')

def Execute(args):
    ft = codecs.open("summary.txt",'a')
    ft.write(args.input + '\n')
    for i in range(1, args.ith):
        print("\n" + "-" * 30 + "GRAPHLAYOUT" + "-" * 30)
        gl.loadFromGraph(args.input)
        gl.timerStart()
        gl.shortestPathLength(args.dismax)
        # gl.timerEnd()
        # print('Cpu time:' + str(gl.timerCpuTime()))
        # print('Real time:' + str(gl.timerRealTime()))


        #需要设置一个最小团个数
        gl.genMultilevel(100)

        # gl.timerStart()
        gl.computeSimilarity(args.threads, args.perp, args.dismax)
        # gl.timerEnd()
        # print('Cpu time:' + str(gl.timerCpuTime()))
        # print('Real time:' + str(gl.timerRealTime()))

        isout = 0
        if len(args.outfolder) > 0:
            isout = 1
        # gl.timerStart()
        gl.run(args.outdim, args.threads, args.samples, args.alpha, args.neg, args.gamma, isout, args.outfolder)
        gl.timerEnd()
        print('Total Cpu time:' + str(gl.timerCpuTime()))
        print('Total Real time:' + str(gl.timerRealTime()))

        gl.save(args.output.replace(".txt", "_" + str(i) + ".txt"))

        # with warnings.catch_warnings():
        #     warnings.simplefilter("ignore")
        #     txtToPng(args.outfolder, 'png/', args.input)
        #     fxn()

        # ev.evaluation(args.input, args.output)

        ft.write(str(gl.timerRealTime()) + '\n')
    ft.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-input', default = '', help = 'input file')
    parser.add_argument('-output', default = '', help = 'output file')
    parser.add_argument('-outdim', default = -1, type = int, help = 'output dimensionality')
    parser.add_argument('-threads', default = 8, type = int, help = 'number of training threads')
    parser.add_argument('-samples', default = -1, type = int, help = 'number of training mini-batches')
    parser.add_argument('-prop', default = -1, type = int, help = 'number of propagations')
    parser.add_argument('-alpha', default = -1, type = float, help = 'learning rate')
    parser.add_argument('-neg', default = -1, type = int, help = 'number of negative samples')
    parser.add_argument('-neigh', default = -1, type = int, help = 'number of neighbors in the NN-graph')
    parser.add_argument('-gamma', default = -1, type = float, help = 'weight assigned to negative edges')
    parser.add_argument('-perp', default = 50.0, type = float, help = 'perplexity for the NN-grapn')
    parser.add_argument('-dismax', default = 2 << 22, type = int, help = 'The max distance user for breadth first search. Default is 2^23.')
    parser.add_argument('-outfolder', default = './out/', help = 'The folder user for saving intermediate result.')
    parser.add_argument('-ith', default = 1, type = int, help = 'The iteration of the algorithm.')

    args = parser.parse_args()
    isout = 0
    if len(args.outfolder) > 0:
        isout = 1

    gl.loadFromGraph(args.input)
    gl.shortestPathLength(args.dismax)
    gl.genMultilevel(100)
    gl.computeSimilarity(args.threads, args.perp, args.dismax)
    gl.run(args.outdim, args.threads, args.samples, args.alpha, args.neg, args.gamma, isout, args.outfolder)
    gl.save(args.output)
    #Execute(args)
