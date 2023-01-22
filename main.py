from flask import Flask,jsonify,request
import csv

all_articles=[]

with open("articles.csv")as f:
    reader=csv.reader(f)
    data=list(reader)
    all_articles=data[1:]

liked_articles=[]
not_liked_movies=[]

app=Flask(__name__)

@app.route("/get_articles")
def get_articles():
    return jsonify({
        "data":all_articles[0],
        "status":"sucess"
    })

@app.route("/liked_articles",method=["POST"])
def liked_articles():
    article=all_articles[0]
    all_articles=all_articles[1:]
    liked_articles.append(article)
    return jsonify({
        "status":"sucess"
    }),201

@app.route("/disliked_articles",method=["POST"])
def disliked_articles():
    article=all_articles[0]
    all_articles=all_articles[1:]
    disliked_articles.append(article)
    return jsonify({
        "status":"sucess"
    }),201

if __name__=="__main__":
    app.run()
    