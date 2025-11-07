import streamlit as st
from dataset import df
from utils import convert_csv,messagem_sucesso


st.title('Dataset de vendas ')

#uma condicao
# aqui criamaos tosos os filtros da outra page  
with st.expander('Colunas'):
    colunas = st.multiselect(
        'Selecione as Colunas',
        list(df.columns),
        list(df.columns)
        
        )
st.sidebar.title('Filtros')
with st.sidebar.expander('Cateoria do Produto'):
    categorias = st.multiselect( 
        'Selecione as categorias',
        df['Categoria do Produto'].unique(),
        df['Categoria do Produto'].unique()
        )

with st.sidebar.expander('Preço do Produto'):
    preco = st.slider(
        'Selecione o Preço',
         0, 5000,
        (0, 5000)

        )
with st.sidebar.expander('Data da Compra'):
    data_compra = st.date_input(
        'Selecione a data',
        (df['Data da Compra'].min(),
        df['Data da Compra'].max())
    )
# fim filtro 

#Criando auma query da categoria o filtro do menu
query = '''
    `Categoria do Produto` in @categorias and \
    @preco[0] <= Preço  <= @preco[1] and \
    @data_compra[0] <= `Data da Compra` <= @data_compra[1]
'''
#filtramos os registros da minha linha
filtro_dados = df.query(query)
# aqui filtramosos regiustros das minhas colunas 
filtro_dados = filtro_dados[colunas]

st.dataframe(filtro_dados)
# st.dataframe(df)

# aqui crimos a barra que aparece nas tabelas de numeros de linhas e colunas
st.markdown(f' A tabela possui :blue[{filtro_dados.shape[0]}] linhas e :blue[{filtro_dados.shape[1]}] colunas')


### aqui fizemos o dowload
st.markdown('Escreve um nome do arquivo')
coluna1, coluna2 = st.columns(2)
with coluna1:
    nome_aquivo = st.text_input(
        '',
        label_visibility='collapsed'
    )
    nome_aquivo +='.csv'

with coluna2 :
    st.download_button(
       'Baixar arquivo',
       data= convert_csv(filtro_dados),
       file_name=nome_aquivo,
       mime='text/csv',
       on_click=messagem_sucesso
)