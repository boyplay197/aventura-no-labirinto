"""Funções utilitárias."""
import time


def imprimir_menu(console=None):
    print("1 - Instruções")
    print("2 - Jogar")
    print("3 - Resolver (recursivo)")
    print("4 - Sair")


def imprimir_instrucoes(console=None):
    print("\nUse W A S D para se mover até o F.\n")


def animacao_vitoria(n, console=None):
    if n == 0:
        return
    print("🎉 Vitória!")
    time.sleep(0.3)
    animacao_vitoria(n - 1)


def resolver_labirinto(lab, x, y, visitado=None):
    """Resolve o labirinto recursivamente (DFS)."""
    if visitado is None:
        visitado = set()

    if (x, y) in visitado:
        return None

    if not (0 <= x < len(lab) and 0 <= y < len(lab[0])):
        return None

    if lab[x][y] == "#":
        return None

    if lab[x][y] == "F":
        return [(x, y)]

    visitado.add((x, y))

    caminhos = [(1,0),(-1,0),(0,1),(0,-1)]

    for dx, dy in caminhos:
        res = resolver_labirinto(lab, x + dx, y + dy, visitado)
        if res:
            return [(x, y)] + res

    return None