import streamlit as st
import time
import streamlit_antd_components as sac
import re

def Aspas_simples(value_str: str):
    if value_str is None:
        return '\'' + '\''
    else:
        return '\'' + value_str + '\''

# Converte Bool
def convertToBool(value_bool:bool):
    if value_bool == True:
        return 1
    else:
        return 0 
  
def InvertToBool(value_bool:bool):
    if value_bool == True:
        return False
    else:
        return True
      
def convertToSexo(value_sexo:str):
    if ('M'.find(value_sexo[0].upper()) >= 0):
        return 'M'
    else:
        return 'F'
    
def fn_spinner_3(value_msg: str):
    with st.spinner(value_msg):
        time.sleep(3)  # Simula uma operação demorada de 5 segundos
        
# Função que simula uma operação demorada
def fn_spinner_5(value_msg: str):
    with st.spinner(value_msg):
        time.sleep(5)  # Simula uma operação demorada de 5 segundos

def fn_spinner_10(value_msg: str):
    with st.spinner(value_msg):
        time.sleep(10)  # Simula uma operação demorada de 5 segundos 
             
# Formatar DateTime     
def format_datetime_post(value_str:str):
    return Aspas_simples(value_str.strftime("%Y-%m-%d %H:%M:%S"))

# Formatar DateTime     
def format_datetime_get(value_str:str):
    return Aspas_simples(value_str.strftime("%d/%m/%Y %H:%M:%S"))

# Formatar Date
def format_date_post(value_str:str):
    return Aspas_simples(value_str.strftime("%Y-%m-%d"))

# Formatar Time    
def format_time(value_str:str):
    return Aspas_simples(value_str.strftime("%H:%M:%S"))

# Valida Str vazia
def validate_none(value_none:str, p_type:str):
    if p_type == 'str':
        return '\'''' if value_none is None else str(value_none)
    # elif p_type == 'int':
    #      return NULL if value_none is None else int(value_none)

def calcular_media(valor, qtd) :
    media = (valor / qtd)
    return media 

def primeira_letra_maiscula(string: str):
    new_text = ''
    quebra = string.split(' ')
    tamanho_list = len(quebra)
    for p in range(tamanho_list):
        if tamanho_list == 1:
             new_text = quebra[p].capitalize()
        else:
            new_text += quebra[p].capitalize() + ' '  
    return str(new_text)

def remove_espaco_duplo(string: str):
    return " ".join(string.split())   
            
def Alerta(plabel, pdescription, pradius = 'lg', pcolor='rgb(20,80,90)'):
    sac.alert(label= plabel, description= pdescription, radius=pradius, color=pcolor, banner=[False, True], icon=True, closable=True)
    
def Informacao(plabel= 'label', pdescription= 'Informação'):
    sac.result(label=plabel, description=pdescription)
    
def Sucesso(plabel = 'label', pdescription = 'success'):
    sac.result(label=plabel, description=pdescription, status='success')
    
def Aviso(plabel = 'label', pdescription = 'warning'):
    sac.result(label=plabel, description=pdescription, status='warning')

def Erro(plabel = 'label', pdescription = 'error'):
    sac.result(label=plabel, description=pdescription, status='error')

def Vazio(plabel = 'label', pdescription = 'empty'):
    sac.result(label=plabel, description=pdescription, status='empty')
    
def Divisor(plabel = 'label', picon='house', pcolor='rgb(20,80,90)', pKey : str = ''):
    sac.divider(label=plabel, icon=picon, align='center', variant='solid', color=pcolor, key=pKey)
    
# Função de validação que recebe uma lista de campos e retorna um dicionário de mensagens de erro
def validar_campos(campos):
    mensagens_erro = {}

    for campo in campos:
        valor = campo["valor"]
        label = campo["label"]

        if not valor:
            mensagens_erro[campo["key"]] = f"{label} é obrigatório!"

        # Adicione outras validações conforme necessário
        # Exemplo: Verificar se o campo é um número, se tem um formato específico, etc.

    return mensagens_erro

# Colocar as letras em maiúscula
_upperCase = lambda n : n.upper()

# Colocar as letras em minúsculas 
_casefold = lambda n : n.casefold()

# Verificar se é número
_isnumeric = lambda n : n.isnumeric() 
