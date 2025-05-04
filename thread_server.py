from socket  import *
from constCS import *
from threading import Thread
import time
import random

s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(100)

def calcular_operacao(num1, num2, operacao):
  if operacao == "soma":
    resultado = num1 + num2
  elif operacao == "subtracao":
    resultado = num1 - num2
  elif operacao == "multiplicacao":
    resultado = num1 * num2
  elif operacao == "divisao":
    if num2 == 0:
      return "Erro: Divisão por zero"
    resultado = num1 / num2
  else:
    return "Erro: Operação inválida"
  
  return f"O resultado da {operacao} é: {resultado}"

def tratamento_requisicao(conn, data):
  time.sleep(random.uniform(1, 3))  # Simula um atraso aleatório entre 1 e 3 segundos
  input = data.decode().strip()
  partes = input.split()

  if len(partes) != 4:
    resposta = "Erro: Entrada inválida. Use o formato 'int int str id'"
  else:
    num1, num2, operacao = float(partes[0]), float(partes[1]), partes[2]
    resposta = f"operação {partes[3]}: {calcular_operacao(num1, num2, operacao)}"

  conn.send(resposta.encode())

def tratamento_cliente(conn, addr):
  while True:
    data = conn.recv(1024)
    if not data:
      break
    Thread(target=tratamento_requisicao, args=(conn, data)).start()
  conn.close()

while True:
  conn, addr = s.accept()
  Thread(target=tratamento_cliente, args=(conn, addr)).start()
