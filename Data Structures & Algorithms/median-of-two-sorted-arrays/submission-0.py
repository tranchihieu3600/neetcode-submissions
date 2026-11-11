class Solution:

    def findMedianSortedArrays(
        self, nums1: list[int], nums2: list[int]
    ) -> float:
        # Đảm bảo nums1 là mảng có kích thước nhỏ hơn để tìm kiếm nhị phân tối ưu O(log(min(m, n)))
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left, right = 0, m
        half_len = (m + n + 1) // 2

        while left <= right:
            i = (left + right) // 2  # Số phần tử lấy từ nums1 cho nửa bên trái
            j = half_len - i  # Số phần tử lấy từ nums2 cho nửa bên trái

            # Xác định các biên giới hạn (nếu vượt quá mảng thì lấy vô cực âm/dương)
            nums1_left_max = nums1[i - 1] if i > 0 else float("-inf")
            nums1_right_min = nums1[i] if i < m else float("inf")

            nums2_left_max = nums2[j - 1] if j > 0 else float("-inf")
            nums2_right_min = nums2[j] if j < n else float("inf")

            # Kiểm tra xem đã tìm đúng vách ngăn chưa
            if (
                nums1_left_max <= nums2_right_min
                and nums2_left_max <= nums1_right_min
            ):
                # Nếu tổng số phần tử là lẻ -> trung vị là số lớn nhất ở nửa bên trái
                if (m + n) % 2 == 1:
                    return float(max(nums1_left_max, nums2_left_max))
                # Nếu tổng số phần tử là chẵn -> trung vị là trung bình cộng của 2 phần tử ở giữa
                return (
                    max(nums1_left_max, nums2_left_max)
                    + min(nums1_right_min, nums2_right_min)
                ) / 2.0
            elif nums1_left_max > nums2_right_min:
                # Phần tử bên trái của nums1 quá lớn, cần dịch chuyển vách ngăn sang trái
                right = i - 1
            else:
                # Phần tử bên trái của nums2 quá lớn, cần dịch chuyển vách ngăn sang phải
                left = i + 1

        return 0.0