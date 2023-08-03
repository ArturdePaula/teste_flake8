#Esta classe já foi feita usando PEP8

class FilaPrioritaria: 
    codigo: int = 0
    fila = []
    clientes_atendidos = []
    senha_atual: str = " "

    def gera_senha_atual (self) -> None:
        """Metodo/Função que gera a senha atua, concatenanto o 
        prefixo NM com o codigo da posição na fila""" 
        self.senha_atual = f'PR{self.codigo}'

    def reseta_fila (self) -> None:
        """Metodo/função que reseta a fila para começar do 0 novamente se o codigo ( posição na fila ) 
        já for de 100, caso contrario soma + 1 no codigo da fila"""
        if (self.codigo == 100): 

            self.codigo = 0
        else: 
            self.codigo += 1
    
    def atualiza_fila (self) -> None:
        """Metodo/Função para quando um clinte requisita uma senha, 
        aumentando o codigo da fila, gerando sua senha e colocando o mesmo na fila"""
        self.reseta_fila ()
        self.gera_senha_atual ()
        self.fila.append (self.senha_atual)

    def chama_cliente (self, caixa: int) ->str: 
        """Metodo/Função que retorna uma String informando o codigo do primeiro 
        cliente e o numero do caixa que esta chamando para atendimento. Após isso
        a senha do cliente atendido e colocada na lista de clientes atendidos""" 
        cliente_atual = self.fila.pop(0)
        self.clientes_atendidos.append (cliente_atual)
        return (f'Cliente de codigo { cliente_atual }, dirija-se ao caixa {caixa}')
    
    def estatistica (self, dia:str, agencia: int, flag: str) -> dict: 
        """Metodo/Função que recebe uma data, a agência, e uma flag para determinar qual o
        tipo de estatistica que deve ser retornado. Caso a flag seja 'detail' o retorno será detalhado
        caso contrario o retorno será um dicionario com a quantidade de clientes atendidos por agencia e dia"""
        if flag!='detail': 
            estatistica = {f'{agencia} - {dia}' : len (self.clientes_atendidos)}
        else: 
            estatistica = {}
            estatistica['dia'] = dia
            estatistica['agencia'] = agencia
            estatistica['clientes_atendidos'] = self.clientes_atendidos
            estatistica['quantidade_clintes_atendidos'] = len ( self.clientes_atendidos)
        
        return estatistica

