import pandas as pd
import matplotlib.pyplot as plt

# Carrega os DataFrames
pd.set_option('display.max_columns', None)
df_gols = pd.read_csv('gols_marcados.csv')
df_jogos = pd.read_csv('Jogos.csv')

# Realiza a junção dos DataFrames
df_merged = pd.merge(df_gols, df_jogos[['JOGO', 'VISITANTE']], on='JOGO', how='left')

# Filtra os dados para o jogador 'Roger Guedes'
jogador_roger_guedes = 'Roger Guedes'
df_roger_guedes = df_merged[df_merged['JOGADOR'] == jogador_roger_guedes]

# Agrupa os dados por adversário e calcula a contagem de gols correta
contagem_gols_por_adversario = df_roger_guedes.groupby('VISITANTE').size().reset_index(name='Total de Gols')

# Cria o gráfico de barras
plt.figure(figsize=(12, 6))  # Ajuste o tamanho da figura
bars = plt.bar(contagem_gols_por_adversario['VISITANTE'], contagem_gols_por_adversario['Total de Gols'])

# Adiciona os valores de cada gol em cima de cada barra
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.1, str(round(yval, 2)), va='bottom', ha='center')

# Adiciona rótulos e título
plt.xlabel('Adversário')
plt.ylabel('Total de Gols')
plt.title('Total de Gols Marcados por gênio da bola Roger Guedes')

# Exibe o gráfico
plt.xticks(rotation=45, ha='right')  # Ajuste a rotação e alinhamento dos rótulos do eixo x
plt.grid(True)
plt.tight_layout()
plt.show()
