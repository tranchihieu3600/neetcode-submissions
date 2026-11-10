## Minimum Window Substring

**Độ khó:** Hard

---

Given two strings `s` and `t` of lengths `m` and `n` respectively, return *the **minimum window*** ***substring**** of *`s`* such that every character in *`t`* (**including duplicates**) is included in the window*. If there is no such substring, return *the empty string *`""`.



The testcases will be generated such that the answer is **unique**.



 


Example 1:**



```

**Input:** s = "ADOBECODEBANC", t = "ABC"
**Output:** "BANC"
**Explanation:** The minimum window substring "BANC" includes &#39;A&#39;, &#39;B&#39;, and &#39;C&#39; from string t.

```


Example 2:**



```

**Input:** s = "a", t = "a"
**Output:** "a"
**Explanation:** The entire string s is the minimum window.

```


Example 3:**



```

**Input:** s = "a", t = "aa"
**Output:** ""
**Explanation:** Both &#39;a&#39;s from t must be included in the window.
Since the largest window of s only has one &#39;a&#39;, return empty string.

```


 


**Constraints:**





	- `m == s.length`

	- `n == t.length`

	- `1 5`

	- `s` and `t` consist of uppercase and lowercase English letters.




 


**Follow up:** Could you find an algorithm that runs in `O(m + n)` time?

---
## Gợi ý (Hints)

<details>
<summary><b>Gợi ý 1</b></summary>

Use two pointers to create a window of letters in s, which would have all the characters from t.

</details>

<details>
<summary><b>Gợi ý 2</b></summary>

Expand the right pointer until all the characters of t are covered.

</details>

<details>
<summary><b>Gợi ý 3</b></summary>

Once all the characters are covered, move the left pointer and ensure that all the characters are still covered to minimize the subarray size.

</details>

<details>
<summary><b>Gợi ý 4</b></summary>

Continue expanding the right and left pointers until you reach the end of s.

</details>

