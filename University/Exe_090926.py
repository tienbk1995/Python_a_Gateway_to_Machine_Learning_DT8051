
#Exe 1
# str_1 = input("Enter the first string: ")
# str_2 = input("Enter the second string: ")
def is_in(str_1, str_2):
    for i in str_1:
        if i in str_2:
            return True
    for j in str_2:
        if j in str_1:
            return True
    return False
#print(is_in(str_1, str_2))

#Exe 2
#print(sum((1,2,3,4,5))/len((1,2,3,4,5)))

#Exe 3
# l = [1, 2, 3]
# l.append(l)
# for i in l:
#     print(i)
# print(l is l[-1])



# a = 1
# b = 2

# def swap(a, b):
#     global x, y
#     x = b
#     y = a
#     return b, a
# a, b = swap(a, b)
# print(a,b)

list_comprehension  = []
for i in range(2,101):
    for j in range(2, i):
        if i % j == 0:
            list_comprehension.append(i)
            break
print(list_comprehension)