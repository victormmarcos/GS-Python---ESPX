# BlueGuard - Monitoramento da Qualidade da Água

## Integrantes do Projeto

- Nome: Victor Magdaleno Marcos - RM 556729
- Nome: Arthur Bueno de Oliveira - RM 558396
  
## Descrição do Projeto
BlueGuard é um projeto voltado para o monitoramento da qualidade da água em regiões costeiras. Utilizando sensores simulados em Python, o projeto visa fornecer informações em tempo real sobre a qualidade da água, ajudando a proteger a vida marinha e a sustentabilidade costeira.

## Funcionalidades
- Coleta de dados simulados de qualidade da água.
- Análise de dados coletados para calcular métricas relevantes (média, máximo, mínimo).
- Geração de alertas com base nos dados analisados.

## Instruções de Uso

### Configuração do Python
1. Certifique-se de ter o Python instalado na sua máquina.
2. Faça o download do arquivo `monitoramento.py`.
3. Abra um terminal ou prompt de comando e navegue até o diretório onde o arquivo está salvo.
4. Execute o comando `python monitoramento.py`.

## Requisitos
- Python 3.x

## Estrutura do Código
- `coleta_dados(num_pontos)`: Função que coleta dados simulados de qualidade da água.
- `analisa_dados(phs, temperaturas, turbidezes)`: Função que analisa os dados coletados e retorna métricas relevantes.
- `gera_alertas(ph_medio, temperatura_media, turbidez_media)`: Função que gera alertas com base nas métricas analisadas.
- `main()`: Função principal que coordena a coleta, análise e alerta dos dados.

## Dependências
- Nenhuma dependência externa.

## Informações Adicionais
Este projeto pode ser expandido para integrar sensores reais e interfaces de usuário para visualização dos dados.
