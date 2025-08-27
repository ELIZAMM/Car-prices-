import streamlit as st
import pandas as pd
import plotly.express as px


car_data = pd.read_csv('../car_prices.csv') # leer los datos

st.header('Análisi de venta de autosmoviles') #Titulo de la app