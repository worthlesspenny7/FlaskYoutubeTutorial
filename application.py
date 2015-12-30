from flask import Flask, render_template


application = app = Flask(__name__)

@app.route('/')
def homepage():

	title = "Yeah Buddy, I've got a title!."
	paragraph = ["does this work without brackets?", "I hope so, it should be a list now", "if it's not a list, it will be an ugly paragraph."]
	return render_template("index.html", title=title, paragraph=paragraph)
	
if __name__ == "__main__":
	app.run()
