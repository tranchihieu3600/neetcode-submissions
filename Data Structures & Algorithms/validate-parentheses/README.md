## Valid Parentheses

**Độ khó:** Easy

---

Given a string `s` containing just the characters `&#39;(&#39;`, `&#39;)&#39;`, `&#39;{&#39;`, `&#39;}&#39;`, `&#39;[&#39;` and `&#39;]&#39;`, determine if the input string is valid.



An input string is valid if:




	- Open brackets must be closed by the same type of brackets.

	- Open brackets must be closed in the correct order.

	- Every close bracket has a corresponding open bracket of the same type.



 


Example 1:**




**Input:** s = "()"



**Output:** true




Example 2:**




**Input:** s = "()[]{}"



**Output:** true




Example 3:**




**Input:** s = "(]"



**Output:** false




Example 4:**




**Input:** s = "([])"



**Output:** true




Example 5:**




**Input:** s = "([)]"



**Output:** false




 


**Constraints:**





	- `1 4`

	- `s` consists of parentheses only `&#39;()[]{}&#39;`.

---
## Gợi ý (Hints)

<details>
<summary><b>Gợi ý 1</b></summary>

Use a stack of characters.

</details>

<details>
<summary><b>Gợi ý 2</b></summary>

When you encounter an opening bracket, push it to the top of the stack.

</details>

<details>
<summary><b>Gợi ý 3</b></summary>

When you encounter a closing bracket, check if the top of the stack was the opening for it. If yes, pop it from the stack. Otherwise, return false.

</details>

