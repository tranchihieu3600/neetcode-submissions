## Permutation in String

**Độ khó:** Medium

---

Given two strings `s1` and `s2`, return `true` if `s2` contains a permutation of `s1`, or `false` otherwise.



In other words, return `true` if one of `s1`&#39;s permutations is the substring of `s2`.



 


Example 1:**



```

**Input:** s1 = "ab", s2 = "eidbaooo"
**Output:** true
**Explanation:** s2 contains one permutation of s1 ("ba").

```


Example 2:**



```

**Input:** s1 = "ab", s2 = "eidboaoo"
**Output:** false

```


 


**Constraints:**





	- `1 4`

	- `s1` and `s2` consist of lowercase English letters.

---
## Gợi ý (Hints)

<details>
<summary><b>Gợi ý 1</b></summary>

Obviously, brute force will result in TLE. Think of something else.

</details>

<details>
<summary><b>Gợi ý 2</b></summary>

How will you check whether one string is a permutation of another string?

</details>

<details>
<summary><b>Gợi ý 3</b></summary>

One way is to sort the string and then compare. But, Is there a better way?

</details>

<details>
<summary><b>Gợi ý 4</b></summary>

If one string is a permutation of another string then they must have one common metric. What is that?

</details>

<details>
<summary><b>Gợi ý 5</b></summary>

Both strings must have same character frequencies, if  one is permutation of another. Which data structure should be used to store frequencies?

</details>

<details>
<summary><b>Gợi ý 6</b></summary>

What about hash table?  An array of size 26?

</details>

