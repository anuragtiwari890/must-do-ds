# Array Problems - Must Do DSA

This directory contains 17 fundamental array problems with their optimal solutions. Each problem includes multiple approaches with the best solution implemented.

## Table of Contents

1. [Array Rotation](#1-array-rotation)
2. [Majority Element](#2-majority-element)
3. [Adding One to Number Array](#3-adding-one-to-number-array)
4. [Rearrange Alternating Positive Negative Items](#4-rearrange-alternating-positive-negative-items)
5. [Product Array Puzzle](#5-product-array-puzzle)
6. [Find Frequency of Elements in Limited Range](#6-find-frequency-of-elements-in-limited-range)
7. [Factorial of Large Number](#7-factorial-of-large-number)
8. [Minimum Jumps to Reach End](#8-minimum-jumps-to-reach-end)
9. [Kth Element of Two Sorted Arrays](#9-kth-element-of-two-sorted-arrays)
10. [Find Row with Maximum Number of 1s](#10-find-row-with-maximum-number-of-1s)
11. [Buy and Sell Stock](#11-buy-and-sell-stock)
12. [Longest Consecutive Subsequence](#12-longest-consecutive-subsequence)
13. [Maximum j - i such that arr[i] ≤ arr[j]](#13-maximum-j---i-such-that-arri--arrj)
14. [Trapping Rain Water](#14-trapping-rain-water)
15. [Triplet Sum Closest to Target](#15-triplet-sum-closest-to-target)
16. [Maximum Sum in Subarray (Kadane's Algorithm)](#16-maximum-sum-in-subarray-kadanes-algorithm)
17. [Merge Two Sorted Arrays](#17-merge-two-sorted-arrays)

---

## 1. Array Rotation

**Problem**: Rotate an array to the left by `d` positions.

**Example**: 
- Input: `arr[] = {1, 2, 3, 4, 5, 6}`, `d = 2`
- Output: `{3, 4, 5, 6, 1, 2}`

**Best Solution**: Reverse Algorithm - **O(n) time, O(1) space**
- Reverse first d elements
- Reverse remaining n-d elements  
- Reverse entire array

---

## 2. Majority Element

**Problem**: Find the element that appears more than n/2 times in the array.

**Example**:
- Input: `arr[] = [1, 1, 2, 1, 3, 5, 1]`
- Output: `1` (appears 4 times, > 7/2 = 3)

**Best Solution**: Moore's Voting Algorithm - **O(n) time, O(1) space**
- Find candidate using voting mechanism
- Validate candidate by counting occurrences

---

## 3. Adding One to Number Array

**Problem**: Add 1 to a number represented as an array of digits.

**Example**:
- Input: `arr[] = {9, 9, 9}`
- Output: `{1, 0, 0, 0}`

**Best Solution**: Carry Propagation - **O(n) time, O(1) space**
- Start from rightmost digit
- Handle carry propagation
- Insert new digit if needed

---

## 4. Rearrange Alternating Positive Negative Items

**Problem**: Arrange array in alternating positive and negative fashion maintaining order.

**Example**:
- Input: `arr[] = {-2, 3, 4, -1}`
- Output: `{-2, 3, -1, 4}` (or similar valid arrangement)

**Best Solution**: Partitioning Approach - **O(n) time, O(1) space**
- Partition positive and negative numbers
- Use two-pointer technique for alternating arrangement

---

## 5. Product Array Puzzle

**Problem**: Create array where each element is product of all other elements except itself.

**Example**:
- Input: `arr[] = {10, 3, 5, 6, 2}`
- Output: `{180, 600, 360, 300, 900}`

**Best Solution**: Handle Zero Cases - **O(n) time, O(1) space**
- Count zeros in array
- Calculate product of non-zero elements
- Handle different zero count scenarios

---

## 6. Find Frequency of Elements in Limited Range

**Problem**: Find frequency of each element in sorted array in less than O(n) time.

**Example**:
- Input: `arr[] = {1, 1, 1, 2, 3, 3, 5, 5, 8, 8, 8, 9, 9, 10}`
- Output: Element frequencies for each unique element

**Best Solution**: Binary Search - **O(m log n) time, O(1) space**
- Use binary search to find last occurrence of each element
- Calculate frequency as (last - first + 1)

---

## 7. Factorial of Large Number

**Problem**: Calculate factorial of large numbers that exceed integer limits.

**Example**:
- Input: `100`
- Output: Very large factorial result

**Best Solution**: Linked List Multiplication - **O(n²) time, O(n) space**
- Use linked list to store digits
- Multiply each node with current number and handle carry

---

## 8. Minimum Jumps to Reach End

**Problem**: Find minimum jumps needed to reach end of array where each element represents max jump length.

**Example**:
- Input: `arr[] = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]`
- Output: `3` jumps

**Best Solution**: Greedy Approach - **O(n) time, O(1) space**
- Track maximum reachable position
- Update jumps when current reach is exhausted

---

## 9. Kth Element of Two Sorted Arrays

**Problem**: Find kth element in merged sorted order of two sorted arrays.

**Example**:
- Input: `arr1[] = [2, 3, 6, 7, 9]`, `arr2[] = [1, 4, 8, 10]`, `k = 5`
- Output: `6`

**Best Solution**: Binary Search - **O(log(min(m,n))) time, O(1) space**
- Binary search on smaller array
- Partition both arrays to find kth element

---

## 10. Find Row with Maximum Number of 1s

**Problem**: Find row with maximum 1s in binary matrix where each row is sorted.

**Example**:
- Input: Binary matrix with sorted rows
- Output: Row index with maximum 1s

**Best Solution**: Top-Right Traversal - **O(m + n) time, O(1) space**
- Start from top-right corner
- Move left on 1, move down on 0

---

## 11. Buy and Sell Stock

**Problem**: Find maximum profit from buying and selling stock multiple times.

**Example**:
- Input: `prices[] = [100, 180, 260, 310, 40, 535, 695]`
- Output: `865` (maximum profit)

**Best Solution**: Accumulating Profit - **O(n) time, O(1) space**
- Add profit for every consecutive price increase
- Equivalent to buying at valleys and selling at peaks

---

## 12. Longest Consecutive Subsequence

**Problem**: Find length of longest subsequence of consecutive integers.

**Example**:
- Input: `arr[] = {1, 9, 3, 10, 4, 20, 2}`
- Output: `4` (subsequence: 1, 2, 3, 4)

**Best Solution**: Hash Set - **O(n) time, O(n) space**
- Store all elements in hash set
- For each potential start, count consecutive sequence

---

## 13. Maximum j - i such that arr[i] ≤ arr[j]

**Problem**: Find maximum difference between indices where arr[i] ≤ arr[j] and i ≤ j.

**Example**:
- Input: `arr[] = {34, 8, 10, 3, 2, 80, 30, 33, 1}`
- Output: `6`

**Best Solution**: Precomputed Min-Max Arrays - **O(n) time, O(n) space**
- Precompute left minimums and right maximums
- Use two pointers to find maximum valid difference

---

## 14. Trapping Rain Water

**Problem**: Calculate water trapped between bars in elevation map.

**Example**:
- Input: `arr[] = [3, 0, 1, 0, 4, 0, 2]`
- Output: `10` units of water

**Best Solution**: Two Pointers - **O(n) time, O(1) space**
- Use left and right pointers with left_max and right_max
- Decide water level based on smaller boundary

---

## 15. Triplet Sum Closest to Target

**Problem**: Find triplet sum closest to given target value.

**Example**:
- Input: `arr[] = [-1, 2, 2, 4]`, `target = 4`
- Output: `5` (closest sum to target)

**Best Solution**: Sort + Two Pointers - **O(n²) time, O(1) space**
- Sort array first
- Fix one element, use two pointers for remaining two
- Track closest sum to target

---

## 16. Maximum Sum in Subarray (Kadane's Algorithm)

**Problem**: Find maximum sum among all possible subarrays.

**Example**:
- Input: `arr[] = {-2, -3, 4, -1, -2, 1, 5, -3}`
- Output: `7` (subarray: [4, -1, -2, 1, 5])

**Best Solution**: Kadane's Algorithm - **O(n) time, O(1) space**
- Track maximum ending here and maximum so far
- Extend subarray or start new based on current sum

---

## 17. Merge Two Sorted Arrays

**Problem**: Merge two sorted arrays while maintaining sorted order.

**Example**:
- Input: `arr1[] = {1, 3, 5, 7}`, `arr2[] = {0, 2, 6, 8, 9}`
- Output: Merged sorted array

**Best Solution**: Two Pointers - **O(n + m) time, O(n + m) space**
- Use two pointers to merge elements in sorted order
- Handle remaining elements from both arrays

---

## Key Algorithmic Techniques Used

1. **Two Pointers**: Problems 9, 11, 14, 15, 17
2. **Binary Search**: Problems 6, 9
3. **Greedy Approach**: Problems 8, 11
4. **Hash Set/Map**: Problems 12
5. **Dynamic Programming**: Problems 16 (Kadane's)
6. **Array Manipulation**: Problems 1, 3, 4, 5
7. **Prefix/Suffix Arrays**: Problems 13
8. **Partitioning**: Problems 4, 10

Each solution is optimized for the best time and space complexity while maintaining code clarity and correctness.
