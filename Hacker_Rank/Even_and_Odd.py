print("Write the number to be analize: ")
n = int(input().strip())
if n % 2 == 0 :
    if n >= 2 and n < 5 :
        print("Not Weird")        
    elif n >= 6 and n <= 20 :
        print("Weird")
    elif n > 20 :
        print("Not Weird")
if n % 2 == 1 :
    print("Weird")             