from fila_base import FilaBase

from valores_constantes import CODIGO_FILA_PRIORITARIA


class FilaPrioritaria(FilaBase):
    def gera_senha_atual(self) -> None:
        """Metodo/Função que gera a senha atua, concatenanto o
        prefixo NM com o codigo da posição na fila"""

        self.senha_atual = f"{CODIGO_FILA_PRIORITARIA}{self.codigo}"

    def chama_cliente(self, caixa: int) -> str:
        """Metodo/Função que retorna uma String informando o codigo do primeiro
        cliente e o numero do caixa que esta chamando para atendimento. Após isso
        a senha do cliente atendido e colocada na lista de clientes atendidos"""

        cliente_atual = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return f"Cliente de codigo { cliente_atual }, dirija-se ao caixa {caixa}"

    def estatistica(self, dia: str, agencia: int, flag: str) -> dict:
        """Metodo/Função que recebe uma data, a agência,
        e uma flag para determinar qual o tipo de estatistica que
        deve ser retornado. Caso a flag seja 'detail' o retorno será
        detalhado caso contrario o retorno será um dicionario com a
        quantidade de clientes atendidos por agencia e dia
        """

        if flag != "detail":
            estatistica = {f"{agencia} - {dia}": len(self.clientes_atendidos)}
        else:
            estatistica = {}
            estatistica["dia"] = dia
            estatistica["agencia"] = agencia
            estatistica["clientes_atendidos"] = self.clientes_atendidos
            estatistica["quantidade_clintes_atendidos"] = len(self.clientes_atendidos)

        return estatistica
