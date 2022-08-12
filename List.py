Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
list1 = [1,2,3,4,5,6,7]
list1
[1, 2, 3, 4, 5, 6, 7]
list1.append(2)
list1
[1, 2, 3, 4, 5, 6, 7, 2]
#append is used for adding any element in the list at the end
list1.count(1)
1
#count is used to count the number of occurance of that element
list1
[1, 2, 3, 4, 5, 6, 7, 2]
list1.clear(2)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    list1.clear(2)
TypeError: list.clear() takes no arguments (1 given)
list1.clear()
list1
[]
list1.append(1,2,3)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    list1.append(1,2,3)
TypeError: list.append() takes exactly one argument (3 given)
list1.append(7)
list1.append(2)

z
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    z
NameError: name 'z' is not defined
list1.append(4)
list1.append(6)
list1.append(5)
list1
[7, 2, 4, 6, 5]
list1.sort()
list1
[2, 4, 5, 6, 7]
list1.reverse()
list1
[7, 6, 5, 4, 2]
list2 = [7,8,9,3,4]
list1.extend(list2)
list1
[7, 6, 5, 4, 2, 7, 8, 9, 3, 4]
#extend is used for concatinating two strings

#now concatinating two lists using new list and + operator
list3 = list1+list2
list3
[7, 6, 5, 4, 2, 7, 8, 9, 3, 4, 7, 8, 9, 3, 4]

#now concatinating two lists using new * operator

list4 = [*list1, *list2]
list4
[7, 6, 5, 4, 2, 7, 8, 9, 3, 4, 7, 8, 9, 3, 4]
[7, 6, 5, 4, 2, 7, 8, 9, 3, 4, 7, 8, 9, 3, 4]
[7, 6, 5, 4, 2, 7, 8, 9, 3, 4, 7, 8, 9, 3, 4]

lista = [3,6,1,2,5,6]
lista.remove(2:5)
SyntaxError: invalid syntax
lista.remove[2:5]
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    lista.remove[2:5]
TypeError: 'builtin_function_or_method' object is not subscriptable
lista[2:4] = []
lista
[3, 6, 5, 6]
#this is the method for removing multiple elements from the list
