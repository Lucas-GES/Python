def memoize(f):  # -> Function
    """Retorna uma funcao f qualquer, memoizada."""
    memo = dict()

    def call_f(*args):
        if args in memo:
            return memo[args]
        else:
            result = f(*args)
            memo[args] = result
            return result
    
    return call_f


def log_debug(f):
    def call_f(*args):
        print(f'Entrando em {f} com {args}.')
        resultado = f(*args)
        print(f'Saindo de {f} com resultado {resultado}.')
        return resultado
    
    return call_f


# Explicação sobre closures.
def funcao_fora(n: int): #-> Function:
    alpha = .5 * n

    def funcao_dentro(g: int) -> float:
        return alpha/g  # Closure
    
    return funcao_dentro
