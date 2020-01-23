x = 1
y = 1
X1 = 3
X2 = 4
B = -10
bias = 1
cnt = 0
update = 0.1
ans = (X1 * x) + (X2 * y) + (B + (bias*update))
while(ans < 0):
    cnt += 1
    X1 = X1 + update*x
    X2 = X2 + update*y
    B = B + update*bias
    
    ans = (X1 * x) + (X2 * y) + (B + (bias*update))
    print("X1 = " + str(X1))
    print("X2 = " + str(X2))
    print("B = " + str(B))
    print(cnt)
    print(":::::")
    print(ans)
    print("**************")

print(cnt)
print(ans)
