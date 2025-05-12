import socket

HOST = 'localhost'
PORT = 8080

def extrair_requisicao_http(conexao):
    dados = b""
    conexao.settimeout(5)  # Tempo de espera de 5 segundos para receber dados
    while True:
        try:
            parte = conexao.recv(1024)
            if not parte:
                print("⚠️ Conexão fechada pelo cliente.")
                break  # Sai do loop se não houver dados (conexão fechada)
            dados += parte
            print(f"🔍 Dados recebidos: {parte}")
            if b"\r\n\r\n" in dados:
                break
        except socket.timeout:
            print("⚠️ Timeout atingido enquanto aguardava dados da requisição.")
            break
        except Exception as e:
            print(f"❌ Erro ao ler a requisição: {e}")
            break

    headers, _, restante = dados.partition(b"\r\n\r\n")
    headers_str = headers.decode("utf-8")
    print("\n📥 Cabeçalhos recebidos:\n", headers_str)

    if not headers_str.strip():
        print("❌ Cabeçalho da requisição vazio!")
        return None, None  # Retorna None se não houver cabeçalhos

    return headers_str, restante

def receber_corpo(headers, conexao, body_inicial):
    # Recebe o corpo de uma requisição HTTP a partir dos headers e da conexão.
    # Extrai o valor do Content-Length dos headers
    # Inicializa o corpo com a parte já recebida e continua recebendo até atingir o tamanho esperado
    # Decodifica o corpo recebido de bytes para string
    content_length = 0
    for linha in headers.split("\r\n"):
        if linha.lower().startswith("content-length:"):
            content_length = int(linha.split(":")[1].strip())
            break
    print(f"📏 Content-Length esperado: {content_length}")
    restante = body_inicial
    while len(restante) < content_length:
        restante += conexao.recv(1024)
    corpo = restante.decode("utf-8")
    print("📦 Corpo da requisição recebido:\n", corpo)
    return corpo
