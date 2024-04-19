from flask import Flask, render_template,jsonify

app = Flask(__name__)

JOBS = [{
    "id": 1,
    "profile": "Data Analyst",
    "company": "Google",
    "location": "Bangalore",
    "salary": "Rs.10,00,000"
}, {
    "id": 2,
    "profile": "Data Scientist",
    "company": "Amazon",
    "location": "Bangalore",
    "salary": "Rs.15,00,000"
}, {
    "id": 3,
    "profile": "Data Engineer",
    "company": "Microsoft",
    "location": "Bangalore",
    "salary": "Rs.20,00,000"
}, {
    "id": 4,
    "profile": "Data Analyst",
    "company": "Google",
    "location": "Bangalore",
    "salary": "Rs.10,00,000"
}, {
    "id": 5,
    "profile": "fullstack developer",
    "company": "Google",
    "location": "Bangalore",
    "salary": "Rs.30,00,000"
}]


@app.route('/')
def helloworld():
  return render_template('home.html', jobs=JOBS, company_name="Pagaar")

@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080, debug=True)
