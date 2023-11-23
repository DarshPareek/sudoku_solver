import pandas as pd
import numpy as np
data = pd.read_csv('sudoku.csv')
# for i in range(len(X_s)):
#     X_s[i] = np.array(list(X_s[i]),'int').reshape((-1, 9, 9, 1))
#     Y_s[i] = np.array(list(Y_s[i]),'int').reshape((-1, 9, 9))
X_s = np.array(data.quizzes.map(lambda x: list(map(int, x))).to_list()).reshape(-1,9,9,1)
Y_s = np.array(data.solutions.map(lambda x: list(map(int, x))).to_list()).reshape(-1,9,9)