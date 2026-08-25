class Solution:
    def maxArea(self, heights: List[int]) -> int:
        greatest_area = 0 
        left, right = 0, len(heights) - 1

        while left < right:
            # area = length * height
            area = (right - left) * min(heights[left], heights[right])
            greatest_area = max(area, greatest_area)
            # check left and right indices (move min indice)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return greatest_area