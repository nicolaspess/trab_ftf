# C++ compiler
CC = g++ 
CC_FLAGS = -fopenmp -std=c++11

destDir_dup = /tmp/RBTree-dup

all_dup: gen_bin_dup gen_data_dup mv_bin_dup

gen_bin_dup: main_dup.cpp RBTree.cpp
	$(CC) $(CC_FLAGS) -o main_dup main_dup.cpp RBTree.cpp

gen_data_dup: gen_bin_dup
	./main_dup input_100000 gold_100000 tmp/RBTree-dup/RBTree-dup-detection.log tmp/RBTree-dup/output2_100000

mv_bin_dup: gen_data_dup
	mkdir -p $(destDir_dup)
	mv main_dup $(destDir_dup)
	cp input_100000 $(destDir_dup)
	cp gold_100000 $(destDir_dup)
	cp output2_100000 $(destDir_dup)
	@echo "All Done, executables should be in the $(destDir_dup)"

clean:
	clear
	rm -rf *.o
	rm -rf main
	rm -rf output2_100000
	rm -rf main_dup
