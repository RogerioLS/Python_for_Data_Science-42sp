# Plano de Revisão - Módulo 00 (Starting)

Este documento centraliza as etapas de revisão e validação dos exercícios implementados. Siga este guia para garantir que cada exercício atenda aos critérios da École 42 antes da submissão.

## 🏁 Exercícios Implementados

- [x] **ex00 a ex05**: Já concluídos.
- [x] **ex06**: `ft_filter.py` & `filterstring.py`
- [x] **ex07**: `sos.py`
- [x] **ex08**: `Loading.py`
- [x] **ex09**: `ft_package`

---

## 🛠️ Guia de Revisão por Exercício

### [ex06] ft_filter & filterstring
- [ ] **ft_filter.py**: A docstring é idêntica ao `filter.__doc__` original?
- [ ] **filterstring.py**: O programa usa obrigatoriamente uma *list comprehension* e uma *lambda*?
- [ ] **Erro**: `python3 filterstring.py` sem argumentos imprime `AssertionError: the arguments are bad`?
- [ ] **Erro**: Tipos errados (ex: trocar ordem de string/int) disparam o erro correto?

### [ex07] Dictionaries SoS
- [ ] **Dicionário**: O nome da variável é `NESTED_MORSE`?
- [ ] **Formato**: Espaços viram `/` e caracteres Morse são separados por espaço simples?
- [ ] **Erro**: Caracteres não alfanuméricos (como `$`, `@`, `#`) disparam `AssertionError: the arguments are bad`?
- [ ] **Norma**: Passou no `flake8`?

### [ex08] Loading... (A ser implementado)
- [ ] **Funcionalidade**: A função `ft_tqdm` usa o operador `yield`?
- [ ] **Interface**: A aparência da barra de progresso é o mais próxima possível do `tqdm` original?
- [ ] **Configuração**: O código lida com o tamanho do terminal (`get_terminal_size`)?

### [ex09] My first package (A ser implementado)
- [ ] **Estrutura**: Possui `pyproject.toml`, `README.md` e `LICENSE`?
- [ ] **Instalação**: O comando `pip install ./dist/ft_package-0.0.1.tar.gz` funciona?
- [ ] **Metadados**: `pip show -v ft_package` exibe as informações corretas (Autor, License, etc)?

---

## 🚨 Checklist Geral (Padrão 42)
- [ ] Todas as funções têm `__doc__`?
- [ ] Não há código no escopo global (tudo dentro de `main()`)?
- [ ] Todas as exceções estão sendo tratadas (sem crashes brutos)?
- [ ] O comando `flake8 .` retorna 0 erros?
- [ ] O `README.md` e `notes.md` de cada pasta foram atualizados?
