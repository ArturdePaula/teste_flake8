class filanormal:
    codigo: int = 0
    fila = []
    clientesatendidos = []
    senhatual: str = " "

    def gerasenhaatual(self) -> None:
        """Metodo/Função que gera a senha atua, concatenanto o prefixo NM com o codigo da posição na fila"""
        self.senhatual = f"NM {self.codigo}"

    def resetafila(self) -> None:
        """Metodo/função que reseta a fila para começar do 0 novamente se o codigo ( posição na fila ) já for de 100, caso contrario soma + 1 na codigo da fila"""
        if self.codigo == 100:
            self.codigo = 0
        else:
            self.codigo += 1

    def atualizafila(self) -> None:
        """Metodo/Função para quando um clinte requisita uma senha, aumentando o codigo da fila, gerando sua senha e colocando o mesmo na fila"""
        self.resetafila()
        self.gerasenhaatual()
        self.fila.append(self.senhatual)

    def chamaCliente(self, caixa: int) -> str:
        """Metodo/Função que retorna uma String informando o codigo do primeiro cliente e o numero do caixa que esta chamando para atendimento. Após isso
        a senha do cliente atendido e colocada na lista de clientes atendidos"""
        cliente_atual = self.fila.pop(0)
        self.clientesatendidos.append(cliente_atual)
        return f"Cliente de codigo { cliente_atual }, dirija-se ao caixa {caixa}"
