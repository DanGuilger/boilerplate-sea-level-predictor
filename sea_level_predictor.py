import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    # carrego os dados do csv com as informacoes de nivel do mar de 1880 ate 2013
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    # crio uma figura e faco um scatter plot com os pontos dos dados reais
    # cada ponto representa um ano e o nivel do mar correspondente
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    # calculo a regressao linear usando todos os dados historicos (1880-2013)
    # isso me da a inclinacao e interseccao da linha de tendencia
    slope1, intercept1, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    # estendo a previsao ate 2050 usando a formula da linha reta
    years_extended = range(1880, 2051)
    line1 = [slope1 * year + intercept1 for year in years_extended]
    plt.plot(years_extended, line1, 'r', label='Best fit line (1880-2050)')

    # Create second line of best fit
    # agora faco outra regressao so com dados mais recentes (de 2000 pra frente)
    # isso mostra se a tendencia mudou nos ultimos anos
    df_recent = df[df['Year'] >= 2000]
    slope2, intercept2, r_value, p_value, std_err = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = range(2000, 2051)
    line2 = [slope2 * year + intercept2 for year in years_recent]
    plt.plot(years_recent, line2, 'g', label='Best fit line (2000-2050)')

    # Add labels and title
    # adiciono os labels e titulo que os testes esperam
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()