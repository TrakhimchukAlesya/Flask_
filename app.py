from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")

# @app.route('/user/<string:name>/<int:id>')
# def user(name,id):
#     return 'User page'+name+"-"+str(id)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/mht')
def my_html_template():
    return render_template('my_html_t.html')

if __name__=='__main__':
    app.run(debug=True)