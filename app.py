from flask import Flask, render_template, request, jsonify, flash, session
import pymysql
import json

app = Flask(__name__)

@app.route('/')
def home():
    #병학님 로그인 되었는지 확인하는 코드
    # session['login_flag'] = True
    # session['user_id'] = "abc"

    return render_template('comment.html')


@app.route("/comment", methods=["POST"])
def insert_comment():
    db = pymysql.connect(host='hjdb.cmux79u98wpg.us-east-1.rds.amazonaws.com', user='master', password='Abcd!234', db="hjdb", port=3306)
    cursor = db.cursor()
    # print("hello1")
    # comment = request.json

    comment_title = request.form["comment_title"]
    comment_content = request.form["comment_content"]
    star = request.form["star"]
    # print(comment_title, comment_content, star)

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

    sql = """insert into comment (comment_title,comment_content,star, user_unique_id,problem_id,review_id)values (%s,%s,%s,%s,%s,%s)"""

    cursor.execute(sql, (comment_title, comment_content, star,1,1,1))
    db.commit()
    db.close()
    return jsonify({'msg': '댓글 달기 완료!'})


@app.route("/comment", methods=["GET"])
def get_comments():
    db = pymysql.connect(host='hjdb.cmux79u98wpg.us-east-1.rds.amazonaws.com', user='master', password='Abcd!234', db="hjdb", port=3306)
    cursor = db.cursor()
    sql = """
        SELECT comment.comment_id, comment.comment_title, users.user_id,comment.comment_content,comment.star, comment.user_unique_id,comment.problem_id, comment.review_id
        FROM comment
        INNER JOIN users ON comment.user_unique_id =users.unique_id;
        """
    cursor.execute(sql)
    rows = cursor.fetchall()

    # python 객체를 json 데이터로 쓰기
    json_str = json.dumps(rows, indent=4, sort_keys=True, default=str, ensure_ascii=False)

    db.commit()
    db.close()
    return json_str,200


@app.route("/comment", methods=["PATCH"])
def patch_comment():
    db = pymysql.connect(host='hjdb.cmux79u98wpg.us-east-1.rds.amazonaws.com', user='master', password='Abcd!234', db="hjdb", port=3306)
    cursor = db.cursor()

    comment_title = request.form["comment_title"]
    comment_content = request.form["comment_content"]
    star = request.form["star"]

    sql = """UPDATE comment
	set comment_content = "new content", comment_title = "new title",star = 2
	where user_unique_id = 1; """
    # user_unique_id 대신 user_id를 가져오는 방법?

    cursor.execute(sql)
    db.commit()
    db.close()
    # 해당 댓글 수정하는 창 새로 띄우기, post 다시 하기
    return jsonify({'msg': '댓글이 정상적으로 수정되었습니다.'})

@app.route("/comment", methods=["DELETE"])
def delete_comment():
    db = pymysql.connect(host='hjdb.cmux79u98wpg.us-east-1.rds.amazonaws.com', user='master', password='Abcd!234', db="hjdb", port=3306)
    cursor = db.cursor()

    comment_title = request.form["comment_title"]
    comment_content = request.form["comment_content"]
    star = request.form["star"]

    sql = """DELETE from comment where user_unique_id = 1;"""
    # user_unique_id 대신 user_id를 가져오는 방법?
    # user_id = '$(sessionID)' 비교하는 방법?

    cursor.execute(sql)
    db.commit()
    db.close()

    return jsonify({'msg': '댓글이 정상적으로 삭제되었습니다.'})

# 서버실행
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)



