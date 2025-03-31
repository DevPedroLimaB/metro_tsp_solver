import heapq
import random
import numpy as np
import matplotlib.pyplot as plt
import csv
import os

# Função para carregar os pontos do arquivo .tsp
def carregar_instancia_tsp(arquivo):
    if not os.path.exists(arquivo):
        print(f"Erro: Arquivo '{arquivo}' não encontrado.")
        return []
    
    with open(arquivo, 'r') as f:
        linhas = f.readlines()
    
    if not linhas:
        print(f"Erro: Arquivo '{arquivo}' está vazio.")
        return []

    pontos = []
    for linha in linhas:
        partes = linha.strip().split()
        if len(partes) == 3:  # Ignora a primeira coluna com o índice
            _, x, y = partes
            pontos.append((float(x), float(y)))
        else:
            print(f"Ignorando linha inválida: {linha.strip()}")
    
    return pontos

# Função para calcular distância euclidiana entre dois pontos
def calcular_distancia(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))

# Função para avaliar a solução (soma das distâncias do caminho)
def avaliar_solucao(caminho, pontos):
    return sum(calcular_distancia(pontos[caminho[i]], pontos[caminho[i+1]]) for i in range(len(caminho)-1))

# Algoritmo de Subida de Encosta
def subida_encosta(pontos):
    if len(pontos) < 2:
        print("Erro: Não há pontos suficientes para o TSP.")
        return [], float('inf')

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

# Algoritmo de Têmpera Simulada
def tempera_simulada(pontos, temp_inicial=1000, resfriamento=0.99, temp_min=1):
    if len(pontos) < 2:
        print("Erro: Não há pontos suficientes para o TSP.")
        return [], float('inf')

    caminho = list(range(len(pontos)))
    random.shuffle(caminho)
    custo_atual = avaliar_solucao(caminho, pontos)
    temp = temp_inicial

    while temp > temp_min:
        i, j = random.sample(range(len(caminho)), 2)
        caminho[i], caminho[j] = caminho[j], caminho[i]
        novo_custo = avaliar_solucao(caminho, pontos)

        if novo_custo < custo_atual or random.random() < np.exp((custo_atual - novo_custo) / temp):
            custo_atual = novo_custo
        else:
            caminho[i], caminho[j] = caminho[j], caminho[i]

        temp *= resfriamento
    
    return caminho, custo_atual

# Função para salvar os resultados em um arquivo CSV
def salvar_resultados(arquivo, resultados):
    with open(arquivo, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Algoritmo", "Caminho", "Custo"])
        for resultado in resultados:
            writer.writerow(resultado)

# Função para gerar gráfico da solução do TSP
def gerar_grafico_tsp(pontos, caminho, titulo="Solução do Problema do Caixeiro Viajante"):
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

# Carregar os pontos do arquivo
pontos = carregar_instancia_tsp("germany.tsp")

if pontos:
    resultados = []

    for _ in range(10):
        caminho_se, custo_se = subida_encosta(pontos)
        caminho_ts, custo_ts = tempera_simulada(pontos)
        
        resultados.append(("Subida de Encosta", caminho_se, custo_se))
        resultados.append(("Têmpera Simulada", caminho_ts, custo_ts))

    # Salvar resultados
    salvar_resultados('resultados_tsp.csv', resultados)

    # Gerar gráfico da melhor solução encontrada
    melhor_caminho = min(resultados, key=lambda x: x[2])[1]  # Seleciona o menor custo
    gerar_grafico_tsp(pontos, melhor_caminho)
