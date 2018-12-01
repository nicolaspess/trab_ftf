# C++ compiler
CC = g++
CC_FLAGS = -fopenmp -std=c++11

destDir = /tmp/BTree-dup

all: gen_bin gen_data mv_bin

gen_bin: BTree_dup.cpp
	 $(CC) $(CC_FLAGS) -g -o main BTree_dup.cpp

gen_data: gen_bin
	./main input_100000 gold_100000 tmp/BTree-dup-detection.log tmp/output_100000

mv_bin: gen_data
	mkdir -p $(destDir)
	mv main input_100000 gold_100000 $(destDir)
	@echo "All Done, executables should be in the $(destDir)"
