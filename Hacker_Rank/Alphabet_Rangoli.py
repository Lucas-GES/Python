import string

def print_rangoli(size):    
    alpha = string.ascii_lowercase

    for i in range(size-1,-size,-1):    
        row = ['-']*(4*size-3)
        for j in range(0,size-abs(i)):    
            row[2*(size-1+j)] = alpha[abs(i)+j]
            row[2*(size-1-j)] = alpha[abs(i)+j]
        print(''.join(row))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)