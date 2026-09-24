---
name: slug-review
description: Use when changing slugify behavior or fixing its edge cases (accents, punctuation, empty strings) to verify the output stays deterministic and the CLI examples stay in sync.
---
# Revisão de slugify

Quando você alterar `src/textkit/slug.py`, faça o seguinte antes de dar por
pronto:

1. Rode os casos de borda e confirme que a saída é determinística:
   - `slugify("Olá, mundo!")`
   - `slugify("  espaços  e  TAB\t")`
   - `slugify("")` → string vazia, sem erro
   - `slugify("café com leite")` → `cafe-com-leite`
   - `slugify("----")` → string vazia (tudo vira separador)
2. Atualize os exemplos em `README.md` e `AGENTS.md` se a saída mudar.
3. Rode a CLI de ponta a ponta: `python -m textkit.cli "Olá, mundo!"`.

A regra de ouro: entrada determinística → saída determinística.