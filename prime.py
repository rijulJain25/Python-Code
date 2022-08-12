#prime numbers between a and b
a = int(input('Enter the lower value: '))
b = int(input('Enter the upper value: '))
i = a;
for number in range (a, b+1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number)  

    
            
    
