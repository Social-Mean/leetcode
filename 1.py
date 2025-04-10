from checker import Checker


def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []


if __name__ == "__main__":
    checker = Checker(__file__)
    checker.check(two_sum)
