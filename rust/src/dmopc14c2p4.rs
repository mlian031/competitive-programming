// # problem:
// # The Logging Company has a long line of  N   ( 1 ≤ N ≤ 1 000 000 )  
// # trees numbered from  0  to  N − 1 . Each tree i has a mass  m_i ( 0 ≤ m i ≤ 2000 ).
// # The Company wants to cut some of the trees, so they hired you to calculate the mass of 
// # all the wood they would get from cutting all the trees between positions a and b inclusive 
// # (0 ≤ a , b < N). In particular, they want you to answer Q (1 ≤ Q ≤ 1 000 000) 
// # such queries.

// # input specification
// # first line: N
// # lines 2 to N+1: line i + 2 is the mass of the tree i, m_i
// # the line N + 2 will contain the integer Q, the number of queries the logging company wants to make
// # the next Q lines will contain the integers a and b

use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let mut lines = stdin.lock().lines().map(|l| l.unwrap());
    let n: usize = lines.next().unwrap().parse().unwrap();
    let mass: Vec<i32> = lines.by_ref().take(n).map(|l| l.parse().unwrap()).collect();
    let q: usize = lines.next().unwrap().parse().unwrap();

    let mut prefix_sum: Vec<i32> = vec![0; n + 1];
    for i in 0..n {
        prefix_sum[i + 1] = prefix_sum[i] + mass[i];
    }
    for _ in 0..q {
        let query: Vec<usize> = lines.next().unwrap().split_whitespace().map(|x| x.parse().unwrap()).collect();
        let a = query[0];
        let b = query[1];
        println!("{}", prefix_sum[b + 1] - prefix_sum[a]);
    }
}
