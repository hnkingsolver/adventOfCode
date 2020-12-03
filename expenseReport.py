# # def missingExpense(numbers):
# #     sum = 2020
    
# #     for i in range(len(numbers) - 1):
# #         for j in range(i + 1, len(numbers)):
# #             if numbers[i] + numbers[j] == sum:
# #                 return(numbers[i], numbers[j])
    
# # print(missingExpense(numbers))

# def twoSumNaive(num_arr, pair_sum):
#       # search first element in the array
#   for i in range(len(num_arr) - 1):
#     # search other element in the array
#     for j in range(i + 1, len(num_arr)):
#       # if these two elemets sum to pair_sum, print the pair
#       if num_arr[i] + num_arr[j] == pair_sum:
#           print(num_arr[i] * num_arr[j])

      

# # Driver Code
# num_arr = []

# # converting .txt to list
# numbers_file = open('input.txt', 'r')
# lines = numbers_file.read().split('\n')
# num_arr.append(lines)
# # num_arr = [3, 5, 2, -4, 8, 11, 1, 2019]
# pair_sum = 2020

# # Function call inside print
# twoSumNaive(num_arr, pair_sum) 

from functools import reduce

numbers = [int(x) for x in open('input.txt').read().split('\n')]
print(reduce(lambda x, y: x * y, list(filter(lambda x: 2020 - x in set(numbers), numbers))))
