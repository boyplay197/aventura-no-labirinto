"""Controle do jogador."""

def iniciar_jogador():
    return [0, 0], 0


def mover(pos, direcao, lab):
    x, y = pos

    moves = {
        "w": (-1, 0),
        "s": (1, 0),
        "a": (0, -1),
        "d": (0, 1)
    }

    if direcao in moves:
        dx, dy = moves[direcao]
        nx, ny = x + dx, y + dy

        if not (0 <= nx < len(lab) and 0 <= ny < len(lab[0])):
            return pos

        if lab[nx][ny] == "#":
            return pos

        return [nx, ny]

    return pos


def pontuar(pontos, lab, pos):
    if lab[pos[0]][pos[1]] == "F":
        return pontos + 10
    return pontos + 1