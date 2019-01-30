from flask import Flask
app = Flask(__name__)

class Developer:
	first_name = ""
	last_name = ""
	programming_language = ""

	def __init__(self, fname, lname, plan):
		self.first_name = fname
		self.last_name = lname
		self.programming_language = plan

	def __str__(self):
		return "{} {} - {}".format(self.first_name, self.last_name, self.programming_language)

d_list = []
d_list.append(Developer("Dan", "Brown", "Java Developer"))
d_list.append(Developer("July", "Fish", "Python Developer"))
d_list.append(Developer("Tom", "Tory", "iOS Developer"))

@app.route('/')
def developer_controller():
    d = Developer("Dan", "Brown", "Java Developer")

    return str(d)

@app.route('/remove_developer')
def remove_developer():
    if len(d_list) > 0:
    	d_list.pop()

    return str(len(d_list))



