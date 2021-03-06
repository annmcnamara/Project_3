from flask import Flask, render_template

# EB looks for an 'application' callable by default.
application = Flask(__name__)

@application.route("/")
def welcome():
	return render_template("index.html")

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
