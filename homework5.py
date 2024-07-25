immutable_var = (1, 2, 3, 'string', 5.5, True)
print('Immutable tuple: ',immutable_var)
immutable_var[0] = 2
print(immutable_var) #TypeError: 'tuple' object does not support item assignment - элемент кортежа не изменяется!

mutable_list = [1, 2, 3, 'string', 5.5, True]
mutable_list[0] = 2
print('Mutable list: ', mutable_list)