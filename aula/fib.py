def fib_list(n):
    v0, v1 = 0, 1
    fibs = list()
    for _ in range(n):
        fibs.append(v0)
        v0, v1 = v1, v0+v1

    return fibs

def fib_gen(n):
    v0, v1 = 0, 1
    for _ in range(n):
        yield v0
        v0, v1 = v1, v0+v1

def fib_index(i):
    assert i >= 0, 'Não existe fib negativo.'

    ultimo_fib = 0
    for fib in fib_gen(i):
        ultimo_fib = fib
    return ultimo_fib

def fib(i):
    assert i >= 0, 'Não pode haver elemento de indice negativo em uma sequência.'

    if i in (0,1):
        return i
    else:
        return fib(i-2) + fib(i-1)    

is_teste = False
if is_teste:
    fibs_recursivo = ['Recursivo'] + [fib(n) for n in range(10)]
    fibs_sequencial = ['Sequencial'] + [fib_index(n) for n in range(10)]
    zero_a_nove = ['Indice'] + list(range(10))
    for zipado in zip(zero_a_nove, fibs_recursivo, fibs_sequencial):
        print(zipado)
