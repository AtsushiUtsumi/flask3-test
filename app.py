from flask import Flask, render_template

app = Flask(__name__)
app.config['JWT_TOKEN_LOCATION'] = ['headers']# これを後から足した
app.config['JWT_SECRET_KEY'] = 'your-secret-key'  # 本番環境では環境変数から読み込むことを推奨

@app.route('/')
def test():
    return 'TEST'
