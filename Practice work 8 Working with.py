#1.1
print("1.")
n = int(input("N: "))
arr = [[int(input()) for j in range(n)] for i in range(n)]
print("List: ", arr)
count = 0
s = 0
for i in range(len(arr) - 1):
    for j in range(i + 1, len(arr[i])):
        if arr[i][j] > 0:
            s += arr[i][j]
            count += 1
print("Sum of positive elements: ", s)
print("Number of positive elements: ", count)

#1.2
N = int(input("N: "))
B = [[int(input()) for j in range(N)] for i in range(N)]
for i in B:
    for j in i:
        print(j, end = " ")
    print()
for i, row in enumerate(B):
    max = min = 0
    for j, elem in enumerate(row):
        if elem > row[max]:
            max = j
        if elem < row[min]:
            min = j
    row[max], row[0] = row[0], row[max]
    row[min], row[-1] = row[-1], row[min]
print(B)
print("\n")



#2.1
print("2.")
n = int(input("N: "))
arr = [[int(input()) for j in range(n)] for i in range(n)]
s = 0
for i in range(n):
    s += arr[0][i]

b = "YES"
for i in range(n):
    s1 = 0
    s2 = 0
    for j in range(n):
        s1 += arr[i][j]
        s2 += arr[j][i]
    if s1 != s or s2 != s:
        b = "NO"
        break
print(b)

#2.2
N = 3
M = 4
A = [[4, 2, 1, 9],[4, 6, 1, 8],[7, 5, 10, 3]]
print("Rectangular matrix: ")
for i in A:
    for j in i:
        print(j, end=" ")
    print()
print()

for i in range(N):
    tmp = A[i][0]
    A[i][0] = A[i][M-1]
    A[i][M-1] = tmp

for i in range(N):
    for j in range(M):
        print("%2d " % A[i][j], end='')
    print()
print("\n")



#3.1
print("3.")
N = int(input("N: "))
A = [[int(input()) for j in range(n)] for i in range(n)]
b = "YES"
for i in range(N):
    for j in range(N):
        if A[i][j] != A[j][i]:
            b = "NO"
            break
print(b)

#3.2
from random import randint
a = [[randint(10, 99) for i in range(9)] for j in range(7)]
for row in a:
    print(*map('{:2d}'.format, row))
print()
max_elem = a[0][0]
ie = je = 0
for i in range(len(a)):
    for j in range(len(a[0])):
        if a[i][j] > max_elem:
            max_elem = a[i][j]
            ie = i 
            je = j 
a[0], a[ie] = a[ie], a[0]
a[0][0], a[0][je] = a[0][je], a[0][0]
for row in a:
    print(*map('{:2d}'.format, row))
print("\n")



#4.2
print("4.")
a = [[1,2,-3],[-1,2,3],[1,-2,3]]
for i in a:
    for j in i:
        print(j, end=" ")
    print()
print()
a = [[1 if x>0 else 0 for x in i] for i in a]
for i in range(len(a)):
    print(*[a[i][x] if x<=i else '' for x in range(len(a[i]))],'')
print("\n")



#5.1
print("5.")
n=int(input("Enter size: "))
m=int(input("Enter size 2: "))
a= [[int(input()) for j in range(n)] for i in range(n)]
print(list(map(sorted, a)))

def qsort(a): 
    if len(a) <= 1:
        return a
    else:
        return qsort( [x for x in a[1:] if x < a[0]]) + [a[0]] + qsort([x for x in a[1:] if x >= a[0]] )
qsort(a)
print("\n")



#6.1
import random
n=int(input("Enter n: "))
m=n
a=[[random.randrange(10) for i in range(n)] for j in range(m)]
for i in a:
    for j in i:
        print(j, end=" ")
    print()
print()

for i in range(n):
    print(a[i],max(a[i]))
for i in range(m):  
    x=[x[i] for x in a]
    print(min(x), end=" ")

#6.2
import random
n = int(input("Enter n: "))
arr=[[random.randrange(10) for i in range(n)] for j in range(n)]
for i in arr:
    print(i)
print()
 
a = sum(arr, [])
max1 = max(a[::n+1])
max2 = max(a[n-1::n-1][:n])
if max1 > max2:
    i1 = j1 = a[::n+1].index(max1)
else:
    i1 = a[n-1::n-1][:n].index(max2)
    j1 = n - 1 - i1
arr[n//2][n//2], arr[i1][j1] = arr[i1][j1], arr[n//2][n//2]
 
for i in arr:
    print(i)
print("\n")



#8.1
print("8.")
n = int(input('Enter the n: '))

k = int(input('Enter the k: '))

arr = [[int(input()) for j in range(n)] for i in range(n)]

for i in range(n):

   for j in range(n):

       if k == i:

           arr[i][j] = arr[i][j] / arr[i][i]

print('\n'.join([''.join([str(f'{i:4}') for i in row]) for row in arr]))

#8.2
n = int(input('Enter the n: '))

arr = [[int(input()) for j in range(n)] for i in range(n)]

print('\n'.join([''.join([str(f'{i:4}') for i in row]) for row in arr]))

arr = list(zip(*arr))

print('\n'.join([''.join([str(f'{i:4}') for i in row]) for row in arr]))
print("\n")



#12.1
print("12.")
arr = [[1, 2, 3, -4], [2, -3, -1, -8], [3, -1, 7, 7], [-4, -8, 2, -8]]
for i in arr :
    print(*map('{:2d}'.format, i))
print()
n = 4
arr_rev = list(map(list,zip(*arr)))
for i in range(n) :
    for j in range(n) :
        if arr[i] == arr_rev[j] :
            print(i+1, 'raw and ', j+1, 'column is equal')

#12.2
m = [[2, 3, 4, 5, 3],
     [7, 7, 7, 7, 7],
     [3, 2, 3, 2, 3],
     [6, 6, 6, 6, 6],
     [1, 1, 1, 1, 1], ]
 
for i in range(len(m) - 1):
    for j in range(len(m[0])):
        m[i][j] -= m[-1][j]
 
for i in m:
    print(*i)
print("\n")



#13.1
print("13.")
import random
 
N = int(input('enter the number:'))
M = int(input('enter the number:'))
B = [[random.randrange(10) for i in range(M)] for j in range(N)]
 
for i in B:
    print(*map('{:3}'.format, i))
 
for i in range(0, N): 
    k = min(B[i])
    print('The minimum of the row %d is %d' % (i+1, k))

#13.2
n = int(input("Enter n: "))
m = int(input("Enter m: "))
a = []
 
for i in range(n):
    a.append(list(map(int, input().split())))
 
max1 = max(max(a))
ind_max1 = a.index(max(a))
ind_max2 = a[ind_max1].index(max1)
 
min1 = min(min(a))
ind_min1 = a.index(min(a))
ind_min2 = a[ind_min1].index(min1)
 
a[ind_min1][ind_min2], a[ind_max1][ind_max2] = max1, min1
 
for i in a:
    print(*i)
print("\n")



#14.1
print("14.")
from random import randint 
m = 3
l = [[randint(-10, 10) for j in range(5)] for i in range(5)]
print(*l, sep='\n')
print()
ll = []
for i in range(len(l)):
    ll.append(l[i][i])
maxid = ll.index(max(ll))
l[maxid], l[m] = l[m], l[maxid]
print(*l, sep='\n')

































    
