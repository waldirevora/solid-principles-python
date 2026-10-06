# SOLID Principles Python

Projeto desenvolvido como desafio prático da Rocketseat para aplicar princípios SOLID em Python.

O exercício trabalha dois princípios:

- SRP, Single Responsibility Principle
- OCP, Open Closed Principle

## SRP

O exemplo de SRP foi reorganizado para separar responsabilidades que estavam concentradas em uma única classe.

Foram criadas classes específicas para:

- conexão com API;
- gerenciamento de tarefas;
- envio de notificações;
- geração e envio de relatórios.

Cada classe ficou responsável por uma parte específica do sistema.

## OCP

O exemplo de OCP foi refatorado para permitir a criação de novos tipos de exame sem alterar a classe responsável pela aprovação.

A classe abstrata `Exame` define o método `verificar_condicoes()`.

Os tipos `ExameSangue` e `ExameRaioX` implementam esse método de acordo com o contrato definido.

A classe `AprovaExame` trabalha com essa abstração e não precisa verificar diretamente qual tipo de exame recebeu.

## Estrutura

```text
solid-principles-python
├── 1_S_SRP
│   └── srp_bad_example.py
├── 2_O_OCP
│   └── ocp_bad_example.py
├── .gitignore
└── README.md
```

## Execução

Para executar o exemplo de OCP:

```bash
python ./2_O_OCP/ocp_bad_example.py
```

Saída esperada:

```text
Exame aprovado!
Exame aprovado!
```

## Validação

A sintaxe dos arquivos foi validada com:

```bash
python -m py_compile ./1_S_SRP/srp_bad_example.py
python -m py_compile ./2_O_OCP/ocp_bad_example.py
```
