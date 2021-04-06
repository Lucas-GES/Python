#!/usr/bin/env python3

from typing import Dict, List, Union, Set
import abc


class Expr(abc.ABC):
    def __init__(self, filhos: list) -> None:
        super().__init__()
        self._filhos = filhos

    @abc.abstractmethod
    def resolver(self, variaveis: Dict[str, bool]) -> bool:
        pass
    
    @property
    def qtde_variaveis(self) -> int:
        return len(self.variaveis)
    
    @property
    def variaveis(self) -> Set['str']:
        vars = set()
        for filho in self._filhos:
            vars.update(filho.variaveis)

        return vars
    
    @abc.abstractclassmethod
    def __str__(self) -> str:
        pass


class And(Expr):
    def __init__(self, esq: Expr, dir: Expr) -> None:
        super().__init__([esq, dir])
        self._esq = esq
        self._dir = dir
    
    def resolver(self, variaveis: Dict[str, bool]) -> bool:
        return self._esq.resolver(variaveis) and self._dir.resolver(variaveis)
    
    def __str__(self) -> str:
        return f'{self._esq}*{self._dir}'


class Or(Expr):
    def __init__(self, esq: Expr, dir: Expr) -> None:
        super().__init__([esq, dir])
        self._esq = esq
        self._dir = dir
    
    def resolver(self, variaveis: Dict[str, bool]) -> bool:
        return self._esq.resolver(variaveis) or self._dir.resolver(variaveis)
    
    def __str__(self) -> str:
        return f'({self._esq}+{self._dir})'


class Not(Expr):
    def __init__(self, expr: Expr) -> None:
        super().__init__([expr])
        self._expr = expr
    
    def resolver(self, variaveis: Dict[str, bool]) -> bool:
        return not self._expr.resolver(variaveis)
    
    def __str__(self) -> str:
        return f'!({self._expr})'


class Variavel(Expr):
    def __init__(self, var: str) -> None:
        super().__init__(list())
        self._var = var
    
    def resolver(self, variaveis: Dict[str, bool]) -> bool:
        return variaveis[self._var]
    
    @property
    def variaveis(self) -> Set['str']:
        return {self._var}
    
    def __str__(self) -> str:
        return self._var


class Literal(Expr):
    def __init__(self, literal: bool) -> None:
        super().__init__(list())
        self._literal = literal
    
    def resolver(self, variaveis: Dict[str, bool]) -> bool:
        return self._literal
    
    @property
    def variaveis(self) -> Set['str']:
        return set()
    
    def __str__(self) -> str:
        return str(self._literal)


def existe_solucao_para(expr: Expr, solucao: bool) -> bool:
    return _existe_solucao_para(expr, [], solucao)


def _existe_solucao_para(expr: Expr, valor_variaveis: list, solucao: bool) -> bool:
    # Caso base
    if len(valor_variaveis) == expr.qtde_variaveis:
        mapa_variaveis = {var: valor for var, valor in zip(expr.variaveis, valor_variaveis)}
        resultado = expr.resolver(mapa_variaveis)
        print(mapa_variaveis, resultado)

        return resultado == solucao

    # Caso recursivo
    else:
        vars_aumentada_true = valor_variaveis + [True]
        vars_aumentada_false = valor_variaveis + [False]
        return True if _existe_solucao_para(expr, vars_aumentada_true, solucao) \
            else _existe_solucao_para(expr, vars_aumentada_false, solucao)


# if __name__ == '__main__':
#     expressao = ExpressaoBooleana('a*b+c*a')
#     resultado_buscado = False
#     if existe_solucao_para(expressao, resultado_buscado):
#         print (f'A expressão booleana {expressao} possui solução para {resultado_buscado}.')
#     else:
#         print (f'A expressão booleana {expressao} não possui solução para {resultado_buscado}.')
