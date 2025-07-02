from flask import Flask 

app= Flask(__name__)

@app.route("/")
def index():
    with get_connection().cursor()as cur:
        cur.execute("SELECT *FROM student")
        res = cur.fetchall()
        print(res)
    return render_template('index.html',nm=res) 

@app.route("/student/<int:id>")
def get




"<h1>Hello World </h1>"
if __name__=='__main__':
    app.run(debug=True)


