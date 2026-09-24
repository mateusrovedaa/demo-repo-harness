# textkit

Pequeno utilitário de texto em Python: transforma texto livre em slugs
seguros para URL.

```sh
python -m textkit.cli "Olá, mundo!"
# ola-mundo
```

```python
from textkit import slugify

slugify("Receitas de Festa Junina")
# receitas-de-festa-junina
```

Sem dependências, só a biblioteca padrão.