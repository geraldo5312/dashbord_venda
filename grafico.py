import plotly.express as px

from utils import df_rec_estado, df_rec_mensal, df_rec_Categorias, df_vendedores

# trabalhamos com grafico de mapa 
grafico_map_estados = px.scatter_geo(
    df_rec_estado,
    lat='lat',
    lon='lon',
    scope='south america',
    size='Preço',
    template='seaborn',
    hover_name='Local da compra',
    hover_data={'lat': False, 'lon' : False},
    title='Receitas por Estados'

)


#grafico 2 , receitas do mes 
grafico_rec_mensal = px.line(
    df_rec_mensal,
    x = 'Mes',
    y = 'Preço',
    markers=True,
    range_y=(0,df_rec_mensal.max()),
    color='Ano',
    line_dash='Ano',
    title='Receitas Mensal'
)
grafico_rec_mensal.update_layout(yaxis_title ='Receita')

 # head pega os primeiro 5,  Tail pega os ultimos 5 registo
    # aqui pegamos os 5 estados top
grafico_rec_estado = px.bar(  
    df_rec_estado.head(5),
    x='Local da compra',
    y='Preço',
    text_auto=True,
    title='Top Receita por Estados'
)

grafico_rec_categoria = px.bar(
    df_rec_Categorias.head(7),
    text_auto=True,
    title='Top 7 Categoria com Maior Receita'
)

grafico_rec_vendedores = px.bar(
    df_vendedores[['sum']].sort_values('sum', ascending=False).head(7),
    x='sum',
    y=df_vendedores[['sum']].sort_values('sum', ascending=False).head(7).index,
    text_auto=True,
    title='Top 7 vendedores por Receitas'
)