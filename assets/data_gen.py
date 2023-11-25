import pandas as pd
import numpy as np
data = pd.read_csv('sudoku.csv', chunksize=20)

# def gen_data():
#     for d in data:
#         X_s = np.array(d.puzzle.map(lambda x: list(map(int, x))).to_list()).reshape(-1,9,9,1)
#         Y_s = np.array(d.solution.map(lambda x: list(map(int, x))).to_list()).reshape(-1,9,9)
#         X_s = X_s / 9
#         X_s -= 0.5
#         Y_s -= 1
#         yield (X_s, Y_s)

# s = 0
# dd = gen_data()
# t = next(dd)
# # print((t[0].shape)[0])
# for i in dd:
#     s = s+(i[0].shape)[0]
# print(s)
# n =[]
# for i in data:
#     n.append(i.shape)
# for i in range(len(X_s)):
#     X_s[i] = np.array(list(X_s[i]),'int').reshape((-1, 9, 9, 1))
#     Y_s[i] = np.array(list(Y_s[i]),'int').reshape((-1, 9, 9))
# X_s = np.array(data.puzzle.map(lambda x: list(map(int, x))).to_list()).reshape(-1,9,9,1)
# Y_s = np.array(data.solution.map(lambda x: list(map(int, x))).to_list()).reshape(-1,9,9)