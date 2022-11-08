def solution(nums):
    select = len(nums) // 2
    no_repeat = len(set(nums))

    if select < no_repeat:
        return select
    else:
        return no_repeat
