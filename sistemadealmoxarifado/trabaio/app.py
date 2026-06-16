from flask import Flask, render_template, request, redirect, session
import mysql.connector

app = Flask(__name__)

app.secret_key = 'roger'

@app.route('/entrada.html')
def entrada():
    return render_template("entrada.html")

@app.route('/login.html', methods=['GET', 'POST'])
def login():

    return render_template("login.html")

@app.route('/criacao.html', methods=['GET', 'POST'])
def criacao():
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='TCC'
    )

    if request.method == 'POST':
        print('teste se metodo = post')
        dado_name = request.form['nome']
        dado_funcao = request.form['funcao']
        dado_senha = request.form['senha']

        cursor = conexao.cursor()
        query = """
        INSERT INTO funcionario (nome, funcao, senha)
        VALUES (%s, %s, %s)
        """
        valores = (dado_name, dado_funcao, dado_senha)

        cursor.execute(query, valores)
        conexao.commit()

        cursor.close()
   
    return render_template("criacao.html")

@app.route('/loginusuario.html', methods=['GET', 'POST'])
def loginusuario():
    if request.method == 'POST':
        nome = request.form.get('nome')
        senha = request.form.get('senha')
        conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='TCC'
        )

        cursor = conexao.cursor()
        query = "SELECT id FROM funcionario WHERE nome = %s AND senha = %s"

        cursor.execute(query, (nome, senha))
        resultado = cursor.fetchone()

        cursor.close()
        conexao.close()

        if resultado:
            session['usuario_logado'] = nome
            return redirect('/estoque.html')
        else:
            return render_template("loginusuario.html", erro=True)
        
    return render_template("loginusuario.html")

@app.route('/index.html', methods=['GET', 'POST'] )
def index():
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='TCC'
    )
    print('teste')
    if request.method == 'POST':
        print('teste se metodo = post')
        dado_name = request.form['nome']
        dado_quantidade = request.form['quantidade']
        dado_categoria = request.form['categoria']
        dado_estoque_minimo = request.form['estoque_minimo']
        dado_preço = request.form['descrição']
        dado_descrição = request.form['preço']

        cursor = conexao.cursor()
        query = """
        INSERT INTO estoque_almoxarifado (nome, quantidade, categoria, estoque_minimo, descrição, preço)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        valores = (dado_name, dado_quantidade, dado_categoria, dado_estoque_minimo, dado_preço, dado_descrição)

        cursor.execute(query, valores)
        conexao.commit()

        cursor.close()

        

    return render_template("index.html")


@app.route('/estoque.html', methods=['GET', 'POST'])
def estoque():
    if 'usuario_logado' not in session:
        return redirect('/loginusuario.html')
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='TCC'
    )

    cursor = conexao.cursor()
    query = "SELECT id, nome, quantidade, estoque_minimo, descrição, preço, categoria FROM estoque_almoxarifado"
    print ("foi")

    cursor.execute(query)
    resultado_banco = cursor.fetchall()
    cursor.close()
    conexao.close()

    return render_template("estoque.html", resultado=resultado_banco)

@app.route('/solicitar.html', methods=['GET', 'POST'])
def solicitar():
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='TCC'
    )

    if request.method == 'POST':
        cursor = conexao.cursor()

        dado_id = request.form['id']
        dado_quantidade = int(request.form['quantidade'])
        acao = request.form['acao']

        cursor.execute("SELECT quantidade FROM estoque_almoxarifado WHERE id =%s", (dado_id,))

        resultado=cursor.fetchone()
        if resultado:
            quantidade_atual=int(resultado[0]) if resultado[0] is not None else 0
            if acao == 'colocar':
                nova_quantidade = quantidade_atual + dado_quantidade
    
            elif acao == 'retirar':
                if quantidade_atual >= dado_quantidade:
                    nova_quantidade = quantidade_atual - dado_quantidade

                cursor.execute("""
                    UPDATE estoque_almoxarifado
                    SET quantidade = %s
                    WHERE id = %s
                """, (nova_quantidade, dado_id))

        conexao.commit()
        cursor.close()
        conexao.close()
        
    return render_template("solicitar.html")

@app.route('/tabela.html')
def tabela():
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='TCC'
    )

    cursor = conexao.cursor()
    query = "SELECT id, nome, funcao, senha FROM funcionario"
    print ("foi")

    cursor.execute(query)
    resultado_banco = cursor.fetchall()
    cursor.close()
    conexao.close()

    return render_template("tabela.html", resultado=resultado_banco)

if __name__== '__main__':
    app.run(host='0.0.0.0', debug=True)