class FilaBase:
    
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
