# Dominant Character

**Problem ID:** 1605C  
**Platform:** Codeforces  
**Problem Link:** https://codeforces.com/problemset/problem/1605/C  

---

## 🧩 Problem Statement

Ashish has a string `s` of length `n` containing only characters `'a'`, `'b'`, and `'c'`.  
He wants to find the length of the **smallest substring** that satisfies all of the following conditions:

- The substring has **length at least 2**.
- The number of `'a'` characters in the substring is **strictly greater** than the number of `'b'` characters in that substring.
- The number of `'a'` characters in the substring is **strictly greater** than the number of `'c'` characters in that substring.

A string `a` is considered a **substring** of string `b` if `a` can be obtained by deleting zero or more characters from the beginning and zero or more characters from the end of `b`.  
Help Ashish find the **minimum possible length** of such a substring, or print `-1` if no such substring exists.

---

## 📥 Input

- The first line contains a single integer `t` — the number of test cases.
- Each test case consists of two lines:
  - The first line contains an integer `n` — the length of the string `s`.
  - The second line contains the string `s`, consisting only of characters `'a'`, `'b'`, and `'c'`.

It is guaranteed that the sum of all `n` values over all test cases does not exceed `10^6`. :contentReference[oaicite:0]{index=0}

---

## 📤 Output

For each test case, output a single integer — the **minimum length** of a substring that satisfies the given conditions, or `-1` if no such substring exists. :contentReference[oaicite:1]{index=1}

---

## 📌 Constraints

- `1 ≤ t ≤ 10^5`
- `2 ≤ n ≤ 10^6`
- The string contains only `'a'`, `'b'`, `'c'`.  
- Total sum of `n` over all test cases ≤ `10^6`. :contentReference[oaicite:2]{index=2}

---

## 📝 Example
```
### Input
3
2
aa
5
cbabb
8
cacabccc


### Output
2
-1
3

```
---

## 💡 Explanation

### Example 1  
String: `aa`  
The substring `aa` itself has 2 `'a'` characters and 0 `'b'` and `'c'`, so it satisfies the condition. Length = 2.

### Example 2  
String: `cbabb`  
No substring of length ≥ 2 has `'a'` occurring strictly more times than `'b'` and `'c'` simultaneously.

### Example 3  
String: `cacabccc`  
One valid substring is `"aca"`, where `'a'` occurs twice while `'b'` and `'c'` occur once or less. The minimum length satisfying all conditions is 3. :contentReference[oaicite:3]{index=3}

---

## 🧠 Notes

A brute force check of all substrings is too slow for large `n`. Efficient solutions typically exploit the fact that **only short substrings (length ≤ 7)** need to be checked to determine the answer, because when `'a'` is dominant, longer qualifying substrings contain qualifying short ones inside them.

---
