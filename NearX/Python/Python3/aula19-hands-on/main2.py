import copy

original = {"a": 1, "b": [2, 3]}


novo = original.copy()

novo["cidade"] = "São Paulo"
novo["b"][0] = 999

print(original)