"""Criação e impressão do labirinto."""
import random


def criar_labirinto(tamanho=8, densidade=0.25):
    """Gera um labirinto simples com início livre e fim garantido."""
    lab = [[" " for _ in range(tamanho)] for _ in range(tamanho)]

    for i in range(tamanho):
        for j in range(tamanho):
            if (i, j) != (0, 0) and (i, j) != (tamanho - 1, tamanho - 1):
                if random.random() < densidade:
                    lab[i][j] = "#"

    lab[0][0] = " "
    lab[tamanho - 1][tamanho - 1] = "F"

    return lab


def imprimir_labirinto(lab, console=None, pos=None):
    """Imprime o labirinto com jogador."""

    if console:
        from rich.table import Table

        table = Table(show_header=False, box=None, pad_edge=False)

        for _ in lab[0]:
            table.add_column(justify="center")

        for i, row in enumerate(lab):
            styled = []

            for j, c in enumerate(row):
                if pos and (i, j) == (pos[0], pos[1]):
                    styled.append("[bold green]P[/bold green]")
                elif c == "#":
                    styled.append("[red]#[/red]")
                elif c == "F":
                    styled.append("[bold yellow]F[/bold yellow]")
                else:
                    styled.append(" ")

            table.add_row(*styled)

        console.print(table)

    else:
        for i, linha in enumerate(lab):
            linha_str = []
            for j, c in enumerate(linha):
                if pos and (i, j) == (pos[0], pos[1]):
                    linha_str.append("P")
                else:
                    linha_str.append(c)

            print(" ".join(linha_str))