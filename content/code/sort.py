import time
import random

def sort_numbers(numbers):
    result = []     # 这里记录排列好的序列
    while numbers:  # 一直循环，直到 numbers 为空
        curr_max = -float('inf')    # 记录当前最大的数，因为还没开始，所以是负无穷大
        curr_max_idx = 0            # 记录当前最大的数在第几个
        for idx in range(len(numbers)):  
            if numbers[idx] > curr_max:
                curr_max = numbers[idx] 
                curr_max_idx = idx

        numbers.pop(curr_max_idx)   # 把 numbers 里面最大的那个数扔掉
        result.append(curr_max)     # 把这个最大的数放到 result 数组里面

    return result                   # 返回的 result 就是排列好的数组了

numbers = [random.randint(0, 100000) for _ in range(100000)]

start = time.time()
sort_numbers(list(numbers))
end = time.time()
print("基础版耗时： " + str(end - start))

start = time.time()
list(numbers).sort()
end = time.time()
print("基础版耗时： " + str(end - start))


