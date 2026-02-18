# Person and Pet Management API

API responsável pelo cadastro e gerenciamento de pessoas e seus respectivos pets.

O sistema foi desenvolvido com foco na aplicação de princípios de arquitetura
de software, priorizando organização, separação de responsabilidades
e evolução arquitetural consciente.

## 🎯 Objetivos do Projeto

- Aplicar princípios de arquitetura de software
- Separar responsabilidades entre camadas
- Utilizar interfaces para desacoplamento
- Organizar o código de forma evolutiva e compreensível
- Exercitar boas práticas sem rigidez excessiva

## 🧠 Visão Arquitetural

A arquitetura do projeto foi pensada para manter:
- Controllers responsáveis apenas por orquestração
- Camadas bem definidas entre entrada, validação e persistência
- Uso de interfaces para reduzir acoplamento
- Infraestrutura tratada como detalhe de implementação

O projeto não segue rigidamente um único modelo arquitetural,
mas se orienta por princípios como:
- Separação de responsabilidades
- Clareza estrutural
- Evolução incremental da arquitetura

## 🗂️ Estrutura do Projeto

- `controllers`: camada de entrada da aplicação
- `views`: responsabilidade de resposta HTTP
- `validators`: validações de entrada
- `models`: abstrações de persistência e entidades
- `errors`: tratamento centralizado de erros
- `main`: composição da aplicação e inicialização do servidor

## ⚖️ Considerações

Este projeto representa um estágio de aprendizado e evolução contínua.
Há pontos de melhoria e possíveis refinamentos arquiteturais,
que fazem parte do processo natural de amadurecimento técnico.

O objetivo principal é demonstrar raciocínio arquitetural,
não um modelo perfeito ou definitivo.
