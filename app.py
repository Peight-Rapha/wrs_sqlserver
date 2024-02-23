import streamlit as st
import pandas as pd
import pyodbc

def fetch_data():
    server = 'WINUEAPD49711\DEV01,25882'
    database = 'DB_PROJ_GPS'
    username = 'BR_PROJ_ORGANON'
    password = 'BRPROJORG49711@@'
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    query = """
    SELECT TOP (1000) [DATA]
          ,[DATA_CRIACAO]
          ,[DATA_MODIFICACAO]
          ,[CANAL]
          ,[MERCADO]
          ,[LABORATORIO]
          ,[MARCA]
          ,[ESPECIALIDADE]
          ,[CRM]
          ,[MEDICO]
          ,[POTENCIAL]
          ,[UNIDADES]
      FROM [DB_PROJ_GPS].[dbo].[BR_GPS_PRESCRIPTIONS]
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def main():
    st.title('Visualização de Dados do Banco de Dados')

    # Carregar dados
    data = fetch_data()

    # Mostrar os dados em uma tabela
    st.write(data)

if __name__ == "__main__":
    main()
