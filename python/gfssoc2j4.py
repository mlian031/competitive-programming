# problem:
# It was a peaceful day in the life of a student, when suddenly Timothy Li messages you about some strange anime called Date a Live.
# There are N episodes in the series, and each episode i has a rating k_i from 1 to 10. 
# Being super bored, you decide to give it a try. Unfortunately, you cannot live without food through the entire afternoon and the 
# anime streamer you are using does not have a pause button for some reason. 
# Thus, to make an intelligent decision on when to go make food, you have Q queries in the form a b. 
# For each of these queries, you will simulate skipping episodes a to b (inclusive), and output the sum of the ratings of the episodes you do not skip.

# input specification
# The first line of input contains 2 integers, space separated — N, Q.
# The next line contains N integers, space separated. The i-th of these integers represents the rating of the i-th episode.
# The next Q lines contain integers a_i and b_i, the episodes that are skipped.


# use fast input
import sys

N, Q = map(int, sys.stdin.readline().split())

ratings = list(map(int, sys.stdin.readline().split()))

psa = [0] * (N + 1)

for i in range(1, N+1):
    psa[i] = psa[i-1] + ratings[i-1]

for _ in range(Q):
    a, b = map(int, sys.stdin.readline().split())
    print(psa[N] - (psa[b] - psa[a-1]))