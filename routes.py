from app import app
@app.route('/')
@app.route('/index')
def index():
    user={'username':'Ishika'}
    return '''
    <html>
    <head>
    <title>MY APPLICATION</title>
    </head>
    <body bgcolor='green'>
    <h1>Hello,'''+user['username']+'''!</h1>
    </body>
    </html>'''