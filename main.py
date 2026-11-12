from scanner.leitor_arquivo import ler_arquivo_txt
from scanner.detector import detectar_dado_sensivel
from tkinter import filedialog, messagebox

def main():
    caminho = filedialog.askopenfilename()
    mascarar = messagebox.askyesno("Mascarar Dados", "Deseja mascarar os dados sensíveis?")
    try: 
        conteudo = ler_arquivo_txt(caminho)

        resultados = detectar_dado_sensivel(conteudo, mascarar)
        print("\n ----------- Detector de Dados Vazados -----------")
        if not resultados:
            print("Nenhum dado sensível encontrado.")

        else:
            for resultado in resultados:
                print(f"[{resultado['tipo']}] Linha {resultado['linha']}: {resultado['valor']}")
            print(f"\n Resultados encontrados: {len(resultados)}")

    except (FileNotFoundError, PermissionError, OSError) as erro:
        print(f"Erro ao acessar arquivo: {erro}")


if __name__ == "__main__":
    main()