# Gestor Financeiro Pessoal

Um sistema interativo de gerenciamento financeiro via terminal construído 100% em Python. 

Este projeto foi desenvolvido do zero para aplicar e consolidar conceitos estruturais de Programação Orientada a Objetos (POO), tratamento de erros e persistência de arquivos.

## Funcionalidades

* **Cadastro de Movimentações:** Adicione receitas e despesas com descrição, valor e categoria.
* **Cálculo de Saldo Automático:** O sistema atualiza seu saldo dinamicamente com base nas entradas.
* **Extrato Detalhado:** Histórico completo e formatado de todas as transações cadastradas.
* **Persistência de Dados (JSON):** Suas transações são salvas automaticamente em um arquivo `dados.json`. Nada é perdido ao fechar o programa.
* **UX e Validação Segura:** Sistema blindado contra erros de digitação (ex: digitar letras no lugar de números) utilizando `try/except` e validações com `@property`.

## Tecnologias e Conceitos Aplicados

* **Python 3**
* **Programação Orientada a Objetos (POO):** Criação de Classes, Instanciamento de Objetos, Encapsulamento de atributos.
* **Manipulação de Arquivos:** Leitura e escrita de arquivos `.json` nativo do Python.
* **Modularização:** Arquitetura dividida em responsabilidades (`main.py` para a interface, `gerenciador.py` para a regra de negócio, `transacao.py` para o modelo de dados).

## Como Executar o Projeto

1. Clone este repositório:
   ```bash
   git clone [https://github.com/victorlopes-cmyk/GESTOR-FINANCEIRO.git](https://github.com/victorlopes-cmyk/GESTOR-FINANCEIRO.git)
