# import pessoa
from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula, curso) -> None:
        super().__init__(nome, idade)
        self.__nome = nome
        self._matricula = matricula
        self._curso = curso

    def get_ficha(self):
        return f'{self.__nome}, n° {self._matricula}, no curso {self._curso}'

    @classmethod
    def create_if_comp(cls, nome, idade, matricula, curso):
        if curso not in('COMP', 'ENSW'):
            return None

        return cls(nome, idade, matricula, curso)
