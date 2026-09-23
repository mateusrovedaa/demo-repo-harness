from textkit import slugify
from textkit.cli import main


def test_slugify_basico():
    assert slugify("Olá, mundo!") == "ola-mundo"


def test_slugify_acentos():
    assert slugify("Café com Leite") == "cafe-com-leite"


def test_slugify_vazio():
    assert slugify("") == ""


def test_slugify_apenas_separadores():
    assert slugify("----") == ""


def test_slugify_tab_e_espacos():
    assert slugify("  espaços  e  TAB\t") == "espacos-e-tab"


def test_cli_sem_argumentos(capsys):
    assert main([]) == 2
    assert "uso:" in capsys.readouterr().err


def test_cli_com_argumento(capsys):
    assert main(["Olá, mundo!"]) == 0
    assert capsys.readouterr().out == "ola-mundo\n"
