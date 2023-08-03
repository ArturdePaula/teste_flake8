import abc

class FilaBase(metaclass=abc.ABCMeta):
    
    codigo: int = 0
    fila: list = []
    clientes_atendidos: list = []
    senha_atual: str = " "

    def reseta_fila(self) -> None:
        """Metodo/função que reseta a fila para começar do 0 novamente se o codigo ( posição na fila )
        já for de 100, caso contrario soma + 1 no codigo da fila"""

        if self.codigo == 200:
            self.codigo = 0
        else:
            self.codigo += 1

    @abc.abstractmethod
    def gera_senha_atual(self): 
        ...

    @abc.abstractmethod
    def atualiza_fila(self):
        ...
    
    @abc.abstractmethod
    def chama_cliente (self, caixa:int): 
        ...