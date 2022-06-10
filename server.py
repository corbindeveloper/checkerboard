from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html', num=8, cols = 8)

@app.route('/<int:num>')
def rows(num):
   return render_template('index.html', num=num, cols = 8)

@app.route('/<int:num>/<int:cols>')
def columns(num, cols):
   return render_template('index.html', num=num, cols=cols)

@app.route('/<int:num>/<int:cols>/<string:odd>')
def oddColor(num, cols, odd):
   return render_template('index.html', num=num, cols=cols, odd=odd)

@app.route('/<int:num>/<int:cols>/<string:odd>/<string:even>')
def evenColor(num, cols, odd, even):
   return render_template('index.html', num=num, cols=cols, odd=odd, even=even)

if __name__ == "__main__":
   app.run(debug = True)

