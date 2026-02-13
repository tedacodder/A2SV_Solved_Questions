# Beautiful Matrix

**Problem ID:** 263A  
**Platform:** Codeforces  
**Problem Link:** https://codeforces.com/problemset/problem/263/A  

---

## 🧩 Problem Statement

You are given a **5 × 5 matrix** that contains exactly **24 zeros** and **a single number 1**.

Rows are numbered from **1 to 5** (top to bottom).  
Columns are numbered from **1 to 5** (left to right).

In one move, you can perform one of the following operations:

- Swap two neighboring rows (row `i` and row `i+1`, where `1 ≤ i < 5`)
- Swap two neighboring columns (column `j` and column `j+1`, where `1 ≤ j < 5`)

A matrix is considered **beautiful** if the single `1` is located at the center position — that is, at **row 3 and column 3**.

Your task is to determine the **minimum number of moves** required to make the matrix beautiful.

---

## 📥 Input

- Five lines follow.
- Each line contains five integers.
- The matrix contains exactly one `1` and twenty-four `0`s.

---

## 📤 Output

Print a single integer — the **minimum number of moves** required to move the `1` to the center of the matrix.

---

## 📌 Constraints

- The matrix size is always `5 × 5`
- Exactly one element is `1`
- All other elements are `0`

---

cat << 'EOF' > examples.md
## 📝 Example 1

### Input
0 0 0 0 0
0 0 0 0 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0

### Output
3

---

## 📝 Example 2

### Input
0 0 0 0 0
0 0 0 0 0
0 1 0 0 0
0 0 0 0 0
0 0 0 0 0

### Output
1
EOF


---

## 💡 Explanation

To solve the problem:

1. Locate the position `(row, column)` of the number `1`.
2. Compute the **Manhattan distance** from that position to the center `(2, 2)`.

### Formula

moves = |row − 2| + |column − 2|


That value represents the **minimum number of moves** required.

---

## 🚀 Approach Summary

- Iterate through the 5 × 5 matrix.
- Find coordinates of `1`.
- Apply Manhattan distance formula.
- Print the result.

---



