## Product of Array Except Self

**Độ khó:** Medium

---

Given an integer array `nums`, return *an array* `answer` *such that* `answer[i]` *is equal to the product of all the elements of* `nums` *except* `nums[i]`.



The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.



You must write an algorithm that runs in `O(n)` time and without using the division operation.



 


Example 1:**


```
**Input:** nums = [1,2,3,4]
**Output:** [24,12,8,6]

```
Example 2:**


```
**Input:** nums = [-1,1,0,-3,3]
**Output:** [0,0,9,0,0]

```

 


**Constraints:**





	- `2 5`

	- `-30 <= nums[i] <= 30`

	- The input is generated such that `answer[i]` is **guaranteed** to fit in a **32-bit** integer.




 


**Follow up:** Can you solve the problem in `O(1)` extra space complexity? (The output array **does not** count as extra space for space complexity analysis.)

---
## Gợi ý (Hints)

<details>
<summary><b>Gợi ý 1</b></summary>

Think how you can efficiently utilize prefix and suffix products to calculate the product of all elements except self for each index. Can you pre-compute the prefix and suffix products in linear time to avoid redundant calculations?

</details>

<details>
<summary><b>Gợi ý 2</b></summary>

Can you minimize additional space usage by reusing memory or modifying the input array to store intermediate results?

</details>

