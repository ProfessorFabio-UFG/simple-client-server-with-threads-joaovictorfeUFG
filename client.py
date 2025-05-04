from socket  import *
from constCS import *
from threading import Thread
from random import randint
from time import time

inicio = time()

# Função que executa a requisição ao servidor
def executa_requisicao(data):
  try:
    with socket(AF_INET, SOCK_STREAM) as s:  # Cria um socket para esta thread
      s.connect((HOST, PORT))
      s.send(data.encode())  # Envia a requisição para o servidor
      resposta = s.recv(1024).decode()  # Recebe a resposta do servidor
      print(resposta)
  except Exception as e:
    print(f"Erro na thread: {e}, thread: {data.strip().split()[3]}")

# loop para enviar requisições ao servidor com threads
for i in range(1, 101):
  entrada = f"{randint(1, 10)} {randint(1, 10)} {['soma', 'subtracao', 'multiplicacao', 'divisao'][randint(0, 3)]} {i}"

  t = Thread(target=executa_requisicao, args=(entrada,))
  t.start()  # Inicia uma nova thread para cada requisição
  t.join()  # Aguarda a thread terminar antes de iniciar a próxima

fim = time()

print(f"Tempo total de execução: {fim - inicio:.2f} segundos")