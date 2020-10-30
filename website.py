from flask import Flask

app = Flask('website')

@app.route('/')
def index():
    return '<html><body>Hello world!</body></html>'

if __name__ == '__main__':
    from elsa import cli
    cli(app, base_url='https://datamarble.org')