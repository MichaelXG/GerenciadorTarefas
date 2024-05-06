'''
Class for do Login
'''
from Controllers.PadraoController import *

class LoginDAO():
    # Função para autenticar o usuário com o banco de dados
    def authenticator(apelido: str, password: str) -> bool:
        
        # DataFrame com login gerados
        df_login = pd.DataFrame(login)
        
        if df_login.empty:
            return False  # Retorna falso se o DataFrame de login estiver vazio
        
        # Verifica se o apelido existe 
        if apelido in df_login['Apelido'].values:
            # Obtém a linha correspondente ao apelido
            usuario = df_login[df_login['Apelido'] == apelido].iloc[0]
            
            # Verifica a senha 
            if usuario['Password'] == password:
                return True  # Senha correta
            else:
                return False  # Senha incorreta
        else:
            return False  # Apelido não encontrado
        
        

 