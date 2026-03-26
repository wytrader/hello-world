"""Simple sorting program using merge sort."""

from typing import List


def merge_sort(nums: List[int]) -> List[int]:
    """Return a new sorted list in ascending order."""
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    return _merge(left, right)


def _merge(left: List[int], right: List[int]) -> List[int]:
    merged: List[int] = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def main() -> None:
    raw = input("请输入一串整数（用空格分隔）：\n").strip()
    nums = [int(x) for x in raw.split()] if raw else []
    print("排序结果：", merge_sort(nums))


if __name__ == "__main__":
    main()
