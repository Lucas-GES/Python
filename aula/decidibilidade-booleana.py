        # expr = self._expr
        # #for variavel in variaveis:
        # #   expr = expr.replace(variaveis, variaveis[variavel])

        # while True:
        #     esq, op, dir = expr.partition('*')
        #     if op == '':
        #         break

        #     result = variaveis(esq[-1]) and variaveis(dir[0])
        #     expr = esq[:-1] + str(result) + dir[1:]

class EspressaoBoleana():
    def __init__(self, expr_str: str) -> None:
        self._expr = expr_str.strip()
    
    def resolver(self, valor_variaveis: Dict[str, bool]) -> bool:
        """Resolve esta expressão booleana. Por enquanto, apenas `*` e `+`."""
        pass

    @property
    def qtde_variaveis(self) -> int:
        pass
    
    @property
    def lista_variaveis(self) -> List[str]:
        pass
    
def existe_solucao_para(expr: ExpressaoBooleana, valor_variaveis: list, solucao: bool) -> bool:
    if len(valor_variaveis) != expr.qtde_variaveis:
        mapa_variaveis = {var: valor for var}
    else:
        vars_aumentada_true = valor_variaveis + [True]
        vars_aumentada_false = valor_variaveis + [False]
        return

if __name__ == '__main__':
    expressao = ExpressaoBooleana('a*b+c*a')
    if existe_solucao_para(expressao, expressao.variaveis, True):
        print (f'A expressâo booleana {expressao} possui solução para True.')
    else:
        print (f'A expressão booleana {expressao} não possui solução para True.')