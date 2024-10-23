import streamlit as st
import pandas as pd

def cargar_contagios():
    data =pd.read_excel('streamlitcovid.xlsx',sheet_name ='contagios')
    return data
def cargar_departamentos():
    data =pd.read_excel('streamlitcovid.xlsx',sheet_name ='departamentos')
    return data
df_contagios = cargar_contagios()
df_departamentos = cargar_departamentos()