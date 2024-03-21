# Litu Ahamed Nirob(221-33-1534)
n = int(input("Enter the size of the array: "))
li = []
sum = 0
for i in range(n):
    a = int(input("Enter the elements of the array: "))
    li.append(a)
max_element = li[0]
min_element = li[0]

for element in li:
    if element > max_element:
        max_element = element
    if element < min_element:
        min_element = element

print("Maximum element in the array:", max_element)
print("Minimum element in the array:", min_element)
