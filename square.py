print("pls enter the length of side:")
n = int(input())
a = [[]]*3
for i in range(1, n+1):
    if i == 1 or i == n:
        for j in range(1, n+1):
            print("*", end='')
            print("   ", end='')
    else:

        for j in range(1, n+1):
            if j == 1 or j == n:
                print("*", end='')
                print("   ", end='')
            else:
                print("    ", end='')
    print('\n')