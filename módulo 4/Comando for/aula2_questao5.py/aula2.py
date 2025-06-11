N = int(input())
M = int(input())
print(" ", end=" ")
for col in range(1, M + 1):
    print(col, end=" ")
print()
for linha in range(1, N + 1):
    print(linha, end=" ")
    for col in range(M):
        print("/", end=" ")
    print()
