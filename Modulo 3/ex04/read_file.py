import sys


def main() -> int:
    """open a file and print your content"""
    try:
        fd = open(str(sys.argv[1]), encoding="utf-8")
        print(fd.read(), end="")
        return 0
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")
        return 1
    except IsADirectoryError:
        print("Erro: O argumento enviado é um diretório.")
        return 1
    except Exception as e:
        print("Erro inesperado:", type(e).__name__)
        return 1


if __name__ == "__main__":
    sys.exit(main())
