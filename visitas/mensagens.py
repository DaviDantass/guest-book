import os
from datetime import datetime

mensagens = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mensagens.txt")
def gerar_id():
    return datetime.now().strftime("%Y%m%d%H%M%S") # Cria um ID único para cada mensagem

def checar_arquivo():
    if not os.path.exists(mensagens):
        with open(mensagens, 'w', encoding="utf-8") as arquivo: # Cria o arquivo de mensagens caso não exista
            pass
        print("Arquivo criado com sucesso.")

def ler_mensagens(): # Lê e retorna todas as mensagens do arquivo
    checar_arquivo()
    with open(mensagens, 'r', encoding="utf-8") as arquivo:
        return arquivo.readlines()

def salvar_mensagem(nome, mensagem): # Salva uma mensagem nova no arquivo com um ID único
    checar_arquivo()
    id_mensagem = gerar_id()
    linha = f"{id_mensagem} || {nome} || {mensagem}\n"
    with open(mensagens, 'a', encoding="utf-8") as arquivo:
        arquivo.write(linha)
    print("Mensagem salva com sucesso.")
    
def apagar_mensagem(id_mensagem): # Apaga uma mensagem do arquivo pelo ID
    checar_arquivo()
    mensagens_existentes = ler_mensagens()
    with open(mensagens, 'w', encoding="utf-8") as arquivo:
        for linha in mensagens_existentes:
            if not linha.split(" || ")[0] == id_mensagem:
                arquivo.write(linha)
    print("Mensagem apagada com sucesso.")
