# Utils Usage

### Bash

`DR_plot.sh`: you can test different datasets in this way.
```Vim
$ bash DR_plot.sh
```

`Graph_Layout.py`: if you want to change the parameters of the algorithm, you can go into the `Graph_Layout.py`, and make some changes in it. If there are many datasets to test, you can also write a bash script to run the `Graph_Layout.py`.

### Plot
`plot.py`: you can plot one picture once.
```
python3 plot.py -input mnist_vec2D.txt -label mnist_label.txt -output mnist_vec2D_plot
```

`plot_folder.py`: you can plot a folder's file one time.
```
python3 plot_folder.py -input ./out/ -output ./png/ -label ../mnist_label.txt
```