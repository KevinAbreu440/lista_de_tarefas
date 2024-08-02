import json
import os

CAMINHO_ARQUIVO = 'tarefas.json'

def carregar_tarefas():
    if os.path.exists(CAMINHO_ARQUIVO):
        with open(CAMINHO_ARQUIVO, 'r') as arquivo:
            return json.load(arquivo)
    return []

def salvar_tarefas(tarefas):
    with open(CAMINHO_ARQUIVO, 'w') as arquivo:
        json.dump(tarefas, arquivo)

def adicionar_tarefa(tarefa, tarefas):
    tarefas.append(tarefa)
    salvar_tarefas(tarefas)

def exibir_tarefas(tarefas):
    for idx, tarefa in enumerate(tarefas):
        print(f"{idx + 1}. {tarefa}")

def principal():
    tarefas = carregar_tarefas()
    while True:
        print("1. Adicionar Tarefa")
        print("2. Ver Tarefas")
        print("3. Sair")
        escolha = input("Digite a escolha (1/2/3): ")

        if escolha == '1':
            tarefa = input("Digite a descrição da tarefa: ")
            adicionar_tarefa(tarefa, tarefas)
        elif escolha == '2':
            exibir_tarefas(tarefas)
        elif escolha == '3':
            break
        else:
            print("Escolha inválida. Por favor, digite 1, 2 ou 3.")

if __name__ == "__main__":
    principal()
