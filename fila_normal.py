from fila_base import FilaBase

from valores_constantes import CODIGO_FILA_NORMAL


class filanormal(FilaBase):
    def gera_senha_atual(self) -> None:
        """Metodo/Função que gera a senha atua, concatenanto o
        prefixo NM com o codigo da posição na fila"""

        self.senha_atual = f"{CODIGO_FILA_NORMAL}{self.codigo}"

    def chama_cliente(self, caixa: int) -> str:
        """Metodo/Função que retorna uma String informando o codigo do primeiro
        cliente e o numero do caixa que esta chamando para atendimento.
        Após isso a senha do cliente atendido e colocada na lista de
        clientes atendidos"""

        cliente_atual = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return f"Cliente de codigo { cliente_atual }, dirija-se ao caixa {caixa}"
