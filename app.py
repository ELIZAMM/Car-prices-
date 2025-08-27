import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar los datos
car_data = pd.read_csv('car_prices.csv')  

# Encabezado
st.header('Análisis de Venta de Coches')
st.write('Explora los datos de ventas y kilometraje de autos en México.')

# Mostrar histograma si se selecciona la casilla
if st.checkbox('Mostrar histograma de odómetro'):
    st.write('Histograma de odómetro')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

if st.checkbox('Mostrar gráfico de dispersión'):
    st.write('Gráfico de dispersión: odómetro vs precio')
    fig2 = px.scatter(car_data, x='odometer', y='sellingprice', title='Relación entre kilometraje y precio')
    st.plotly_chart(fig2, use_container_width=True)


#Preparar datos para gráfico de barras por bloques de 5 años
# Crear columna 'year_group' agrupando de 5 en 5 años
car_data['year_group'] = (car_data['year'] // 5) * 5
car_data['year_group'] = car_data['year_group'].astype(str) + '-' + (car_data['year_group'] + 4).astype(str)

# Agrupar por intervalos de 5 años
grouped_data = car_data.groupby('year_group')['sellingprice'].mean().reset_index()

# Botón para mostrar gráfico de barras por bloques de 5 años
if st.button('Mostrar precios promedio por grupos de 5 años'):
    fig = px.bar(grouped_data,
                 x='year_group',
                 y='sellingprice',
                 color='year_group',  # color por grupo para mejor visualización
                 title='Precio promedio de autos por grupos de 5 años',
                 labels={'year_group': 'Rango de años', 'sellingprice': 'Precio promedio ($)'},
                 height=500,
                 width=1000, 
                 color_discrete_sequence=px.colors.qualitative.Set3)  # paleta de colores
    
    st.plotly_chart(fig, use_container_width=True)



