from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello Flask!</h1>'


@app.route('/hi')
@app.route('/hello')
def say_hello():
    return '<h1>Hello Flask!</h1>'


@app.route('/greet', defaults={'name': 'Programmer'})
@app.route('/greet/<name>')
def greet(name):
    return '<h1>Hello, {}</h1>'.format(name)


@app.cli.command()
def hello():
    """Just say hello."""
    # click.echo('Hello, Human!')
    print('Hello, Human!')
# 等价写法
# @app.route('/greet')
# @app.route('/greet/<name>')
# def greet(name='Programmer'):
#     return '<h1>Hello, {}</h1>'.format(name)

# if __name__ == '__main__':
#     app.run()
