# Importando a fabrica de filas e seu metodo para gerar o objeto da fila desejada
from fabrica_fila import Fabricafila

# Criando objetos das duas filas existentes
fila_teste1 = Fabricafila.pega_fila("normal")
fila_teste2 = Fabricafila.pega_fila("prioritaria")

# Atualizando as filas 3 vezes cada uma
fila_teste1.atualiza_fila()
fila_teste2.atualiza_fila()
fila_teste1.atualiza_fila()
fila_teste2.atualiza_fila()
fila_teste1.atualiza_fila()
fila_teste2.atualiza_fila()


# Chamando os clientes de ambas as filas 3 vezes intercalando nos mesmos caixas
print(fila_teste1.chama_cliente(10))

print(fila_teste2.chama_cliente(10))

print(fila_teste1.chama_cliente(11))

print(fila_teste2.chama_cliente(11))

print(fila_teste1.chama_cliente(12))

print(fila_teste2.chama_cliente(12))

print(
    f'As estatisticas dos clintes da fila prioritarias foram as seguintes: {fila_teste2.estatistica ("10/5/2032", 219, "detail" )}'
)
