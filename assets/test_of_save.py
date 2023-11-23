import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
import pandas as pd
import numpy as np
from data_gen import X_s, Y_s
from tensorflow import keras
from keras import layers

model = keras.models.load_model('saved_model/')

X = '060720908084003001700100065900008000071060000002010034000200706030049800215000090'
Y = '163725948584693271729184365946358127371462589852917634498231756637549812215876493'

X = np.array(pd.Series(X).map(lambda x: list(map(int, x))).to_list()).reshape(-1,9,9,1)
Y = np.array(pd.Series(Y).map(lambda x: list(map(int, x))).to_list()).reshape(-1,9,9,1)

X = X/9
X -= 0.5
Y -= 1

# print(X.reshape(9,9))
y = model.predict(X).argmax(-1)+1
ans = y[0]
res = ''
for i in ans:
    res += "".join(str(x) for x in i)
print(res)