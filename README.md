---
title: COP4533 - Programming Assignment 2
author:
- 'Bailey Watkins (UFID: 97706540)'
- 'Patrick McCormack (UFID: 73709580)'
date: 3/6/2026
documentclass: article
geometry: margin=1in
papersize: letter
---

# Readme
## Environment Setup
- Run `make init`.

## Running the code
- Run `make run` if you wish to manually type the input data (you will be prompted for the proper format.)
- Run `make run assets/<file>` if you wish to run the code with a provided input file. You may place any input files into the assets folder and run the code using them by providing the file name.

## Compiling the README
- Run `make doc` to use Pandoc and \LaTeX to create a PDF version of the README.

# Written Component

## Question 1: Empirical Comparison

Use **at least three nontrivial input files** (each containing 50 or more requests).

For each file, report the number of cache misses for each policy.

\begin{tabular}{|l|l|l|l|l|l|}
\hline
Input File & k  & m   & FIFO  & LRU & OPTFF \\ \hline
sample1    & 4  & 50  & 4     &  4  & 4     \\ \hline
sample2    & 5  & 55  & 35    & 34  & 22    \\ \hline
sample3    & 6  & 60  & 60    & 60  & 55    \\ \hline
\end{tabular}

Briefly comment:

- Does OPTFF have the fewest misses?
	- **Answer**: OPTFF was by far the most efficient out of the three. Whereas all three algorithms got the same result for the first test (due to the consistent repetition), In the second and third tests, the OPTFF outperformed both FIFO and LRU, especially in the second test significantly.

- How does FIFO compare to LRU?
	- **Answer**: As for FIFO compared to LRU, they both did about the same, although in the second test LRU had one less miss than FIFO.

## Question 2: Bad Sequence for LRU or FIFO

For ( k = 3 ), investigate whether there exists a request sequence for which OPTFF incurs **strictly fewer misses** than LRU (or FIFO).

- If such a sequence exists:
	- Construct one.
	- Compute and report the miss counts for both policies.
- If you believe no such sequence exists for the policy you chose:
	- Provide a clear justification.

- **Answer**: The sequence is provided in `assets/q2.txt`. It has k = 3, m = 7, and is the sequence 1 2 3 4 1 2 4.

\begin{tabular}{|l|l|l|l|l|l|}
\hline
Input File & k  & m   & FIFO  & LRU & OPTFF \\ \hline
q2         & 3  & 7   & 6     &  6  & 4     \\ \hline
\end{tabular}

In either case, briefly explain your reasoning.

- **Answer**: The sequence is constructed such that LRU eventually evicts 1 at the same step that OPTFF evicts 3, which has a cascading effect for LRU where it retains the "wrong" values. This results in OPTFF having strictly fewer misses.

\begin{tabular}{|l|l|l|}
\hline
Step & OPTFF                          & LRU                           \\ \hline
1    & (empty) to A                   & (empty) to A                  \\ \hline
2    & A to AB                        & A to AB                       \\ \hline
3    & AB to ABC                      & AB to ABC                     \\ \hline
4    & ABC to \textcolor{blue}{ABD}   & ABC to \textcolor{red}{BCD}   \\ \hline
5    & ABD to ABD (hit)               & BCD to CDA                    \\ \hline
6    & ABD to ABD (hit)               & CDA to DAB                    \\ \hline
7    & ABD to ABD (hit)               & DAB to DAB (hit)              \\ \hline
\end{tabular}

## Question 3: Prove OPTFF is Optimal

Let OPTFF be Belady’s Farthest-in-Future algorithm.

Let ( A ) be any offline algorithm that knows the full request sequence.

Prove that the number of misses of OPTFF is no larger than that of ( A ) on any fixed sequence.

- **Answer**: The way that OPTFF operates means that it can "see the future" and sets aside cache items better than FIFO or LRU (see above) so by definition, OPTFF cannot miss more than an algorithm that knows the sequence.
