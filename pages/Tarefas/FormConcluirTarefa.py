import streamlit as st
from Controllers.PadraoController import *
from datetime import datetime
import streamlit_antd_components as sac
import Utils as ut
import pages.Tarefas.FormListarTarefa as flt  

def Form_Concluir():  
    
    ut.Divisor('Concluir Tarefas', 'clipboard-check', 'rgb(20,80,90)', 'ConcluirTarefa01')
    with st.container(border=True):
        row_0_col1, row_0_col2, row_0_col3= st.columns([1, 1, 2]) 
        
        df_filtrado_qtd = listar_tarefas('Todas', 'Todas', 'Não') 
        p_max_value = len(df_filtrado_qtd)
        
        with row_0_col1:
            numero_tarefa = st.number_input("ID Tarefa", min_value=1, max_value=p_max_value)
           
        with row_0_col2:
             selected_tarefa_concluir = sac.buttons([
                 sac.ButtonsItem(label='Concluir', icon='clipboard-check', color='#25C3B0'),
                 ], label=' . ', align='center', radius='lg', color='rgb(20,80,90)', index=None)
        
        with row_0_col3:
            st.write("")
                    
        ut.Divisor('Listar Tarefas', 'clipboard2-data', 'rgb(20,80,90)', 'ConcluirTarefa02')
        with st.container(border=True):
            # Chama a função listar_tarefas com os filtros selecionados
            df_filtrado = listar_tarefas('Todas', 'Todas', 'Não')

            # Mostra as tarefas filtradas em um DataFrame do Pandas
            if not df_filtrado.empty:
                st.dataframe(df_filtrado, use_container_width=True)
            else:
                st.write("Não há tarefas correspondentes para ser concluida.")   
       
    if selected_tarefa_concluir == 'Concluir':
        marcar_como_concluida(numero_tarefa)
        
    ut.Divisor('Copyright (c) 2024','','rgb(20,80,90)', 'ConcluirTarefa03')