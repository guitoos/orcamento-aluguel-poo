# Orçamento de Aluguel (POO)

Sistema em Python que gera o orçamento de aluguel de uma imobiliária fictícia (R.M Imóveis), aplicando regras de negócio com Programação Orientada a Objetos e exportando as 12 parcelas em CSV.

Projeto da disciplina Algorithmic Thinking & Introduction to Object-Oriented Programming, do curso de Análise e Desenvolvimento de Sistemas da UniFECAF.

## Regras de negócio

| Tipo | Valor base | Adicionais |
| --- | --- | --- |
| Apartamento | R$ 700 | 2 quartos: +R$ 200 · garagem: +R$ 300 · sem crianças: 5% de desconto |
| Casa | R$ 900 | 2 quartos: +R$ 250 · garagem: +R$ 300 |
| Estúdio | R$ 1.200 | 2 vagas: +R$ 250 · cada vaga extra: +R$ 60 |

O contrato imobiliário (R$ 2.000) pode ser parcelado em até 5 vezes e é cobrado apenas nas primeiras parcelas do orçamento.

## Como executar

```bash
python aluguel.py
```

Responda às perguntas no terminal. O arquivo `parcelas_orcamento.csv` é gerado com aluguel, contrato e total de cada mês (separador `;`, pronto para abrir no Excel).

## Conceitos aplicados

- Classe `Imovel` encapsulando as regras de cálculo
- Validação de todas as entradas do usuário
- Constantes para valores de negócio
- Exportação de dados em CSV

## Autor

Guilherme Oliveira · [LinkedIn](https://www.linkedin.com/in/guilhermeoss)
