x = 0
y = 1
soma = x + y
troca: int

for i in range(1,11):
    soma = x + y
    print(f"{x} + {y} = {soma}")

    x = y
    y = soma


