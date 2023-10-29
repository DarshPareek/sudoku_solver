# %%
import csv

# %%
file = open('sudoku.csv', 'r')

# %%
r = csv.reader(file)

# %%
rows = []
for i in r:
    rows.append(i)
rows.pop(0)

# %%
train_set = rows[:500000]
# print(len(train_set))
cv_set = rows[500000:750000]
# print(len(cv_set))
test_set = rows[750000:1000000]
# print(len(test_set))

# %%
train_x, train_y = [], []
for i in train_set:
    train_x.append(i[0])
    train_y.append(i[1])
cv_x, cv_y = [], []
for i in cv_set:
    cv_x.append(i[0])
    cv_y.append(i[1])
test_x, test_y = [], []
for i in test_set:
    test_x.append(i[0])
    test_y.append(i[1])
# print(train_x[:1])
# print(train_y[:1])
