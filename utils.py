from dataset import df
import pandas as pd
import streamlit as st
import time

# criamos a funcao de formatar o numeros 
def format_number(value, prefix =''):

    for unit in ['', 'mil']:
        if value < 1000:
            return f'{prefix} {value:.2f} {unit}'
        value /= 1000
    return f'{prefix} {value:.2} milhões'

# 1 aqui uma funcao para o grafico agrupamos pelo local o somatorio do preco  Dataframe por estado
df_rec_estado = df.groupby('Local da compra')[['Preço']].sum()
# Eliminar registro duplicado
df_rec_estado = df.drop_duplicates(subset='Local da compra')[['Local da compra','lat','lon']].merge(df_rec_estado, left_on='Local da compra', right_index=True).sort_values('Preço',ascending=False) 


#print(df_rec_estado)

# 2 Dataframe Receita Mensal
# Quando colocamos o index e so para puchar pela data nao pelo id 
df_rec_mensal = df.set_index('Data da Compra').groupby(pd.Grouper(freq='M'))['Preço'].sum().reset_index()
# aqui e para pegar o ano
df_rec_mensal['Ano']= df_rec_mensal['Data da Compra'].dt.year
# aqui e para pegar o mes 
df_rec_mensal['Mes']= df_rec_mensal['Data da Compra'].dt.month_name()

# 3 Dataframe Receita por categorias 
df_rec_Categorias = df.groupby('Categoria do Produto')[['Preço']].sum().sort_values('Preço', ascending=False)

# 4 Dataframe de vendedor, performa 
# vamos ter contagem e soma ao mesmo tempo
df_vendedores = pd.DataFrame(df.groupby('Vendedor')['Preço'].agg(['sum','count']))


# dowload funcão para converter arquivo CSV

@st.cache_data
def convert_csv(df):
    return df.to_csv(index=False).encode('utf-8')

def messagem_sucesso():
    success = st.success(
        'Arquivo baixado com sucesso',
        
    )
    time.sleep(3)
    success.empty()