# Importando as duas filas de seus determinados documentos
from fila_normal import filanormal
from fila_prioritaria import FilaPrioritaria

# Criando objetos das duas filas existentes
fila_teste1 = filanormal()
fila_teste2 = FilaPrioritaria()


# Atualizando as filas 3 vezes cada uma
fila_teste1.atualizafila()
fila_teste1.atualizafila()
fila_teste1.atualizafila()

fila_teste2.atualiza_fila()
fila_teste2.atualiza_fila()
fila_teste2.atualiza_fila()

# Chamando os clientes de ambas as filas 3 vezes intercalando nos mesmos caixas
print(fila_teste1.chamaCliente(10))
print(fila_teste2.chama_cliente(10))

print(fila_teste1.chamaCliente(11))
print(fila_teste2.chama_cliente(11))

print(fila_teste1.chamaCliente(12))
print(fila_teste2.chama_cliente(12))

print(
    f'As estatisticas dos clintes da fila prioritarias foram as seguintes: {fila_teste2.estatistica ("10/5/2032", 219, "detail" )}'
)
