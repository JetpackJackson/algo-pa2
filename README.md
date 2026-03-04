---
title: COP4533 - Programming Assignment 2
author:
- 'Bailey Watkins (UFID: 97706540)'
- 'Patrick McCormack (UFID: 73709580)'
date: 3/2/2026
documentclass: article
geometry: margin=1in
papersize: letter
---

# Readme
## Environment Setup
- Run `make init`.

## Running the code
- Run `make run` if you wish to manually type the input data (you will be prompted for the proper format.)
- Run `make run assets/<file>` if you wish to run the code with a provided input file.

## Compiling the README
- Run `make doc` to use Pandoc and \LaTeX to create a PDF version of the README.

# Written Component

### Question 1.

sample1.txt: <br>
&emsp; k = 4, m = 50 <br>
&emsp; FIFO = 4 <br>
&emsp; LRU = 4 <br>
&emsp; OPTFF = 4 <br>
sample2.txt: <br>
&emsp; k = 5, m = 55 <br>
&emsp; FIFO = 35 <br>
&emsp; LRU = 34 <br>
&emsp; OPTFF = 22 <br>
sample3.txt: <br>
&emsp; k = 6, m = 60 <br>
&emsp; FIFO = 60 <br>
&emsp; LRU = 60 <br>
&emsp; OPTFF = 55 <br>

OPTFF was by far the most efficient out of the three. 
Whereas all three algorithms got the same result for the first test (due to the consistent repetition),
In the second and third tests, the OPTFF outperformed both FIFO and LRU, especially in the second test significantly.
<br>
<br>
As for FIFO compared to LRU, they both did about the same, although in the second test LRU had one less miss than FIFO.

### Question 2.


