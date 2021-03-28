a = int(input())
list1 = set(list(map(int, input().split())))
n = int(input())

for i in range(n):
    command = input().split()
    first = command[0]
    second = int(command[1])

    if first == 'intersection_update':
       parameter = set(list(map(int, input().split()))) 
       list1.intersection_update(parameter)
       
    elif first == 'update':
        parameter = set(list(map(int, input().split())))
        list1.update(parameter)
        
    elif first == 'symmetric_difference_update':
        parameter = set(list(map(int, input().split())))
        list1.symmetric_difference_update(parameter)
        
    elif first == 'difference_update':
        parameter = set(list(map(int, input().split())))
        list1.difference_update(parameter)
        

print(sum(list1))