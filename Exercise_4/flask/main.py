from flask import render_template
from flask import Flask, request
import pickle



app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def foo():
    return render_template('example.html')

@app.route('/answer', methods=['POST'])
def f():
    que = request.form['article']

    with open('clf.pkl', 'rb') as f:
        clf = pickle.load(f)

    with open('count_vect.pkl', 'rb') as f:
        count_vect = pickle.load(f)
    predicted = clf.predict(count_vect.transform([que]).toarray())
    return render_template('answer.html',predicted = predicted[0])

if __name__ == '__main__':
    app.run(port=8989, debug=True)


