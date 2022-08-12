n1 = 0
n2 = 1
i = 0;
n = int(input('Numbers of element to be printed in fibonacci: '))
while i <n:
    print(n1)
    next = n1+n2
    n1 = n2
    n2 = next
    i+=1
    
