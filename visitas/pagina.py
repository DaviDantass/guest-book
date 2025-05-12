from mensagens import ler_mensagens
import os

def renderizar_pagina(mensagens, mensagem_sucesso=""):
    """
    Gera o HTML final preenchendo os espaços no index.html.
    """
    css_path = "/static/style.css" # Define o caminho para o arquivo CSS.
    base_dir = os.path.dirname(os.path.abspath(__file__)) # Obtém o diretório base do script.
    template_path = os.path.join(base_dir, "templates", "index.html") # Define o caminho para o template HTML.

    with open(template_path, "r", encoding="utf-8") as f: # Abre o arquivo HTML para leitura.
        html = f.read() 

    bloco_sucesso = f"<p><strong>{mensagem_sucesso}</strong></p>" if mensagem_sucesso else "" 
    html = html.replace("", bloco_sucesso) 
    lista_html = [] 
    for linha in mensagens: 
        try:
            id_msg, nome, texto = linha.strip().split(" || ") 
            lista_html.append(f"""
                    <div class="mensagem">
                        <p><strong>{nome}</strong>: {texto}</p>
                        <form method="POST" action="/delete">
                            <input type="hidden" name="id" value="{id_msg}">
                            <button type="submit">Apagar Mensagem</button>
                        </form>
                    </div>
            """) # Cria o HTML para exibir a mensagem e o botão de apagar.
        except ValueError:
            continue 

    html = html.replace("", f"<ul>{''.join(lista_html)}</ul>") 
    html = html.replace("", f'<link rel="stylesheet" href="{css_path}">') 

    return html # Retorna o HTML final renderizado.

print(renderizar_pagina(ler_mensagens())) 