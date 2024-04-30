import streamlit as st
import Utils as ut
from Controllers.LoginController import LoginDAO
import streamlit_antd_components as sac
from Controllers.PadraoController import *
   
# Página de login
def login_page():
    Apelido = None
    Password = None
    ut.Divisor('Gerenciador de Tarefas - Login', 'graph-up-arrow', 'rgb(20,80,90)', 'Login01')
    st.write('\n \n')
    # Linhas 
    row_1_col1, row_1_col2, row_1_col3 = st.columns([3, 3 ,3])  
    row_2_col1, row_2_col2, row_2_col3 = st.columns([4, 1 , 4])  
    row_3_col1, row_3_col2, row_3_col3 = st.columns([3, 3 , 3])  
    # Linha 01
    with row_1_col1:
        st.write('')
    with row_1_col2:
        # Entrada de texto para nome de usuário e senha
        Apelido = st.selectbox('Usuário', apelidos, key='Apelido', index=0, placeholder='Seleciona um usuário...')

        Password = st.text_input("Password", type="password", key="Password")
    with row_1_col3:
        st.write('')

    # Linha dos Botões
    with row_2_col1:
        st.write('')
    with row_2_col2:
        selected_login = sac.menu([
                sac.MenuItem(type='divider'),
                sac.MenuItem('Login', icon=sac.BsIcon(name='box-arrow-right', color='green')),
                sac.MenuItem(type='divider'),
                ], color='rgb(20,80,90)', open_all=False, return_index=False, index=None) 
          
    with row_2_col3:
        st.write('')
        
    with row_3_col1:
        st.write('')
    with row_3_col2:
        if selected_login == 'Login':
            if Apelido == None or Password == None:
                ut.Aviso('', 'Ops! Usuário ou Senha em branco')
            elif Apelido != None or Password != None:
                if LoginDAO.authenticator(Apelido, Password):
                    
                    st.session_state.Apelido_L = Apelido
                            
                    ut.fn_spinner_5(f'Aguarde... Carregando dados do Usuário "{Apelido}"')

                    # Aqui você pode redirecionar para outra página ou fazer outras ações após o login
                    st.session_state.logged_in = True  
                    st.rerun()                       
                    Main()       
                else:
                    ut.Erro('','Ops! Nome de usuário ou senha incorretos. Por favor, tente novamente.')
    with row_3_col3:
        st.write('')
            
    ut.Divisor('Copyright (c) 2024','', 'rgb(20,80,90)', 'Login02')