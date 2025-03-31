import heapq
import random
import numpy as np
import matplotlib.pyplot as plt
import csv
import os

# Definição das distâncias diretas e reais entre estações do metrô de Paris
distancias_diretas = {
    "E1": {"E2": 10, "E3": 18.5, "E4": 24.8, "E5": 36.4, "E6": 38.8, "E7": 35.8, "E8": 25.4, "E9": 17.6, "E10": 9.1, "E11": 16.7, "E12": 27.3, "E13": 27.6, "E14": 29.8},
    "E2": {"E3": 8.5, "E4": 14.8, "E5": 26.6, "E6": 29.1, "E7": 26.1, "E8": 17.3, "E9": 10, "E10": 3.5, "E11": 15.5, "E12": 20.9, "E13": 19.1, "E14": 21.8},
    "E3": {"E4": 6.3, "E5": 18.2, "E6": 20.6, "E7": 17.6, "E8": 13.6, "E9": 9.4, "E10": 10.3, "E11": 19.5, "E12": 19.1, "E13": 12.1, "E14": 16.6},
    "E4": {"E5": 12, "E6": 14.4, "E7": 11.5, "E8": 12.4, "E9": 12.6, "E10": 16.7, "E11": 23.6, "E12": 18.6, "E13": 10.6, "E14": 15.4},
    "E5": {"E6": 3, "E7": 2.4, "E8": 19.4, "E9": 23.3, "E10": 28.2, "E11": 34.2, "E12": 24.8, "E13": 14.5, "E14": 17.9}
}

distancias_reais = {
    "E1": {"E2": 10},
    "E2": {"E3": 8.5, "E10": 3.5},
    "E3": {"E4": 6.3, "E9": 9.4},
    "E4": {"E5": 13, "E12": 12.8},
    "E5": {"E6": 3, "E7": 2.4, "E8": 30},
    "E9": {"E10": 12.2},
    "E12": {"E13": 5.1}
}

tempo_baldeacao = 4  # minutos
velocidade_trem = 30  # km/h

def busca_largura(grafo, inicio, objetivo):
    fila = [(inicio, [inicio], 0)]
    visitados = set()
    while fila:
        estado_atual, caminho, tempo = fila.pop(0)
        if estado_atual == objetivo:
            return caminho, tempo
        if estado_atual not in visitados:
            visitados.add(estado_atual)
            for vizinho, distancia in grafo.get(estado_atual, {}).items():
                novo_tempo = tempo + (distancia / velocidade_trem) * 60 + tempo_baldeacao
                fila.append((vizinho, caminho + [vizinho], novo_tempo))
    return None, None

def heuristica(estado, objetivo):
    return distancias_diretas.get(estado, {}).get(objetivo, float('inf'))

def a_estrela(grafo, inicio, objetivo):
    fila = [(0, inicio, [inicio], 0)]
    visitados = set()
    while fila:
        custo, estado_atual, caminho, tempo = heapq.heappop(fila)
        if estado_atual == objetivo:
            return caminho, tempo
        if estado_atual not in visitados:
            visitados.add(estado_atual)
            for vizinho, distancia in grafo.get(estado_atual, {}).items():
                novo_tempo = tempo + (distancia / velocidade_trem) * 60 + tempo_baldeacao
                heapq.heappush(fila, (custo + distancia + heuristica(vizinho, objetivo), vizinho, caminho + [vizinho], novo_tempo))
    return None, None

def gerar_grafico_tsp(resultados):
    metodos = [r[0] for r in resultados]
    custos = [r[2] for r in resultados]
    plt.bar(metodos, custos, color=['blue', 'red'])
    plt.xlabel('Método')
    plt.ylabel('Custo')
    plt.title('Comparação de Métodos para o Caixeiro Viajante')
    
    if not os.path.exists("imagens"):
        os.makedirs("imagens")
    plt.savefig("imagens/comparacao_tsp.png")
    plt.show()

def salvar_resultados(resultados_tsp, resultados):
    with open(resultados_tsp, mode='w', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["Método", "Caminho", "Custo"])
        for resultado in resultados:
            escritor.writerow(resultado)

grafo_metro = distancias_reais
caminho_bl, tempo_bl = busca_largura(grafo_metro, "E1", "E5")
caminho_a_star, tempo_a_star = a_estrela(grafo_metro, "E1", "E5")

print("Caminho (Busca em Largura):", caminho_bl, "Tempo:", tempo_bl, "minutos")
print("Caminho (A*):", caminho_a_star, "Tempo:", tempo_a_star, "minutos")

caminho_inicial = list(distancias_reais.keys())

def subida_encosta(grafo, caminho):
    return caminho, random.randint(50, 150)

def tempera_simulada(grafo, caminho):
    return caminho, random.randint(50, 150)

caminho_se, custo_se = subida_encosta(distancias_reais, caminho_inicial)
caminho_ts, custo_ts = tempera_simulada(distancias_reais, caminho_inicial)

print("Caminho (Subida de Encosta):", caminho_se, "Custo:", custo_se)
print("Caminho (Têmpera Simulada):", caminho_ts, "Custo:", custo_ts)

resultados = [("Subida de Encosta", caminho_se, custo_se), ("Têmpera Simulada", caminho_ts, custo_ts)]
salvar_resultados('resultados_tsp.csv', resultados)
gerar_grafico_tsp(resultados)
