tab = [5, 3, 6, 10, 9, 7, 1, 2, 4, 8]

n=len(tab)
for i in range(n):
    for j in range(i+1,n):
        print(i,j)
