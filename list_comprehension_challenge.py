
# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
    
# x=1
# y=1
# z=1
# n=2
# 
# 
# comp = [(i, j, k) for i in range(x + 1) for j in range(y + 1) for k in range(z + 1)]
# final = [for
x, y, z = 1, 1, 1  # Example dimensions
n=2
result = [(i, j, k) for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
print(result)