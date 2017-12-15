from elasticsearch import Elasticsearch
from flask import render_template
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def foo():
    return render_template('show.html')

@app.route('/result', methods=['POST'])
def f():
    que = request.form['request']
    es = Elasticsearch()
    a = es.search(index='news-index', doc_type='test', q=que)
    i = 0
    t=[]
    d=[]
    while i < 3:

        try:
            t.append(a['hits']['hits'][i]['_source']['title'])
            d.append(a['hits']['hits'][i]['_source']['date'])

        except IndexError:
            t.append( ' ')
            d.append(' ')

        i = i + 1
    return render_template('result.html',t1 = t[0],t2 = t[1], t3 = t[2], d1=d[0], d2=d[1], d3=d[2])


if __name__ == '__main__':
    app.run(port=8989, debug=True)