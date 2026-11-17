# def one_loop(nums):
#     steps = 0
#     for n in nums:
#         steps += 1
#     return steps

# def loop_in_loop(nums):
#     steps = 0
#     for a in nums:
#         for b in nums:
#             steps += 1
#     return steps

# small = list(range(10))     # 10 numbers
# big = list(range(100))      # 100 numbers

# print("one loop, 10 items:", one_loop(small))
# print("one loop, 100 items:", one_loop(big))
# print("loop in loop, 10 items:", loop_in_loop(small))
# print("loop in loop, 100 items:", loop_in_loop(big))
import time

big_list = list(range(10_000_000))
big_set = set(big_list)

start = time.time()
print(9_999_999 in big_list)
print("list time:", time.time() - start)

start = time.time()
print(9_999_999 in big_set)
print("set time:", time.time() - start)