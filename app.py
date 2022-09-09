from flask import Flask,render_template,Form






app = Flask(__name__)



# @app.route('/')
# def index():
#   return render_template('index.html')

# @app.route('/home')
# def home():
#   return '<h2>Bad request</h2>',400

# @app.route('/cookie')
# def cookie():
#   response = make_response('<h1>This contains a cookie </h1>')
#   response.set_cookie('answer', '42')
#   return response

# @app.route('/dotcom')
# def dotcom():
#   return redirect('/')
class NameForm(Form):


@app.route('')
def user():
  return 

















if __name__ == '__main__':
  app.run(debug=True)







