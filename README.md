# Verificador de Consumo de Água

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
![Water](https://img.shields.io/badge/Sustentabilidade-%C3%81gua-00a8e8?style=for-the-badge&logo=waterdrop&logoColor=white)

## Sobre o Projeto

O Verificador de Consumo de Água é um script em Python desenvolvido para classificar e alertar os usuários sobre o seu consumo mensal de água (em m³), baseado no tipo de imóvel (Comercial, Casa ou Apartamento).

O sistema tem como objetivo promover a conscientização ambiental, indicando se o consumo está dentro do padrão, se é econômico ou se é excessivo.

---

## ⚙️ Regras de Negócio (Lógica do Sistema)

O programa analisa as entradas do usuário e classifica o consumo de acordo com as seguintes regras:

- **Comercial:** Tarifa corporativa aplicada independentemente do consumo.
- **Apartamento (Econômico):** Consumo menor que 10m³.
- **Apartamento ou Casa (Moderado):** Consumo de até 25m³.
- **Excedente / Outros Casos:** Qualquer consumo acima dos limites residenciais descritos é classificado como excessivo, alertando sobre possíveis vazamentos e a necessidade de adotar medidas de economia.

---

## Tecnologias e Conceitos Utilizados

- **Linguagem:** [Python 3](https://www.python.org/)
- **Estruturas de Controle:** Utilização da estrutura condicional moderna `match/case` combinada com *Guards* (`if`) para validações de múltiplas condições de forma limpa e otimizada.

