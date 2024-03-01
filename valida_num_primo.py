def valida_primo(x) -> bool:
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
print(valida_primo(1))