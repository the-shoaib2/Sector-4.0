s = input().strip()
stack = []

k = 0
for char in s:
    if len(stack) == 0:
        stack.append(char)
        continue

    if stack[-1] == char:
        k += 1
        stack.pop()
    else:
        stack.append(char)

if k % 2 == 0:
    print("NO")
else:
    print("YES")
