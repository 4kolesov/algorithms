# 71992307
def broken_search(nums, target) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        nums_left = nums[left]
        if nums_left == target:
            return left
        nums_right = nums[right]
        if nums[right] == target:
            return right
        mid = (left + right + 1) // 2
        num_mid = nums[mid]
        if num_mid == target:
            return mid
        if nums_left < num_mid:
            if nums_left < target < num_mid:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if num_mid < target < nums_right:
                left = mid + 1
            else:
                right = mid - 1
    return -1
