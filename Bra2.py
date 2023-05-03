data_list = [3, 5, 13, 4, 9, 20, 100]
data_list = sorted(data_list)
print(data_list)
#print([i for i in data_list if i%2==0])
three_dl = []
for j in data_list:
    if j%3==0:
        three_dl.append(j)
print(three_dl)
