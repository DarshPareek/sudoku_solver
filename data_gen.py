import pandas as pd
import numpy as np
data = pd.read_csv('sudoku.csv')
X_s = np.array(data['quizzes'])
Y_s = np.array(data['solutions'])
for i in range(len(X_s)):
    X_s[i] = np.array(list(X_s[i]),'int32').reshape(9,9)
    Y_s[i] = np.array(list(Y_s[i]),'int32').reshape(9,9)