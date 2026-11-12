## Score of a String

**Độ khó:** Easy

---

You are given a string `s`. The **score** of a string is defined as the sum of the absolute difference between the **ASCII** values of adjacent characters.



Return the **score** of* *`s`.



 


Example 1:**




**Input:** s = "hello"



**Output:** 13



**Explanation:**



The **ASCII** values of the characters in `s` are: `&#39;h&#39; = 104`, `&#39;e&#39; = 101`, `&#39;l&#39; = 108`, `&#39;o&#39; = 111`. So, the score of `s` would be `|104 - 101| + |101 - 108| + |108 - 108| + |108 - 111| = 3 + 7 + 0 + 3 = 13`.




Example 2:**




**Input:** s = "zaz"



**Output:** 50



**Explanation:**



The **ASCII** values of the characters in `s` are: `&#39;z&#39; = 122`, `&#39;a&#39; = 97`. So, the score of `s` would be `|122 - 97| + |97 - 122| = 25 + 25 = 50`.




 


**Constraints:**





	- `2 <= s.length <= 100`

	- `s` consists only of lowercase English letters.

---
## Gợi ý (Hints)

<details>
<summary><b>Gợi ý 1</b></summary>

Sum the difference between all the adjacent characters by just taking the absolute difference of their ASCII values.

</details>

