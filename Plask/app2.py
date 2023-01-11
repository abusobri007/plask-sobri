from flask import Flask, render_template


app = Flask(__name__)

@app.route('/budi')
def home():
      return  render_template('budi.html')



if __name__=='__main__':
      app.run(debug=True)
