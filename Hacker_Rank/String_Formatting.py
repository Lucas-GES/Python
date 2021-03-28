def print_formatted(number):
    nd = bin(number).__len__()
    
    for i in range(1, number+1):

        line = str()
        dec = str(i)
        octal = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        binario = bin(i)[2:]
        nums = [octal, hexa, binario]
        spaces = nd - dec.__len__() - 2
        
        for j in range(spaces):
            line = line.__add__(' ')
        line = line.__add__(dec)

        for num in nums:
            spaces = nd - num.__len__() - 1
            for j in range(spaces):
                line = line.__add__(' ')
            line = line.__add__(num)
        print(line)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)