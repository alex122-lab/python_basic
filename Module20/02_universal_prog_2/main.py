def is_prime(n):
    if n < 2 or n % 2 == 0:
        return n == 2
    else:
        d = 3
        while n % d != 0:
            d += 1
        return d == n

def crypto(symbols):
    prime_indexes = []
    for i, sym in enumerate(symbols):
        if is_prime(i):
            prime_indexes.append(sym)
    return prime_indexes

def crypto_return(symbols):
    return [sym for i, sym in enumerate(symbols) if is_prime(i)]

print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(crypto('О Дивный Новый мир!'))

print(crypto_return([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(crypto_return('О Дивный Новый мир!'))


