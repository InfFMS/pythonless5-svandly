# Заполните список длины N случайными числами в диапазоне от 0 до 1000
# Выведите:
# 1.длину списка;
# 2.последний элемент списка;
# 3.список в обратном порядке (вспоминаем срезы);
# 4.YES, если список содержит трехзначное число, состоящее из одинаковых цифр
# NO в противном случае;
# 5.список с удаленными первым и последним элементами.
from random import randint
N = int(input())
A = [randint(0, 1000) for _ in range(N)]
print (len(A))
print (A)
print (A[-1])
l1= A[::-1]
l2 = A[1:N-1:]
i = 0
j = False
while i < N:
    if A[i] == 111 or A[i] == 222 or A[i] == 333 or A[i] == 444 or A[i] == 555 or A[i] == 666 or A[i] == 777 or A[i] == 888 or A[i] == 999:
        j = True
    i += 1
if j == True:
    print("YES")
else:
    print("NO")
print (l1)
print (l2)