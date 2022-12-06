from flask import Flask, render_template, request, jsonify
import pymysql
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('comment.html')


@app.route("/comment", methods=["POST"])
def insert_comment():
    db = pymysql.connect(host='localhost', user='root', password='Rotorrl1!', db="new_project", port=3306)
    cursor = db.cursor()
    print("hello1")
    # comment = request.json

    comment_title = request.form["comment_title"]
    comment_content = request.form["comment_content"]
    star = request.form["star"]
    print(comment_title, comment_content, star)

    # sql = """insert into comment (comment_id,comment_content,star)values (%s,%s,%s)"""
    # cursor.execute(sql, (comment_id, comment_content, star))
    # rows = cursor.fetchall()
    # json_str = json.dumps(rows, indent=4, sort_keys=True, default=str)
    # db.commit()
    # db.close()
    # return 'insert success', 200

    # comment_id_receive = request.form['comment_id_give']
    # comment_receive = request.form['comment_content_give']
    # star_receive = request.form['star_give']

    sql = """insert into comment (comment_title,comment_content,star)values (%s,%s,%s)"""

    cursor.execute(sql, (comment_title, comment_content, star))
    db.commit()
    db.close()
    return jsonify({'msg': '댓글 달기 완료!'})


@app.route("/comment", methods=["GET"])
def get_comments():
    db = pymysql.connect(host='localhost', user='root', password='Rotorrl1!', port=3306)
    cursor = db.cursor()
    sql = """
        SELECT *
        FROM new_project.comment
        """
    cursor.execute(sql)
    rows = cursor.fetchall()

    # python 객체를 json 데이터로 쓰기
    json_str = json.dumps(rows, indent=4, sort_keys=True, default=str, ensure_ascii=False)

    db.commit()
    db.close()
    return json_str,200

# 서버실행
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)



