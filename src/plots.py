import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

# 1. HISTOGRAMA 
def grafico_histograma(df):
    sns.histplot(df["Preço"])
    plt.title("Distribuição dos preços")
    plt.show()

# 2. GRÁFICO DE DISPERSÃO
def grafico_dispersao(df):
    sns.scatterplot(data=df, x="Preço", y="Nota")
    plt.title("Dispersão: Preço vs Nota")
    plt.show()

# 3. MAPA DE CALOR (correlação)
def grafico_heatmap(df):
    corr = df.corr(numeric_only=True)
    sns.heatmap(corr, annot=True)
    plt.title("Mapa de calor das correlações")
    plt.show()

# 4. GRÁFICO DE BARRAS
def grafico_barras(df):
    df["Marca"].value_counts().head(10).plot(kind="bar")
    plt.title("Top 10 marcas com mais produtos")
    plt.show()

# 5. GRÁFICO DE PIZZA
def grafico_pizza(df):
    df["Gênero"].value_counts().plot(kind="pie", autopct="%1.1f%%")
    plt.title("Distribuição por gênero")
    plt.ylabel("")
    plt.show()

# 6. GRÁFICO DE DENSIDADE
def grafico_densidade(df):
    sns.kdeplot(df["Preço"], fill=True)
    plt.title("Densidade de preços")
    plt.show()

# 7. GRÁFICO DE REGRESSÃO
def grafico_regressao(df):
    sns.regplot(data=df, x="Preço", y="Nota")
    plt.title("Regressão: Preço vs Nota")
    plt.show()