import streamlit as st
from Controllers.PadraoController import *
import Utils as ut

def Form_ListarTarefa(pPrioridade, pCategoria):  
    
    ut.Divisor('Listar Tarefas', 'clipboard2-data', 'rgb(20,80,90)', 'ListarTarefa01')

    with st.container(border=True):
        # Chama a função listar_tarefas com os filtros selecionados
        df_filtrado = listar_tarefas(pPrioridade, pCategoria)

        # Mostra as tarefas filtradas em um DataFrame do Pandas
        if not df_filtrado.empty:
            st.dataframe(df_filtrado, hide_index=True)
        else:
            st.write("Não há tarefas correspondentes aos filtros selecionados.")
           
    ut.Divisor('Copyright (c) 2024','','rgb(20,80,90)', 'ListarTarefa02')