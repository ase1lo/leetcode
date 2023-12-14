# from typing import List


# class Solution:
#     def numSpecial(self, mat: List[List[int]]) -> int:
#         count = 0




# mat = [[1, 0, 0], [0, 0, 1], [1, 0, 0]]
# # mat = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
# indexes = []
# for i in range(len(mat)):
#     for j in range(len(mat[i])):
#         if mat[i][j] == 1:
#             indexes.append([i, j])
# print(indexes)
# count = 0
# for i in range(len(indexes) - 1):
#     for j in range(i, len(indexes)):
#         print(indexes[i], indexes[j])
#         if (indexes[i][0] != indexes[j][0]) or (indexes[i][1] != indexes[j][1]):
#             count += 1

# print(count)