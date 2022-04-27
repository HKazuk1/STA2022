# オプション1

def prime_checker(n):
    if n == 1: return False
    for i in range(2,int(n ** 0.5) + 1):
        if n%i == 0:
            return n
    return "Prime"

for i in range(30, 61):
    print(prime_checker(i))
