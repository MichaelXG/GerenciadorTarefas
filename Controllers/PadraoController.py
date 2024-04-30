'''
Class for do PadraoController
'''
import random
# criar lista de Login
login = []

login = [{"Apelido":'Suporte',"Password": '123'},
         {"Apelido":'Visitante',"Password": 'visitante123'},
         {"Apelido":'Maria',"Password": 'Maria@123'}
        ]
apelidos = ['Suporte', 'Visitante', 'Maria']

# Lista para armazenar as tarefas
tarefas = []

tarefas = [{"Nome":'Mercado',"Descrição": 'Comprar itens de limpeza',"Prioridade": 'Média',"Categoria": 'Casa',"Concluída": False},
           {"Nome":'Farmacia',"Descrição": 'Comprar desloratadina',"Prioridade": 'Alta',"Categoria": 'Saúde',"Concluída": False},
           {"Nome":'Horti',"Descrição": 'Comprar legumes',"Prioridade": 'Alta',"Categoria": 'Casa',"Concluída": False},
           {"Nome":'Python',"Descrição": 'Concluir o Projeto',"Prioridade": 'Alta',"Categoria": 'Estudo',"Concluída": False},
           {"Nome":'Daily',"Descrição": 'Daily com o time geral',"Prioridade": 'Média',"Categoria": 'Trabalho',"Concluída": False},
           {"Nome":'Tiros',"Descrição": 'Ir ao clube de tiro para manter habitualizade',"Prioridade": 'Média',"Categoria": 'Lazer',"Concluída": False},
           {"Nome":'Resenha',"Descrição": 'resenha qualquer',"Prioridade": 'Baixa',"Categoria": 'Outros',"Concluída": False},
           ]

import Utils as ut
import pandas as pd 
import os
import streamlit_antd_components as sac
import streamlit as st

# Função para adicionar uma nova tarefa
def adicionar_tarefa(nome, descricao, prioridade, categoria):
    tarefa = {
        "Nome": nome,
        "Descrição": descricao,
        "Prioridade": prioridade,
        "Categoria": categoria,
        "Concluída": False
    }
    tarefas.append(tarefa)
    st.write("Tarefa adicionada com sucesso!")

# Função para listar todas as tarefas ou usando um filtro
def listar_tarefas(pPrioridade, pCategoria, pConcluida):
    if not tarefas:
        return pd.DataFrame()  # Retorna um DataFrame vazio se não houver tarefas
        
    df = pd.DataFrame(tarefas)
    df.insert(0, 'ID', range(1, len(df) + 1))
    df['Concluída'] = df['Concluída'].apply(lambda x: 'Sim' if x else 'Não')
    
    # Aplicar os filtros
    if (pPrioridade == 'Todas' and pCategoria == 'Todas' and pConcluida == 'Todas') or \
       (pPrioridade is None and pCategoria is None and pConcluida is None):
        df_filtrado = df
    elif pPrioridade == 'Todas' and pCategoria == 'Todas':
        df_filtrado = df[df['Concluída'] == pConcluida]
    elif pPrioridade == 'Todas' and pConcluida == 'Todas':
        df_filtrado = df[df['Categoria'] == pCategoria]
    elif pCategoria == 'Todas' and pConcluida == 'Todas':
        df_filtrado = df[df['Prioridade'] == pPrioridade]
    elif pConcluida == 'Todas':
        df_filtrado = df[(df['Prioridade'] == pPrioridade) & (df['Categoria'] == pCategoria)]
    elif pPrioridade == 'Todas':
        df_filtrado = df[(df['Categoria'] == pCategoria) & (df['Concluída'] == pConcluida)]
    elif pCategoria == 'Todas':
        df_filtrado = df[(df['Prioridade'] == pPrioridade) & (df['Concluída'] == pConcluida)]
    elif pPrioridade is None:
        df_filtrado = df[(df['Categoria'] == pCategoria) & (df['Concluída'] == pConcluida)]
    elif pCategoria is None:
        df_filtrado = df[(df['Prioridade'] == pPrioridade) & (df['Concluída'] == pConcluida)]
    else:
        df_filtrado = df[(df['Prioridade'] == pPrioridade) & (df['Categoria'] == pCategoria) & (df['Concluída'] == pConcluida)]
    
    return df_filtrado

# Paramentros para cadastro
prioridades = ['Alta', 'Média', 'Baixa']
categorias = ['Trabalho', 'Estudo', 'Lazer', 'Casa', 'Saúde', 'Outros']

# Parametros para pesquisa
prioridades_p = ['Todas', 'Alta', 'Média', 'Baixa']

categorias_p = ['Todas', 'Trabalho', 'Estudo', 'Lazer', 'Casa', 'Saúde', 'Outros']

concluida_p =  ['Todas', 'Sim', 'Não']

# Função para marcar uma tarefa como concluída
def marcar_como_concluida(numero_tarefa):
    if 1 <= numero_tarefa <= len(tarefas):
        tarefas[numero_tarefa - 1]['Concluída'] = True
        st.write("Tarefa marcada como concluída!")
    else:
        st.write("Número de tarefa inválido.")


def Key_Unique(value : str):
    widget_id = 0
    widget_id = random.randint(100, 999)
    key_unique = f'{value}_{widget_id}'
    return key_unique