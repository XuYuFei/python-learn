from flask import Flask, url_for

app = Flask(__name__)  # 创建Flask对象


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s ' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d ' % post_id


@app.route('/url/')
def get_url():
    return url_for('show_post', post_id=2)


@app.route('/css/')
def get_style():
    return url_for('static', filename = 'style.css')


if __name__ == '__main__':
    app.run(debug = True)
