def gerador_pares(numero: int) -> int:
    for par in range(0, numero, 2):
        yield par
                
par = gerador_pares(7)

print(next(par))
print(next(par))
print(next(par))
print(next(par))
print(next(par))