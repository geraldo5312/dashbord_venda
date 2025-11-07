import streamlit as st
import plotly.express as px
from dataset import df
#importar funcao da formatação numeeros 
from utils import format_number
#importar grafico da pagina grafico
from grafico import grafico_map_estados, grafico_rec_mensal, grafico_rec_estado, grafico_rec_categoria, grafico_rec_vendedores

st.set_page_config( layout="wide")
st.title("Dashboard de Vendas :shopping_cart:")

#sidebar filtro vendedor
st.sidebar.title(' Filtro de Vendedores ')
filtro_vendedor = st.sidebar.multiselect(
    'Vendedores',
    df['Vendedor'].unique()
)
# se o evendedor esta contindo , dentro de onde os selecionado
if filtro_vendedor:
    df=df[df['Vendedor'].isin(filtro_vendedor)]



# Criando abas 

abas1,abas2,abas3 = st.tabs(['Dataset','Receitas','Vendedoras'])

#aqui vamos colocar valores em casa abas 

with abas1:
    st.dataframe(df)

with abas2:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.metric('Receita total', format_number(df['Preço'].sum(), 'kz') )
        #aqui passamos o grafico 
        st.plotly_chart(grafico_map_estados, use_container_width=True)
        st.plotly_chart(grafico_rec_estado, use_container_width=True)
    with coluna2:
        st.metric('Quantitdade de Vendas', format_number(df.shape[0])) # aqui pegamos total de vendas 
        st.plotly_chart(grafico_rec_mensal, use_container_width=True)
        st.plotly_chart(grafico_rec_categoria, use_container_width=True)

with abas3:
    coluna1,coluna2 = st.columns(2)
    with coluna1:
        st.plotly_chart(grafico_rec_vendedores, use_container_width=True)