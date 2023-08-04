import abc


class FilaBase(metaclass=abc.ABCMeta):
    codigo: int = 0
    fila: list = []
    clientes_atendidos: list = []
    senha_atual: str = " "

    def reseta_fila(self) -> None:
        """Metodo/função que reseta a fila para começar do 0
        novamente se o codigo ( posição na fila ) já for de 100,
        caso contrario soma + 1 no codigo da fila"""

        if self.codigo == 200:
            self.codigo = 0
        else:
            self.codigo += 1

    def inseri_cliente(self):
        """Metodo/função que inseri a senha do cliente na fila
        para ser atendido"""
        self.fila.append(self.senha_atual)

    @abc.abstractmethod
    def gera_senha_atual(self):
        ...

    def atualiza_fila(self):
        """Metodo/função template que chama o metodo reseta_fila,
        gera_senha_atual e inseri_cliente,ou seja, quando
        um novo cliente requisita uma senha"""
        self.reseta_fila()
        self.gera_senha_atual()
        self.inseri_cliente()

    @abc.abstractmethod
    def chama_cliente(self, caixa: int):
        ...
