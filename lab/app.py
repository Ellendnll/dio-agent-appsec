# ATENÇÃO: código vulnerável de propósito, para estudo. Rode só na sua máquina.
import sqlite3
from flask import Flask, request

app = Flask(__name__)
DB = "lab.db"


def init_db():
    conn = sqlite3.connect(DB)
    conn.execute("CREATE TABLE IF NOT EXISTS usuarios (usuario TEXT, senha TEXT)")
    conn.execute("DELETE FROM usuarios")
    conn.execute("INSERT INTO usuarios VALUES ('ana', 'senha123')")
    conn.commit()
    conn.close()


@app.route("/login", methods=["POST"])
def login():
    usuario = request.form.get("usuario", "")
    senha = request.form.get("senha", "")
    conn = sqlite3.connect(DB)
    # FALHA: entrada do usuário concatenada direto no SQL
    query = "SELECT * FROM usuarios WHERE usuario = '" + usuario + "' AND senha = '" + senha + "'"
    row = conn.execute(query).fetchone()
    conn.close()
    return "Login OK" if row else ("Credenciais inválidas", 401)


if __name__ == "__main__":
    init_db()
    app.run(host="127.0.0.1", port=5000)
