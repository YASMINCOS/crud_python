import sqlite3 as lite


#CRUD 



#criando conexao
con=lite.connect('dados.db')


#inserir informacoes
def inserir_info(i):
    with con:
        cur=con.cursor()
        query="INSERT INTO formular (nome,email,telefone,dia_em_DATE,estado,assunto) VALUES (?, ?, ?, ?, ?, ?)"
        cur.execute(query,i)



#Acessando informacoes
def mostrar_info():
    lista=[]
    with con:
        cur= con.cursor()
        query="SELECT * FROM formular"
        cur.execute(query)
        informacao= cur.fetchall()
        
        for i in informacao:
            lista.append(i)
    return lista
            
        
#Atualizar info

def atualizar_info(i):
    with con:
        cur=con.cursor()
        query="UPDATE formular SET nome=?, email=?, telefone=?, dia_em_DATE=?, estado=?, assunto=? WHERE id=?"
        cur.execute(query,i)
    

#Delete

def deletar_info(i):
    with con:
        cur=con.cursor()
        query="DELETE FROM formular WHERE id=?"
        cur.execute(query,i)
    
