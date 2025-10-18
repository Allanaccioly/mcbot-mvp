import pandas as pd
import os

def coletar_dados():
    """
    Coleta dados de arquivos CSV e Excel na pasta data/
    """
    print("📂 Coletando dados...")
    data_dir = "data/"
    dados = []

    # Verifica se a pasta existe
    if not os.path.exists(data_dir):
        print(f"❌ Pasta '{data_dir}' não encontrada!")
        return pd.DataFrame()

    # Processa arquivos
    for arquivo in os.listdir(data_dir):
        caminho = os.path.join(data_dir, arquivo)
        
        try:
            if arquivo.endswith(".xlsx"):
                print(f"   📊 Lendo Excel: {arquivo}")
                df = pd.read_excel(caminho, engine='openpyxl')
                df['fonte_arquivo'] = arquivo
                dados.append(df)
                
            elif arquivo.endswith(".csv"):
                print(f"   📄 Lendo CSV: {arquivo}")
                df = pd.read_csv(caminho)
                df['fonte_arquivo'] = arquivo
                dados.append(df)
                
        except Exception as e:
            print(f"   ⚠️ Erro em {arquivo}: {e}")
            continue

    if not dados:
        print("❌ Nenhum arquivo .xlsx ou .csv encontrado!")
        return pd.DataFrame()

    # Combina todos os dados
    dados_combinados = pd.concat(dados, ignore_index=True)
    print(f"✅ {len(dados_combinados)} registros coletados de {len(dados)} arquivos")
    return dados_combinados
