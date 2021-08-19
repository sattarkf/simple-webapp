import os
from flask import Flask
app = Flask(__NAME__)

@app.route("/")
def main():
	return "Welcome!"\

@app.route("/how are you")
def.hello():
	return 'I am Good, How about You?'
	
	
