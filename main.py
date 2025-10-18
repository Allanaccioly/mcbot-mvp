from modules.coleta_dados import coletar_dados
from modules.processamento import processar_dados
from modules.visualizacao import gerar_dashboard

def main():
    print("🔹 Iniciando o McBot MVP...")
    
    # Coleta dados
    dados = coletar_dados()
    
    # Processa dados
    dados_processados = processar_dados(dados)
    
    # Gera dashboard
    gerar_dashboard(dados_processados)
    
    print("✅ MVP executado com sucesso. Verifique a pasta outputs/")

if __name__ == "__main__":
    main()
