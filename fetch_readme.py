import os
import requests
import re

LEETCODE_API_URL = "https://leetcode.com/graphql"

# Danh sách mapping các bài NeetCode 150 bị đổi tên so với slug gốc của LeetCode
MANUAL_MAPPING = {
    "duplicate-integer": "contains-duplicate",
    "is-anagram": "valid-anagram",
    "two-integer-sum": "two-sum",
    "anagram-groups": "group-anagrams",
    "top-k-elements-in-list": "top-k-frequent-elements",
    "string-encode-and-decode": "encode-and-decode-strings",
    "products-of-array-discluding-self": "product-of-array-except-self",
    "is-palindrome": "valid-palindrome",
    "two-integer-sum-ii": "two-sum-ii-input-array-is-sorted",
    "three-integer-sum": "3sum",
    "max-water-container": "container-with-most-water",
    "buy-and-sell-crypto": "best-time-to-buy-and-sell-stock",
    "longest-substring-without-duplicates": "longest-substring-without-repeating-characters",
    "longest-repeating-substring-with-replacement": "longest-repeating-character-replacement",
    "permutation-string": "permutation-in-string",
    "minimum-window-with-characters": "minimum-window-substring",
    "search-2d-matrix": "search-a-2d-matrix",
    "eating-bananas": "koko-eating-bananas",
    "find-target-in-rotated-sorted-array": "search-in-rotated-sorted-array",
    "reverse-a-linked-list": "reverse-linked-list",
    "merge-two-sorted-linked-lists": "merge-two-sorted-lists",
    "linked-list-cycle-detection": "linked-list-cycle",
    "reorder-linked-list": "reorder-list",
    "remove-node-from-end-of-linked-list": "remove-nth-node-from-end-of-list",
    "copy-linked-list-with-random-pointer": "copy-list-with-random-pointer",
    "add-two-numbers": "add-two-numbers",
    "find-duplicate-integer": "find-the-duplicate-number",
    "lru-cache": "lru-cache",
    "merge-k-sorted-linked-lists": "merge-k-sorted-lists",
    "invert-a-binary-tree": "invert-binary-tree",
    "depth-of-binary-tree": "maximum-depth-of-binary-tree",
    "same-binary-tree": "same-tree",
    "subtree-of-a-binary-tree": "subtree-of-another-tree",
    "lowest-common-ancestor-in-binary-search-tree": "lowest-common-ancestor-of-a-binary-search-tree",
    "binary-tree-level-order-traversal": "binary-tree-level-order-traversal",
    "valid-binary-search-tree": "validate-binary-search-tree",
    "kth-smallest-integer-in-bst": "kth-smallest-element-in-a-bst",
    "construct-binary-tree-from-preorder-and-inorder-traversal": "construct-binary-tree-from-preorder-and-inorder-traversal",
    "binary-tree-maximum-path-sum": "binary-tree-maximum-path-sum",
    "serialize-and-deserialize-binary-tree": "serialize-and-deserialize-binary-tree",
    "minimum-stack": "min-stack",
    "validate-parentheses": "valid-parentheses"
}

def clean_html(raw_html):
    """Làm sạch các thẻ HTML cơ bản từ API trả về để README dễ nhìn hơn"""
    clean_text = re.sub(r'<p>', '', raw_html)
    clean_text = re.sub(r'</p>', '\n\n', clean_text)
    clean_text = re.sub(r'<ul>', '\n', clean_text)
    clean_text = re.sub(r'</ul>', '\n', clean_text)
    clean_text = re.sub(r'<li>', '- ', clean_text)
    clean_text = re.sub(r'</li>', '\n', clean_text)
    clean_text = re.sub(r'<pre>', '```\n', clean_text)
    clean_text = re.sub(r'</pre>', '\n```\n', clean_text)
    clean_text = re.sub(r'<code>', '`', clean_text)
    clean_text = re.sub(r'</code>', '`', clean_text)
    clean_text = re.sub(r'<strong>', '**', clean_text)
    clean_text = re.sub(r'</strong>', '**', clean_text)
    clean_text = re.sub(r'<em>', '*', clean_text)
    clean_text = re.sub(r'</em>', '*', clean_text)
    clean_text = re.sub(r'&nbsp;', ' ', clean_text)
    clean_text = re.sub(r'&lt;', '<', clean_text)
    clean_text = re.sub(r'&gt;', '>', clean_text)
    clean_text = re.sub(r'&quot;', '"', clean_text)
    # Loại bỏ các thẻ HTML còn lại
    clean_text = re.sub(r'<[^>]+>', '', clean_text)
    return clean_text.strip()

def get_leetcode_problem(slug):
    query = """
    query questionData($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            questionFrontendId
            title
            content
            difficulty
        }
    }
    """
    variables = {"titleSlug": slug}
    payload = {"query": query, "variables": variables}
    
    try:
        response = requests.post(LEETCODE_API_URL, json=payload)
        if response.status_code == 200:
            data = response.json()
            if "data" in data and data["data"]["question"]:
                return data["data"]["question"]
    except Exception as e:
        print(f"Lỗi khi gọi API cho {slug}: {e}")
    return None

def main():
    for root, dirs, files in os.walk("."):
        if ".git" in root or ".github" in root:
            continue
            
        has_code = any(f.endswith(('.py', '.cpp', '.java', '.js', '.go', '.c')) for f in files)
        readme_path = os.path.join(root, "README.md")
        
        if has_code and not os.path.exists(readme_path):
            folder_name = os.path.basename(root)
            
            slug = MANUAL_MAPPING.get(folder_name, folder_name)
            
            print(f"Đang tải đề bài: {slug}...")
            problem_data = get_leetcode_problem(slug)
            
            if problem_data:
                title = problem_data['title']
                difficulty = problem_data['difficulty']
                raw_content = problem_data['content']
                
                # Format nội dung
                content = clean_html(raw_content) if raw_content else "Không tải được nội dung đề bài."
                
                readme_content = f"## {title}\n\n"
                readme_content += f"**Độ khó:** {difficulty}\n\n"
                readme_content += f"---\n\n"
                readme_content += f"{content}\n"
                
                with open(readme_path, "w", encoding="utf-8") as f:
                    f.write(readme_content)
                print(f"-> Đã tạo thành công {readme_path}")
            else:
                print(f"-> KHÔNG TÌM THẤY bài toán: {slug}. Hãy kiểm tra lại MANUAL_MAPPING.")

if __name__ == "__main__":
    main()