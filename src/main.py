import pandas as pd

def main():
    df = pd.read_csv("data/ecommerce_estatistica.csv")

    print("\n===== PRIMEIRAS LINHAS =====")
    print(df.head())

    print("\n===== INFORMAÇÕES =====")
    print(df.info())

    print("\n===== ESTATÍSTICAS =====")
    print(df.describe())

if __name__ == "__main__":
    main()