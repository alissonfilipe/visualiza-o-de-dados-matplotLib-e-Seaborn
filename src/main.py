import pandas as pd
from plots import (
    grafico_histograma,
    grafico_dispersao,
    grafico_heatmap,
    grafico_barras,
    grafico_pizza,
    grafico_densidade,
    grafico_regressao
)

def main():
    df = pd.read_csv("data/ecommerce_estatistica.csv")
    df = df.drop(columns=["Unnamed: 0"])

    grafico_histograma(df)
    grafico_dispersao(df)
    grafico_heatmap(df)
    grafico_barras(df)
    grafico_pizza(df)
    grafico_densidade(df)
    grafico_regressao(df)

if __name__ == "__main__":
    main()