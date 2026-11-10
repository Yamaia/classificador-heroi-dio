# ⚔️ Classificador de Nível de Herói

Projeto do desafio da **DIO** que classifica um herói em um nível (de *Ferro* a *Radiante*) de acordo com a sua quantidade de experiência (XP).

Desenvolvido por Yamaia, desenvolvedor Python, como parte do meu portfólio no GitHub.

## 🎯 Objetivo

Armazenar o **nome** e o **XP** de um herói e, com estruturas de decisão, exibir:

```
O Herói de nome **{nome}** está no nível de **{nivel}**
```

## 🧠 Conceitos aplicados

| Conceito | Onde aparece |
|---|---|
| **Variáveis** | `nome`, `xp`, `nivel`, lista `herois`, constantes `FAIXAS` e `NIVEL_FINAL` |
| **Operadores** | comparação (`<=`, `<`), lógico (`not`), atribuição, f-strings e formatação |
| **Estruturas de decisão** | `if / elif / else` em `classificar_nivel` |
| **Laços de repetição** | `while` (menu e validação de entrada) e `for` (tabela de faixas, resumo) |

## 📊 Tabela de níveis

| XP | Nível |
|---|---|
| até 1.000 | Ferro |
| 1.001 a 2.000 | Bronze |
| 2.001 a 5.000 | Prata |
| 5.001 a 7.000 | Ouro |
| 7.001 a 8.000 | Platina |
| 8.001 a 9.000 | Ascendente |
| 9.001 a 10.000 | Imortal |
| 10.001 ou mais | Radiante |

> **Decisão de projeto:** o enunciado diz "menor que 1.000" para Ferro e começa Bronze em 1.001, deixando exatamente **1.000** sem regra. Optei por incluir 1.000 em **Ferro**, para que todas as faixas sejam contínuas (cada nível vai até o seu limite superior, inclusive).

## 🗂️ Estrutura

```
classificador-heroi-dio/
├── src/
│   └── classificador.py      # código principal
├── tests/
│   └── test_classificador.py # testes automatizados
├── .gitignore
└── README.md
```

## ▶️ Como executar

Requisito: Python 3.8+ (sem dependências externas).

```bash
git clone https://github.com/<seu-usuario>/classificador-heroi-dio.git
cd classificador-heroi-dio
python src/classificador.py
```

### Exemplo de uso

```
==================================================
   ⚔️  CLASSIFICADOR DE NÍVEL DE HERÓI  ⚔️
==================================================

Nome do herói: Aragorn
XP do herói: 7.500

O Herói de nome **Aragorn** está no nível de **Platina**

Classificar outro herói? (s/n): n

--- Resumo da sessão ---
1. Aragorn         XP:   7500  Nível: Platina
```

## ✅ Testes

```bash
python -m unittest discover -s tests -v
```

Os testes cobrem todos os **valores de fronteira** (999, 1000, 1001, 2000, 2001 etc.), XP negativo e o formato da mensagem final.

## 🔍 Como funciona

1. **`classificar_nivel(xp)`** – cadeia `if/elif/else` que compara o XP com o limite de cada faixa, do menor para o maior; o primeiro teste verdadeiro define o nível.
2. **`classificar_nivel_por_laco(xp)`** – versão alternativa que percorre a lista `FAIXAS` com `for`, evitando repetição e facilitando mudanças nas regras.
3. **`ler_xp()`** – `while True` que só sai quando a entrada é um inteiro válido (aceita `7.500` com ponto de milhar).
4. **`main()`** – menu em laço que permite classificar vários heróis e mostra um resumo no final.

## 🚀 Ideias de evolução

- Salvar o histórico de heróis em arquivo JSON/CSV
- Barra de progresso até o próximo nível
- Interface web com FastAPI + React
- Cores no terminal com `rich`

## 📚 Aprendizados

- Importância de definir **casos de fronteira** nas regras de negócio
- Diferença entre `if/elif` e abordagem orientada a dados (tabela + laço)
- Validação de entrada do usuário e testes automatizados com `unittest`

## 🔗 Referências

- [Desafio DIO](https://www.dio.me/)
- [Documentação Python](https://docs.python.org/3/)
