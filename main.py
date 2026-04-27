"""Entrada principal com CLI."""
import argparse
import time
from aventura_pkg import labirinto, jogador, utils


def jogar(console=None, dificuldade="medio"):
    size = 8 if dificuldade == "medio" else (10 if dificuldade == "dificil" else 6)

    lab = labirinto.criar_labirinto(size)
    pos, pontos = jogador.iniciar_jogador()

    while True:
        # 🔥 LIMPA TELA
        import os
        os.system("cls" if os.name == "nt" else "clear")

        # verifica vitória
        if lab[pos[0]][pos[1]] == "F":
            utils.animacao_vitoria(1, console)
            print("\n🎉 Você venceu!")
            print("Pontuação:", pontos)
            break

        # 🔥 imprime com POS (ESSENCIAL)
        labirinto.imprimir_labirinto(lab, console, pos)

        mv = input("Mover (w/a/s/d): ").lower().strip()
        pos = jogador.mover(pos, mv, lab)
        pontos = jogador.pontuar(pontos, lab, pos)


def resolver_animado(console=None):
    lab = labirinto.criar_labirinto(8)
    path = utils.resolver_labirinto(lab, 0, 0)

    if not path:
        print("Sem solução gerada, tente novamente.")
        return

    for (x, y) in path:
        import os
        os.system("cls" if os.name == "nt" else "clear")

        labirinto.imprimir_labirinto(lab, console, [x, y])
        time.sleep(0.2)

    print("\n🤖 Labirinto resolvido com recursividade!")


def main():
    parser = argparse.ArgumentParser(description="Aventura no Labirinto")

    parser.add_argument("--name", required=True)
    parser.add_argument("--color", default="green")
    parser.add_argument("--dificuldade", default="medio", choices=["facil", "medio", "dificil"])
    parser.add_argument("--disable-sound", action="store_true")
    parser.add_argument("--use-rich", action="store_true")

    args = parser.parse_args()

    console = None
    if args.use_rich:
        try:
            from rich.console import Console
            console = Console()
        except:
            console = None

    while True:
        utils.imprimir_menu(console)
        escolha = input("Escolha: ").strip()

        match escolha:
            case "1":
                utils.imprimir_instrucoes(console)

            case "2":
                jogar(console, args.dificuldade)

            case "3":
                resolver_animado(console)

            case "4":
                print("Saindo...")
                break

            case _:
                print("Opção inválida")


if __name__ == "__main__":
    main()