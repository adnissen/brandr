from flask import Flask
import random
app = Flask(__name__)

@app.route("/")
def main():
	return getBrand() + ": " + getSlogan()

def getBrand():
    return (random.choice(list(open('brands.txt'))))

def getSlogan():
    return (random.choice(list(open('slogans.txt'))))

if __name__ == "__main__":
    app.run()