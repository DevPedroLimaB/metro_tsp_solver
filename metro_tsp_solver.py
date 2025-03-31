import heapq
import random
import numpy as np
import matplotlib.pyplot as plt
import csv
import os

# ---------- Problema do Metrô de Paris ----------
metro_paris = {
    "E1": {"E2": 10, "E3": 8.5},
    "E2": {"E1": 10, "E3": 6.3, "E4": 10},
    "E3": {"E1": 8.5, "E2": 6.3, "E5": 15.3},
    "E4": {"E2": 10, "E6": 3},
    "E5": {"E3": 15.3, "E7": 12.8},
    "E6": {"E4": 3, "E7": 2.4},
    "E7": {"E5": 12.8, "E6": 2.4},
    "E8": {"E9": 9.6},
    "E9": {"E8": 9.6, "E10": 12.2},
    "E10": {"E9": 12.2, "E11": 8.4},
    "E11": {"E10": 8.4},
    "E12": {"E13": 5.1},
    "E13": {"E12": 5.1},
}

def busca_uniforme(inicio, destino):
    fila = [(0, inicio, [])]
    visitados = set()
    
    while fila:
        custo, estacao, caminho = heapq.heappop(fila)
        if estacao in visitados:
            continue
        
        caminho = caminho + [estacao]
        visitados.add(estacao)
        
        if estacao == destino:
            return caminho, custo
        
        for vizinho, dist in metro_paris.get(estacao, {}).items():
            if vizinho not in visitados:
                heapq.heappush(fila, (custo + dist, vizinho, caminho))
    
    return None, float("inf")

def salvar_resultado_metro(arquivo, caminho, custo):
    if not caminho:
        print("Erro: Caminho inválido, não pode ser salvo.")
        return
    with open(arquivo, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Estação", "Caminho Percorrido"])
        writer.writerow([" -> ".join(map(str, caminho)), custo])

# ---------- Problema do Caixeiro Viajante (TSP) ----------
def carregar_instancia_tsp(arquivo):
    pontos = []
    with open(arquivo, 'r') as f:
        linhas = f.readlines()
        for linha in linhas:
            partes = linha.strip().split()
            if len(partes) == 3:
                _, x, y = partes
                pontos.append((float(x), float(y)))
    return pontos

def calcular_distancia(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))

def avaliar_solucao(caminho, pontos):
    return sum(calcular_distancia(pontos[caminho[i]], pontos[caminho[i+1]]) for i in range(len(caminho)-1))

def subida_encosta(pontos):
    caminho = list(range(len(pontos)))
    random.shuffle(caminho)
    custo_atual = avaliar_solucao(caminho, pontos)
    
    for _ in range(1000):
        i, j = random.sample(range(len(caminho)), 2)
        caminho[i], caminho[j] = caminho[j], caminho[i]
        novo_custo = avaliar_solucao(caminho, pontos)
        if novo_custo < custo_atual:
            custo_atual = novo_custo
        else:
            caminho[i], caminho[j] = caminho[j], caminho[i]
    
    return caminho, custo_atual

def salvar_resultado_tsp(arquivo, caminho, custo):
    with open(arquivo, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Caminho", "Custo"])
        writer.writerow([caminho, custo])

def gerar_grafico_tsp(pontos, caminho, titulo):
    plt.figure(figsize=(8, 6))
    for i in range(len(caminho) - 1):
        p1, p2 = pontos[caminho[i]], pontos[caminho[i+1]]
        plt.plot([p1[0], p2[0]], [p1[1], p2[1]], 'r-')
    for x, y in pontos:
        plt.scatter(x, y, c='blue')
    plt.title(titulo)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

# ---------- Execução ----------
if __name__ == "__main__":
    # Resolver Metrô de Paris
    if "E1" in metro_paris and "E7" in metro_paris:
        caminho_metro, custo_metro = busca_uniforme("E1", "E7")
        if caminho_metro:
            salvar_resultado_metro("resultado_metro.csv", caminho_metro, custo_metro)
            print(f"Caminho do Metrô de Paris salvo em resultado_metro.csv: {caminho_metro}, Custo: {custo_metro}")
        else:
            print("Erro: Caminho do metrô não encontrado.")
    else:
        print("Erro: Estação de origem ou destino inválida.")
    
    # Resolver TSP
    if os.path.exists("germany.tsp"):
        pontos = carregar_instancia_tsp("germany.tsp")
        if pontos:
            caminho_tsp, custo_tsp = subida_encosta(pontos)
            salvar_resultado_tsp("resultado_tsp.csv", caminho_tsp, custo_tsp)
            gerar_grafico_tsp(pontos, caminho_tsp, "Solução do Problema do Caixeiro Viajante")
            print(f"Caminho do TSP salvo em resultado_tsp.csv, Custo: {custo_tsp}")
        else:
            print("Erro: Nenhum ponto carregado do arquivo germany.tsp.")
    else:
        print("Erro: Arquivo germany.tsp não encontrado.")
