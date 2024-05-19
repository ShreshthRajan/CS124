#!/bin/bash
make
for i in {7..18}
do
./generatemst 0 $((2**i)) 5 0
done