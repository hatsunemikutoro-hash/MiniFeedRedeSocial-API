from flask import Flask, render_template, jsonify
import requests
import mysql.connector

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'posts_json'
}

def cnx():
    return mysql.connector.connect(**db_config)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/import", methods=['GET'])
def importar_post():
    url = "https://jsonplaceholder.typicode.com/users/1/posts"

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        posts = resposta.json()
        print(len(posts))

        conn = cnx()
        cursor = conn.cursor()

        sql = """
            INSERT INTO posts (id, title, body, postid) 
            VALUES (%s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE title=VALUES(title), body=VALUES(body)
            """

        valores = [(p['id'], p['title'], p['body'], p['userId']) for p in posts]

        cursor.executemany(sql, valores)
        conn.commit()

        cursor.close()
        conn.close()

        return jsonify(posts), 200
    except Exception as e:
        return jsonify({'status': 'erro', 'detalhes': str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)