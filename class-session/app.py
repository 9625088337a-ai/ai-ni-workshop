# 1. Import Flask
from flask import Flask

# 2. Create the app
app = Flask(__name__)

# 3. Homepage route
@app.route('/')
def home():
    return '''
    <h1>Python Notes</h1>
    <p>Welcome to your study notebook server</p>
    '''

# 4. Test route
@app.route('/test')
def test():
    return '''
    <h1>Python Notes</h1>
    <p>Welcome to your study notebook server.</p>
    '''

# 5. Run the server
if __name__ == '__main__':
    app.run(debug=True)