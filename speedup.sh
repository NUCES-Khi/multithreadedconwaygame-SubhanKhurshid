#!/bin/bash

for i in {1..8}
do
    echo "Running program with $i threads"
    time ./aba $i
done
