import pandas as pd

def processar_dados(dados):
    """
    Processa e limpa os dados coletados
    """
    print("🔧 Processando dados...")
    
    if dados.empty:
        print("❌ Nenhum dado para processar")
        return dados
    
    # Faz uma cópia para não modificar o original
    dados_processados = dados.copy()
    
    # Remove colunas completamente vazias
    dados_processados = dados_processados.dropna(axis=1, how='all')
    
    # Preenche valores numéricos faltantes com 0
    colunas_numericas = dados_processados.select_dtypes(include=['number']).columns
    dados_processados[colunas_numericas] = dados_processados[colunas_numericas].fillna(0)
    
    # Preenche valores de texto faltantes com "Não informado"
    colunas_texto = dados_processados.select_dtypes(include=['object']).columns
    dados_processados[colunas_texto] = dados_processados[colunas_texto].fillna('Não informado')
    
    print(f"✅ Dados processados: {dados_processados.shape[0]} linhas, {dados_processados.shape[1]} colunas")
    return dados_processados
