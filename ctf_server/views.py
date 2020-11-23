from ctf_server import app

@app.route('/')
def index():
  return 'Hello World!'
