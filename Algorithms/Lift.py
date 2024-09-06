def lift(a, b):
    if a <= b:
        return b * 4 + 19
    else:
        return (2 * a - b) * 4 + 19

n = int(input())
for c in range(1, n + 1):
    a, b = map(int, input().split())
    res = lift(a, b)
    print(f"Case {c}: {res}")