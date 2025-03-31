# **Metro TSP Solver**

## **Descrição**
Este projeto implementa algoritmos de busca para encontrar o caminho mais curto no metrô de Paris e algoritmos de otimização para resolver o Problema do Caixeiro Viajante (TSP) com base em uma instância da Alemanha.

## **Estrutura do Projeto**
```
metro_tsp_solver/
│-- imagens/                 # Pasta para armazenar imagens geradas
│-- germany.tsp              # Arquivo contendo as coordenadas das cidades
│-- metro_tsp_solver.py      # Código principal do projeto
│-- README.md                # Este arquivo de documentação
│-- Relatorio_Tecnico.pdf    # Relatório técnico detalhado
│-- requisitos.txt           # Lista de dependências
│-- resultados_tsp.csv       # Resultados das execuções dos algoritmos
```

## **Instalação**
1. Clone o repositório:
   ```bash
   git clone https://github.com/DevPedroLimaB/metro_tsp_solver.git
   ```
2. Acesse a pasta do projeto:
   ```bash
   cd metro_tsp_solver
   ```
3. Instale as dependências:
   ```bash
   pip install -r requisitos.txt
   ```

## **Execução**
Para rodar o código principal:
```bash
python metro_tsp_solver.py
```

## **Algoritmos Implementados**
### **Busca no Metrô de Paris**
- **Busca em Largura (BFS)**: Um algoritmo simples de busca que explora todos os vizinhos de um nó antes de explorar nós mais profundos.
- **A* (A-estrela)**: Um algoritmo de busca informada que utiliza uma heurística para otimizar a busca, estimando o custo do caminho até o objetivo.

### **Problema do Caixeiro Viajante (TSP)**
- **Subida de Encosta**: Um algoritmo de otimização local que tenta melhorar a solução iterativamente trocando as cidades.
- **Têmpera Simulada**: Um algoritmo probabilístico de otimização que permite explorar soluções piores temporariamente para escapar de máximos locais, reduzindo gradualmente a aceitação de soluções piores.

## **Entrada e Saída**
- O arquivo `germany.tsp` contém as coordenadas das cidades no formato:
  ```plaintext
  <id> <x> <y>
  ```
- O script `metro_tsp_solver.py` lê esse arquivo, executa os algoritmos e gera os resultados em `resultados_tsp.csv`.
- O gráfico da solução do TSP é gerado e salvo na pasta `imagens/`.

## **Autores**
- Pedro Henrique Lima Barbosa e Antonio Freires
