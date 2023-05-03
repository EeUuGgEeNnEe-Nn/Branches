data_list = [3, 5, 13, 4, 9, 20, 100]
print([i for i in data_list if i%2==0])
new_dl = sorted([i for i in data_list if i%2==0 or i%3==0], reverse=True)
print(new_dl)