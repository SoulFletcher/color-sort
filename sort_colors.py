import collections


def sort_colors(nums) -> None:
    """
    nums - is a list with 3 distinct chars
    sorts nums in place
    using bucket sort
    """
    if len(nums) == 1:
        return
    a = collections.Counter(nums)
    l = r = 0
    for i in range(3):
        r += a[i]
        nums[l:r] = [i] * a[i]
        l += a[i]
