def add(*args):
    soma = 0
    for num in args:
        soma += num
    return soma


total = add(10, 20, 50, 99999, 85, 32)
print(total)
