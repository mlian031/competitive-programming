

# problem:
# The Logging Company has a long line of  N   ( 1 ≤ N ≤ 1 000 000 )  
# trees numbered from  0  to  N − 1 . Each tree i has a mass  m_i ( 0 ≤ m i ≤ 2000 ).
# The Company wants to cut some of the trees, so they hired you to calculate the mass of 
# all the wood they would get from cutting all the trees between positions a and b inclusive 
# (0 ≤ a , b < N). In particular, they want you to answer Q (1 ≤ Q ≤ 1 000 000) 
# such queries.

# input specification
# first line: N
# lines 2 to N+1: line i + 2 is the mass of the tree i, m_i
# the line N + 2 will contain the integer Q, the number of queries the logging company wants to make
# the next Q lines will contain the integers a and b


# use fast input
import sys
input = sys.stdin.readline

N = int(input())

psa = [0] * (N+1)

for i in range(1, N+1):
    psa[i] = psa[i-1] + int(input())

Q = int(input())
for i in range(Q):
    # inline input for a and b
    a, b = map(int, input().split())
    print(psa[b+1] - psa[a])
