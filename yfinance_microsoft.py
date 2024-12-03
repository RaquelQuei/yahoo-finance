import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

# Criação de um objeto Ticker para acessar informações detalhadas sobre a Microsoft (MSFT)
msft = yf.Ticker("MSFT")
# Baixa os dados históricos do ativo MSFT. O parâmetro 'period="max"' especifica o intervalo máximo disponível
msft_data = msft.history(period="max")
# Reseta o índice do DataFrame para transformar o índice padrão (datas) em uma coluna
msft_data.reset_index(inplace=True)

# Seleciona a coluna 'Date' (datas) do DataFrame para uso no eixo X do gráfico
data = msft_data['Date']
# Seleciona a coluna 'Close' (preços de fechamento) do DataFrame para uso no eixo Y do gráfico
fechamento = msft_data['Close']

# Criação de uma figura e eixos para o gráfico com tamanho personalizado
fig, ax = plt.subplots(figsize=(12, 8))
# Plota a série temporal de preços de fechamento com cor azul e legenda
ax.plot(data, fechamento, color='steelblue', label='MSFT - Fechamento')
# Define os rótulos dos eixos X e Y e o título do gráfico
ax.set(xlabel='Data', ylabel='Valor da ação (USD)',
       title='Série histórica de fechamento Microsoft (MSFT)')
# Adiciona uma grade com cor cinza claro e opacidade ajustada
ax.grid(color='lightgray', alpha=0.6)
# Exibe a legenda no gráfico
ax.legend()
# Salva o gráfico em um arquivo chamado 'test.png' com cortes nas bordas brancas
fig.savefig("serie_hist_microsoft.png", bbox_inches='tight')
# Mostra o gráfico na tela
plt.show()
