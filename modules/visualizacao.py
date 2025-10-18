import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def gerar_dashboard(dados):
    """
    Gera visualizações básicas dos dados
    """
    print("📈 Gerando dashboard...")
    
    if dados.empty:
        print("❌ Nenhum dado para visualizar")
        return
    
    # Cria pasta outputs se não existir
    os.makedirs('outputs', exist_ok=True)
    
    # Configuração do estilo
    plt.style.use('default')
    sns.set_palette("husl")
    
    # 1. RESUMO ESTATÍSTICO
    print("   📋 Gerando resumo estatístico...")
    with open('outputs/resumo_estatistico.txt', 'w', encoding='utf-8') as f:
        f.write("=== RESUMO ESTATÍSTICO ===\n\n")
        f.write(f"Total de registros: {len(dados)}\n")
        f.write(f"Total de colunas: {len(dados.columns)}\n\n")
        
        f.write("COLUNAS NUMÉRICAS:\n")
        colunas_numericas = dados.select_dtypes(include=['number']).columns
        if not colunas_numericas.empty:
            f.write(dados[colunas_numericas].describe().to_string())
        else:
            f.write("Nenhuma coluna numérica encontrada\n")
        
        f.write("\n\nCOLUNAS DE TEXTO:\n")
        colunas_texto = dados.select_dtypes(include=['object']).columns
        if not colunas_texto.empty:
            for coluna in colunas_texto:
                f.write(f"\n{coluna}:\n")
                f.write(f"Valores únicos: {dados[coluna].nunique()}\n")
                f.write(f"Valores mais frequentes:\n{dados[coluna].value_counts().head().to_string()}\n")
    
    # 2. GRÁFICOS PARA COLUNAS NUMÉRICAS
    colunas_numericas = dados.select_dtypes(include=['number']).columns
    
    if len(colunas_numericas) > 0:
        print("   📊 Gerando gráficos...")
        
        # Histogramas para colunas numéricas
        fig, axes = plt.subplots(1, min(3, len(colunas_numericas)), figsize=(15, 5))
        if len(colunas_numericas) == 1:
            axes = [axes]
        
        for i, coluna in enumerate(colunas_numericas[:3]):  # Máximo 3 gráficos
            if i < len(axes):
                dados[coluna].hist(bins=20, ax=axes[i])
                axes[i].set_title(f'Distribuição de {coluna}')
                axes[i].set_xlabel(coluna)
                axes[i].set_ylabel('Frequência')
        
        plt.tight_layout()
        plt.savefig('outputs/histogramas.png', dpi=300, bbox_inches='tight')
        plt.close()
    
    # 3. GRÁFICO DE CONTAGEM PARA COLUNAS CATEGÓRICAS
    colunas_categoricas = dados.select_dtypes(include=['object']).columns
    
    if len(colunas_categoricas) > 0:
        # Pega a primeira coluna categórica com menos de 10 valores únicos
        for coluna in colunas_categoricas:
            if dados[coluna].nunique() <= 10:
                plt.figure(figsize=(10, 6))
                dados[coluna].value_counts().plot(kind='bar')
                plt.title(f'Contagem de Valores - {coluna}')
                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.savefig('outputs/contagem_categorias.png', dpi=300, bbox_inches='tight')
                plt.close()
                break
    
    print("✅ Dashboard gerado na pasta outputs/")
