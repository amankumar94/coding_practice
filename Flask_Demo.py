# GET - Sends data in unencrypted form to server
# HEAD - Same as GET, but without response body
# POST - Used to send HTML form data to server
# PUT - Replaces all current representations of target resource with uploaded content
# DELETE - Removes all current representations of target resource given by URL

from flask import Flask, redirect, url_for, request
from flask import render_template #to render HTML templates
app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return 'Hello World'


# taking value from the url to manipulate in the web page -> String
@app.route('/customHello/<name>')
def custom_hello_world(name):
    return 'Hello %s' % name


# taking value from the url to manipulate in the web page -> int
@app.route('/blog/<int:postID>')
def show_blog(postID):
    return 'Blog Number %s' % postID


# taking value from the url to manipulate in the web page -> float
@app.route('/rev/<float:revNo>')
def revision(revNo):
    return 'Revision Number %s' % revNo


# application redirection using url_for()
@app.route('/admin')
def hello_admin():
    return 'Hello Admin'


@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest' % guest


@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect("url_for('hello_guest',guest=name)")


def bye():
    return 'bye Hello World'


@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))


app.add_url_rule('/bye', 'bye', bye)  # adding route to the url without annotation - Alternative method

@app.route('/hello/<user>')
def hello_name(user):
    return render_template('hello.html', name = 'Aman')

if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug=True)
