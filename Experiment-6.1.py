# Litu Ahamed Nirob(221-33-1534)
n = int(input("Enter the size of the array: "))
li = []
sum = 0
for i in range(n):
    a = int(input("Enter the elements of the array: "))
    li.append(a)
for i in li:
    sum = sum + i
print("The sum of the elements of the array is:", sum)
