from flask import Flask, render_template, url_for


application = app = Flask(__name__)

@app.route('/')
def homepage():
	#pageType = "home"
	title = "Yeah Buddy, I've got a title!."
	paragraph = ["does this work without brackets?", "I hope so, it should be a list now", "if it's not a list, it will be an ugly paragraph."]
	return render_template("index.html", title=title, paragraph=paragraph)

@app.route('/graph')
def graph(chartID = 'chart_ID', chart_type = 'line', chart_height = 500):
	def calc():
		data1 = [7, 8, 9, 10, 11, 12, 13, 15, 15, 11, 8, 7]
		return data1
	chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
#	data1 = [7, 8, 9, 10, 11, 12, 13, 15, 15, 11, 8, 7]
	series = [{"name": 'Label1', "data": calc()}, {"name": 'Label2', "data": [4, 5, 6]}]
	graph_title = {"text": 'My Title'}
	xAxis = {"categories": ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Oct', 'Sept', 'Nov', 'Dec']}
	yAxis = {"title": {"text": 'yAxis Label'}}
	return render_template('index.html', chartID=chartID, chart=chart, series=series, graph_title=graph_title, xAxis=xAxis, yAxis=yAxis)
	
	


if __name__ == "__main__":
	app.debug = True
	app.run()
