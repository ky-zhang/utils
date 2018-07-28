str="cifar10"
./Vis -knn_k 100 -L 200 -checkK 200 -S 20 -iter 500 -gamma 8.7 -klevel 2 -input ./data/"$str"_data.txt -label ./data/"$str"_label.txt -knn_type efanna -output ./data/result/result1/
python3 ./data/plot/plot.py -input ./data/result/result1/"$str"/"$str"_vec2D.txt -label ./data/"$str"_label.txt -output ./plot/"$str"_vec2D_plot

str="cifar100"
./Vis -knn_k 100 -L 200 -checkK 200 -S 20 -iter 500 -gamma 8.7 -klevel 2 -input ./data/"$str"_data.txt -label ./data/"$str"_label.txt -knn_type efanna -output ./data/result/result1/
python3 ./data/plot/plot.py -input ./data/result/result1/"$str"/"$str"_vec2D.txt -label ./data/"$str"_label.txt -output ./plot/"$str"_vec2D_plot

str="fashion_mnist"
./Vis -knn_k 100 -L 200 -checkK 200 -S 20 -iter 500 -gamma 8.7 -klevel 2 -input ./data/"$str"_data.txt -label ./data/"$str"_label.txt -knn_type efanna -output ./data/result/result1/
python3 ./data/plot/plot.py -input ./data/result/result1/"$str"/"$str"_vec2D.txt -label ./data/"$str"_label.txt -output ./plot/"$str"_vec2D_plot

str="mnist_vec784D"
./Vis -knn_k 100 -L 200 -checkK 200 -S 20 -iter 500 -gamma 8.7 -klevel 2 -input ./data/"$str"_data.txt -label ./data/"$str"_label.txt -knn_type efanna -output ./data/result/result1/
python3 ./data/plot/plot.py -input ./data/result/result1/"$str"/"$str"_vec2D.txt -label ./data/"$str"_label.txt -output ./plot/"$str"_vec2D_plot

str="svhn"
./Vis -knn_k 100 -L 200 -checkK 200 -S 20 -iter 500 -gamma 8.7 -klevel 2 -input ./data/"$str"_data.txt -label ./data/"$str"_label.txt -knn_type efanna -output ./data/result/result1/
python3 ./data/plot/plot.py -input ./data/result/result1/"$str"/"$str"_vec2D.txt -label ./data/"$str"_label.txt -output ./plot/"$str"_vec2D_plot
