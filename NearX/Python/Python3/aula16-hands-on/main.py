import copy

lista = [1, 2, 3, 4, ["a", "b"]]

b = copy.deepcopy(lista)

b[4].append(999)


print("lista:", lista)
print("b:", b)
