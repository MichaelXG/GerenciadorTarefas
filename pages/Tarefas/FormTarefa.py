import streamlit as st
from Controllers.PadraoController import *
import streamlit_antd_components as sac
import Utils as ut
from pages.Home.Create_Home import Create_Home 
    
def Form_Tarefa():  
    if "widget" not in st.session_state:
        st.session_state.widget = ""
   
    if 'nome' not in st.session_state:
        st.session_state.nome = ''
        
    if 'descricao' not in st.session_state:
        st.session_state.descricao = ''
    
    if 'prioridade' not in st.session_state:
        st.session_state.prioridade = None
        
    if 'categoria' not in st.session_state:
        st.session_state.categoria = None
 
    ut.Divisor('Adicionar Tarefas', 'clipboard-plus', 'rgb(20,80,90)', 'key_tarefa1')

    with st.form(key = 'form_tarefa', clear_on_submit = True):
        row_0_col1, row_0_col2, row_0_col3, row_0_col4 = st.columns([2, 2, 2, 2])  
        row_1_col1, row_1_col2 = st.columns([8, 0.01])  
        row_2_col1, row_2_col2, row_2_col3, row_2_col4, row_2_col5= st.columns([2, 2, 1, 2, 2]) 
        
         # Linha 00
        with row_0_col1:
            st.session_state.nome  = st.text_input('Nome da tarefa', key='key_nome')
            if not st.session_state.nome :
                st.error('O campo "Nome da tarefa" é Obrigatorio.')
                
        with row_0_col2:
            st.session_state.descricao = st.text_input('Desc. da tarefa', key='key_descricao')
            if not st.session_state.descricao:
                st.error('O campo "Desc. da tarefa" é Obrigatorio.')        
        
        with row_0_col3:
            st.session_state.prioridade = st.selectbox('Prioridade', prioridades, key='key_prioridade', index=None, placeholder='Seleciona a prioridade da tarefa...')
            if not st.session_state.prioridade:
                st.error('O campo "Categoria" é Obrigatorio.')
       
        with row_0_col4:
            st.session_state.categoria = st.selectbox('Categoria', categorias, key='key_categoria', index=None, placeholder='Seleciona a categoria da tarefa...')
            if not st.session_state.categoria:
                st.error('O campo "Categoria" é Obrigatorio.')
        
        with row_1_col1:
            sac.menu([sac.MenuItem(type='divider')], color='rgb(20,80,90)', open_all=False, return_index=False, index=None, key='key_divisor')
        with row_1_col2:   
            st.write('')

        with row_2_col1:   
            st.write('')
        
        with row_2_col2:
           st.write('')   
            
        with row_2_col3: 
            form_submit_button_tarefa = st.form_submit_button('Salvar')
            
        with row_2_col4: 
            st.write('') 
        
        with row_2_col5: 
            st.write('') 
            
        if form_submit_button_tarefa:
            if st.session_state.nome and st.session_state.descricao and st.session_state.prioridade and st.session_state.categoria:
                adicionar_tarefa(st.session_state.nome, st.session_state.descricao, st.session_state.prioridade, st.session_state.categoria)           
            else:
                ut.Alerta('','Parametros para incluir uma tarefa incompleto')   
    
    ut.Divisor('Copyright (c) 2024','','rgb(20,80,90)', 'key_tarefa2')