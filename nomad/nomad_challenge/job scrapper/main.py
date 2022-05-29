
from flask import Flask, Response, render_template, request
from joblist import get_jobs

app = Flask("Job Search")


@app.route('/')
def hello():
    return render_template('hello.html')


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/report/')
def report():
    word = request.args.get('word')
    jobs = get_jobs(word)
    return render_template('report.html', jobs=jobs, word=word)


@app.route('/download/<word>')
def download(word):
    jobs = get_jobs(word)
    csv = 'title,company,site\n'
    contents = []
    for job in jobs:
        content = job['title']+','+job['company']+','+job['site']
        contents.append(content)
    csv += '\n'.join(contents)
    return Response(csv, mimetype="text/csv", headers={"Content-disposition": "attachment; filename=jobs_list.csv"})


app.run(host="0.0.0.0")
