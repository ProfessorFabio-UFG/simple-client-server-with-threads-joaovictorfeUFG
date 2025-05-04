
# Análise de Cliente-Servidor com Sockets e Threads

Este experimento tem como objetivo analisar o impacto do uso de **threads** em aplicações cliente-servidor desenvolvidas com **sockets** em Python. Foram comparadas duas abordagens: uma com threads apenas no servidor e outra com threads tanto no cliente quanto no servidor.

---

## 🔄 Threads Apenas no Servidor

A primeira implementação utilizou threads **somente no lado do servidor**. O cliente, por sua vez, enviava **100 requisições sequenciais**, aguardando o término de cada uma antes de iniciar a próxima.

No servidor, foi simulado um atraso entre **1 e 3 segundos** para processar cada requisição.

### 🧪 Resultados

Foram realizadas 3 execuções do cliente com 100 requisições cada. Os tempos de execução observados foram:

- 232.49 segundos
- 232.44 segundos
- 240.64 segundos

**Média de execução**: **235.19 segundos**

Essa abordagem, apesar de tratar múltiplos clientes de forma concorrente no servidor, ainda é limitada pela natureza sequencial do cliente, tornando o sistema do lado do cliente ineficiente.

---

## ⚡ Threads no Cliente e no Servidor

Na segunda abordagem, tanto o **cliente quanto o servidor** foram implementados com threads, permitindo que o cliente executasse **100 requisições simultâneas**.

Assim como na versão anterior, o servidor introduziu um atraso aleatório entre **1 e 3 segundos** por requisição.

### 🧪 Resultados

A seguir os tempos (em segundos) de 10 execuções completas:

- 3.32, 3.32, 3.34, 3.90, 2.39, 3.31, 3.33, 3.32, 3.33, 3.36

**Média de execução**: **3.392 segundos**

Esta abordagem se mostrou **significativamente mais eficiente**, aproveitando o paralelismo para reduzir drasticamente o tempo total.

---

## Resumo

O experimento evidenciou de forma prática a importância do uso de **concorrência** e **paralelismo** em aplicações de rede. Utilizar **threads no cliente e no servidor** permitiu que múltiplas requisições fossem tratadas ao mesmo tempo, melhorando a performance de forma exponencial.

Além disso, foram aprendidos conceitos fundamentais como:

- A diferença entre execução sequencial e concorrente
- A função e comportamento do método `.join()` em threads
- O impacto do uso de `sleep()` para simular carga no servidor
- Como medir e comparar o desempenho entre abordagens distintas

Por fim, o exercício demonstrou como otimizações simples com **multithreading** podem transformar a escalabilidade e eficiência de um sistema distribuído.
