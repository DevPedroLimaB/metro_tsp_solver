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
- **Busca em Largura (BFS)**
- **A* (A-estrela)**

### **Problema do Caixeiro Viajante (TSP)**
- **Subida de Encosta**
- **Têmpera Simulada**

## **Entrada e Saída**
- O arquivo `germany.tsp` contém as coordenadas das cidades.
- O script `metro_tsp_solver.py` lê esse arquivo, executa os algoritmos e gera os resultados em `resultados_tsp.csv`.
- O gráfico da solução do TSP é salvo na pasta `imagens/`.

## **Autores**
- Pedro Henrique Lima Barbosa e Antonio Freires

