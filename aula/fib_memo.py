from decorator import log_debug, memoize

class FibMemorizado:
    def __init__(self) -> None:
        self.memo = dict() # Hashmap

    def fib(self, i):
        if i in self.memo:
            return self.memo[i]
        elif i in (0, 1):
            self.memo[i] = i
            return i
        else:
            resultado = self.fib(i-1) + self.fib(i-2)
            self.memo[i] = resultado
            return resultado

@log_debug
@memoize   # Notação decorator
def fib(i):
    assert i >= 0, 'Não pode haver elemento de índice negativo em uma sequência.'
    
    if i in (0, 1):  # 1 
        return i   # 1
    else:
        return fib(i-2) + fib(i-1)  # 1


if __name__ == "__main__":
    fib_memo = FibMemoizado()
    print(fib_memo.fib(7))
