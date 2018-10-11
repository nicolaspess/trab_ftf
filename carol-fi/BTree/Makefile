# C++ compiler
CC = g++
CC_FLAGS = -fopenmp -std=c++11

destDir = /tmp/BTree

all: gen_bin gen_data mv_bin

gen_bin: BTree.cpp
	 $(CC) $(CC_FLAGS) -g -o main BTree.cpp

gen_data: gen_bin
	./main input_100000 gold_100000

mv_bin: gen_data
	mkdir -p $(destDir)
	mv main input_100000 gold_100000 $(destDir)
	@echo "All Done, executables should be in the $(destDir)"
