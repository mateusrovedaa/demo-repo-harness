# AGENTS.md

## Visão geral

`textkit` é um pequeno utilitário de texto em Python. Hoje ele faz uma coisa
só: transforma texto livre em slugs seguros para URL (`slugify`), com uma CLI
fininha por cima. Use-o como ponto de partida para aprender a construir um
harness em volta de um projeto real.

## Como rodar

```sh
# CLI
python -m textkit.cli "Olá, mundo! Como vai?"
# => ola-mundo-como-vai

# Biblioteca
python -c "from textkit import slugify; print(slugify('À procura de padrões'))"
```

Sem dependências de runtime: o pacote usa só a biblioteca padrão. Não é
necessário instalar nada para rodar.

## Estrutura

```
src/textkit/
  __init__.py   # exports públicos do pacote
  slug.py       # lógica de slugify (a função principal)
  cli.py        # ponto de entrada da linha de comando
```

## Convenções

- **Linguagem**: Python 3.11+. Tipos explícitos em assinaturas de função.
- **Idioma das mensagens**: mensagens de CLI e docstrings em português
  (o público do projeto é BR). Identificadores de código em inglês.
- **Sem novas dependências**: a biblioteca padrão resolve o problema. Antes de
  adicionar um pacote, pergunte se o problema realmente existe.
- **Mudanças de comportamento** em `slugify` devem manter a propriedade
  principal: entrada determinística → saída determinística, sempre.
- **Não commite** arquivos gerados, `.env` ou segredos.

## O que este repo NÃO é

Não é um projeto de produção. É um cenário de demonstração: o código foi
escrito primeiro e o harness (regras, testes, CI, hooks) está sendo
construído em volta dele, nível a nível. Cada nível tem uma tag (`l0`…`l4`).