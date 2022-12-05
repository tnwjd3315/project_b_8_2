from flask import Flask, render_template, request, jsonify
import pymysql
import json

app = Flask(__name__)

db = pymysql.connect(host='localhost', user='root', password='Rotorrl1!', port=3306)
cursor = db.cursor()
sql = """
    SELECT *
    FROM sparta_test.review
    """
cursor.execute(sql)
result = cursor.fetchall()

@app.route('/')
def home():
    return render_template('comment.html')


@app.route("/comment", methods=["POST"])
def web_comment_reply_post():
    comment_id_receive = request.form['comment_id_give']
    comment_receive = request.form['comment_give']
    star_receive = request.form['star_give']

    print(comment_id_receive)

    doc = {
        'comment_id': comment_id_receive,
        'comment': comment_receive,
        'star': star_receive
    }
    db.comment_reply.insert_one(doc)
    print(doc)
    return jsonify({'msg': '댓글 달기 완료!'})


@app.route("/comment", methods=["GET"])
def web_comment_reply_get():
    #all_comments = list(comment_reply.find({}, {'_id': False}))
    #print(all_comments)
    #return jsonify({'all_comments': all_comments})
    return jsonify({'msg': '댓글 달기 완료!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)



