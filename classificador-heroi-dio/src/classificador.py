"""Classificador de nível de Herói.

Conceitos aplicados: variáveis, operadores, laços de repetição e
estruturas de decisão.
"""

# Variáveis globais (constantes) com os limites de cada nível.
# Regra: XP <= limite -> nível. Acima de 10.000 -> Radiante.
NIVEL_FINAL = "Radiante"
FAIXAS = [
    (1000, "Ferro"),
    (2000, "Bronze"),
    (5000, "Prata"),
    (7000, "Ouro"),
    (8000, "Platina"),
    (9000, "Ascendente"),
    (10000, "Imortal"),
]


def classificar_nivel(xp: int) -> str:
    """Retorna o nível do herói usando estruturas de decisão (if/elif/else)."""
    if xp < 0:
        raise ValueError("O XP não pode ser negativo.")

    if xp <= 1000:
        return "Ferro"
    elif xp <= 2000:
        return "Bronze"
    elif xp <= 5000:
        return "Prata"
    elif xp <= 7000:
        return "Ouro"
    elif xp <= 8000:
        return "Platina"
    elif xp <= 9000:
        return "Ascendente"
    elif xp <= 10000:
        return "Imortal"
    else:
        return NIVEL_FINAL


def classificar_nivel_por_laco(xp: int) -> str:
    """Versão alternativa: percorre a tabela FAIXAS com um laço (for).

    Mais fácil de manter: para mudar uma faixa basta editar FAIXAS.
    """
    if xp < 0:
        raise ValueError("O XP não pode ser negativo.")

    for limite, nivel in FAIXAS:
        if xp <= limite:
            return nivel
    return NIVEL_FINAL


def formatar_mensagem(nome: str, nivel: str) -> str:
    return f"O Herói de nome **{nome}** está no nível de **{nivel}**"


def ler_xp(mensagem: str) -> int:
    """Laço while que repete até o usuário digitar um XP válido."""
    while True:
        entrada = input(mensagem).strip().replace(".", "")
        if entrada.isdigit():
            return int(entrada)
        print("  ⚠️  Digite apenas números inteiros não negativos (ex.: 7500).")


def main() -> None:
    print("=" * 50)
    print("   ⚔️  CLASSIFICADOR DE NÍVEL DE HERÓI  ⚔️")
    print("=" * 50)

    herois = []  # lista para guardar o histórico da sessão

    while True:
        nome = input("\nNome do herói: ").strip()
        if not nome:
            print("  ⚠️  O nome não pode ficar vazio.")
            continue

        xp = ler_xp("XP do herói: ")
        nivel = classificar_nivel(xp)
        herois.append((nome, xp, nivel))

        print("\n" + formatar_mensagem(nome, nivel))

        outro = input("\nClassificar outro herói? (s/n): ").strip().lower()
        if outro != "s":
            break

    print("\n--- Resumo da sessão ---")
    for i, (nome, xp, nivel) in enumerate(herois, start=1):
        print(f"{i}. {nome:<15} XP: {xp:>6}  Nível: {nivel}")


if __name__ == "__main__":
    main()
