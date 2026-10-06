'''
OPEN CLOSED PRINCIPLE

O código foi organizado seguindo o Princípio Aberto Fechado.

A classe Exame define uma interface comum para os tipos de exame.
Cada tipo implementa suas próprias condições de aprovação.

Novos tipos de exame podem ser adicionados por meio de novas classes,
sem alterar a classe responsável pela aprovação.
'''

from abc import ABC, abstractmethod

class Exame(ABC):
    @abstractmethod
    def verificar_condicoes(self):
        pass


class AprovaExame:
    def aprovar_solicitacao_exame(self, exame):
        if exame.verificar_condicoes():
            print("Exame aprovado!")


class ExameSangue(Exame):
    def verificar_condicoes(self):
        return True


class ExameRaioX(Exame):
    def verificar_condicoes(self):
        return True


aprovador = AprovaExame()

exame_sangue = ExameSangue()
exame_raio_x = ExameRaioX()

aprovador.aprovar_solicitacao_exame(exame_sangue)
aprovador.aprovar_solicitacao_exame(exame_raio_x)
