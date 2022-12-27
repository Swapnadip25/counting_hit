from flask import Flask

app = Flask(__name__)

visit_counter = 0

@app.route('/')
def page_visit():
 global visit_counter
 visit_counter += 1
 return "You have hit the URL "+ str(visit_counter) +" times"

if __name__ == '__main__':
 app.run(debug=True)
