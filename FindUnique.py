#TO FIND THE UNIQUE ELEMENTS FROM THE LIST
list = []
n = int(input('Enter number of elements yoou want to enter: '))
unique_ele = []
for i in range(0, n):
    ele = int(input('enter the element: ' ))
    list.append(ele)

for x in list:
    if x not in unique_ele:
            unique_ele.append(x)
    # print list
    for x in unique_ele:
        print(x)
