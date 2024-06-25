from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)

def connect_db():
    return psycopg2.connect(
        host="192.168.1.8",
        port="5432",
        database="postgres",
        user="postgres",
        password="R@mones12"
    )

@app.route('/')
def index():
    return render_template('register_aluno.html')

@app.route('/register_aluno', methods=['POST'])
def register_aluno():
    name = request.form['name']
    data_nascimento = request.form['data_nascimento']
    endereco = request.form['endereco']
    telefone = request.form['telefone']

    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO alunos (nome, data_nascimento, endereco, telefone) VALUES (%s, %s, %s, %s)",
                (name, data_nascimento, endereco, telefone))
    conn.commit()
    cur.close()
    conn.close()

    return render_template('success.html')

@app.route('/register_matricula', methods=['GET', 'POST'])
def register_matricula():
    if request.method == 'POST':
        aluno_id = request.form['aluno_id']
        disciplina_id = request.form['disciplina_id']
        data_matricula = request.form['data_matricula']
        nota = request.form.get('nota', None)

        conn = connect_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO matriculas (aluno_id, disciplina_id, data_matricula, nota) VALUES (%s, %s, %s, %s)",
                    (aluno_id, disciplina_id, data_matricula, nota))
        conn.commit()
        cur.close()
        conn.close()

        return render_template('success.html')

    return render_template('register_matricula.html')

if __name__ == '__main__':
    app.run(debug=True)
