import os
from flask import Flask
app = Flask(__NAME__)

@app.route("/")
def main():
	return "Welcome!"\

@app.route("/how are you")
def.hello():
	return 'I am Good, How about You?'
	
If __NAME__ == "__main__":
	app.run(host="0.0.0.0", port=8080)
	
