import streamlit as st
import streamlit_antd_components as sac
import Utils as ut
import pages.Tarefas.FormTarefa as ft  
import pages.Tarefas.FormPesquisaTarefa as fpt  
import pages.Tarefas.FormConcluirTarefa as fct   
from pages.Home.Create_Home import Create_Home    
from pages.Login.Login import login_page    
from Controllers.PadraoController import *  

def Main():
    # Limpar os parâmetros necessários aqui
    # Por exemplo, você pode limpar os parâmetros da sessão do Streamlit:
    st.session_state.nome = ''
    st.session_state.descricao = ''
    st.session_state.prioridade = None
    st.session_state.categoria = None
    
    # Menu
    with st.sidebar:
        st.image('https://blog.runrun.it/wp-content/uploads/2022/05/117960-blog.jpg.webp', width=None, use_column_width='auto') 
        selected_usu = sac.menu([
            sac.MenuItem(f'Bem-vindo, "{st.session_state.Apelido_L}"!', icon=sac.BsIcon(name='person-bounding-box', color='rgb(20,80,90)')),   
            # Usuário Logado
            sac.MenuItem(type='divider'),
            sac.MenuItem('Logout', icon=sac.BsIcon(name='box-arrow-left', color='red')),
            sac.MenuItem(type='divider'),
        ], color='rgb(20,80,90)', open_all=False, return_index=False, index=0, key='Menu_login')
    
    if selected_usu == 'Logout':
        st.session_state.logged_in = False
        st.rerun()  
          
    with st.sidebar:
        selected = sac.menu([
            sac.MenuItem('Menu Principal', icon=sac.BsIcon(name='person-bounding-box', color='rgb(20,80,90)')),   
             # Empresa
            sac.MenuItem(type='divider'),
            sac.MenuItem('Nova Tarefa',  icon=sac.BsIcon(name='clipboard-plus', color='rgb(20,80,90)'), description='Adicionar nova tarefa'),
            # Clientes
            sac.MenuItem(type='divider'),
            sac.MenuItem('Listar Tarefas', icon=sac.BsIcon(name='clipboard2-data', color='rgb(20,80,90)'), description='Lisar as tarefas'),
            # Veículos
            sac.MenuItem(type='divider'),
            sac.MenuItem('ConcluIr Tarefa', icon=sac.BsIcon(name='clipboard-check', color='rgb(20,80,90)'), description='Concluír as tarefas'),
        ], color='rgb(20,80,90)', open_all=False, return_index=False, index=0, key='Menu_principal')
    
    if selected == 'Menu Principal':
        Create_Home()
    elif selected == 'Nova Tarefa':
        if __name__ == "__main__":
            ft.Form_Tarefa()
    elif selected == 'Listar Tarefas':
         if __name__ == "__main__":
            fpt.Form_PesquisaTarefa()  
    elif selected == 'ConcluIr Tarefa':
        if __name__ == "__main__":
            fct.Form_Concluir()   
          
# Lógica para alternar entre as páginas com base na ação do usuário
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
 
st.set_page_config(
    page_title="Tarefas",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded"
)   
        
if __name__ == "__main__":
    if st.session_state.logged_in:        
        Main()
    else:
        opcao = st.radio("Escolha uma opção:", ["Login"], horizontal= True)
        if opcao == "Login":
            if __name__ == "__main__":
                login_page()
