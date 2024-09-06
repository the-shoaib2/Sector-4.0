# Input
T = int(input())

for t in range(1, T + 1):
    # Read the number of creatures
    N = int(input())

    # Read the speeds of creatures
    creature_speeds = list(map(int, input().split()))

    # Find the maximum speed
    max_speed = max(creature_speeds)

    # Output the result
    print(f"Case {t}: {max_speed}")
