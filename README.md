# Health Insurance Cross Sell

<b>AVISO:</b> Todos os problemas e premissas contextualizados no projeto são fictícios. Seu único objetivo é dar sentido para o desenvolvimento da solução.
Os dados estão disponíveis no site do kaggle através do link: https://www.kaggle.com/anmolkumar/health-insurance-cross-sell-prediction
<br><br>

## 1. Problema de negócio.
A Insurance All é uma empresa que fornece seguro de saúde para seus clientes e o time de produtos está analisando a possibilidade de oferecer aos assegurados, um novo produto: Um seguro de automóveis.

Assim como o seguro de saúde, os clientes desse novo plano de seguro de automóveis precisam pagar um valor anualmente à Insurance All para obter um valor assegurado pela empresa, destinado aos custos de um eventual acidente ou dano ao veículo.

A Insurance All fez uma pesquisa com cerca de 380 mil clientes sobre o interesse em aderir a um novo produto de seguro de automóveis, no ano passado. Todos os clientes demonstraram interesse ou não em adquirir o seguro de automóvel e essas respostas ficaram salvas em um banco de dados junto com outros atributos dos clientes.

O time de produtos selecionou 127 mil novos clientes que não responderam a pesquisa para participar de uma campanha, no qual receberão a oferta do novo produto de seguro de automóveis. A oferta será feita pelo time de vendas através de ligações telefônicas.

Contudo, o time de vendas tem uma capacidade de realizar 20 mil ligações dentro do período da campanha.
<br><br>

## 2. Premissas de negócio.
Por enquanto, ainda não foi assumido nenhuma premissa de negócio.
<br><br>
### 2.1. Sobre os dados
| Atributos                        | Descrição                                                    |
| -------------------------------- | ------------------------------------------------------------ 
| id                               | ID único para o cliente 
| gender                           | Gênero do cliente
| age                              | Idade do cliente
| region_code                      | Código único para a região do cliente
| policy_sales_channel             | Código para o canal de venda ao cliente, ou seja. Agentes diferentes, por correio, por telefone, pessoalmente, etc.
| driving_license                  | 0: O cliente não tem habilitação, 1: O cliente já tem habilitação
| vehicle_age                      | Idade do veículo
| vehicle_damage                   | 1: O cliente teve seu veículo danificado no passado. 0: O cliente não teve seu veículo danificado no passado.
| previously_insured               | 1: O cliente já tem seguro de veículos, 0: o cliente não tem seguro de veículos
| annual_premium                   | O valor que o cliente precisa de anuidade no seguro
| vintage                          | Número de dias que o cliente esteve associado à seguradora
| response                         | 1: O cliente está interessado, 0: O cliente não está interessado
<br><br>

## 3. Estratégia de solução
O projeto foi desenvolvido através do método CRISP-DM, aplicando os seguintes passos:

**Passo 01 - Descrição dos Dados:** Nessa etapa, o objetivo foi conhecer os dados, seus tipos, analisar métricas estatísticas básicas como: média, mediana, máximo, mínimo, range, skew, kurtosis e desvio padrão. Foi analisado também o balanceamento dos dados, onde é possível identificar que apenas 12.26% de todos os clientes da base possuem interesse na contratação do seguro.

**Passo 02 - Feature Engineering:** 

**Passo 03 - Filtragem de Variáveis:** 

**Passo 04 - Análise Exploratória de Dados:** 

**Passo 05 - Preparação dos Dados:** 

**Passo 06 - Seleção de Variáveis:** 

**Passo 07 - Machine Learning Modeling:** 

**Passo 08 - Hyperparameter Fine Tunning:** 

**Passo 09 - Tradução e Interpretação do Erro:** 

**Passo 10 - Deploy do Modelo em Produção:** 
<br><br>

## 4. Top Insights
<br><br>

## 5. Modelos de de Machine Learning utilizados
<br><br>

## 6. Performance
<br><br>
### 6.1. Performance - Sem Cross Validation
<br><br>
### 6.2. Performance - Com Cross Validation
<br><br>
### 6.3. Performance - Final
<br><br>

## 7. Performance de negócio
<br><br>

## 8. Conclusão
<br><br>

## 9. Lições aprendidas
<br><br>

## 10. Próximos passos