from fila_normal import filanormal
from fila_prioritaria import FilaPrioritaria
from valores_constantes import TIPO_DE_FILA_NORMAL, TIPO_DE_FILA_PRIORITARIA
from typing import Union


class Fabricafila:
    @staticmethod
    def pega_fila(tipo_da_fila) -> Union[filanormal, FilaPrioritaria]:
        """Metodo que recebe o tipo da fila e retorne um objeto da
        fila selecionada"""
        if tipo_da_fila == TIPO_DE_FILA_NORMAL:
            return filanormal()
        elif tipo_da_fila == TIPO_DE_FILA_PRIORITARIA:
            return FilaPrioritaria()
        else:
            raise NotImplementedError("Este tipo de fila não existe")
