from flask import Flask,render_template
import pymysql


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/index')
def home():
    #return render_template("index.html")
    return index()


@app.route('/movie')
def movie():
    datalist  = []
    con = pymysql.connect(
        host='192.168.43.100',
        port=3306,
        user='root',
        passwd='Root@123',
        db='doubanbook',
        charset='utf8'
    )
    cur = con.cursor()
    sql = "select * from books"
    data = cur.execute(sql)
    result=cur.fetchall()
    for item in result:
        datalist.append(item)
    cur.close()
    cur.close()
    print(datalist)
    return render_template("movie.html", movies=datalist)



@app.route('/score')
def score():
    score = []  #评分
    num = []    #每个评分所统计出的电影数量
    conn = pymysql.Connect(
        host='192.168.43.100',
        port=3306,
        user='root',
        passwd='Root@123',
        db='doubanbook',
        charset='utf8'
    )
    cur = conn.cursor()
    sql = "select * from book_score_num"
    data = cur.execute(sql)
    result = cur.fetchall()
    for item in result:
        score.append(str(item[0]))
        num.append(item[1])

    cur.close()
    conn.close()
    return render_template("score.html",score= score,num=num)

@app.route('/country')
def country():
    country = []  #评分
    num = []    #每个评分所统计出的电影数量
    conn = pymysql.Connect(
        host='192.168.43.100',
        port=3306,
        user='root',
        passwd='Root@123',
        db='doubanbook',
        charset='utf8'
    )
    cur = conn.cursor()
    sql = "select * from book_country_num"
    data = cur.execute(sql)
    result = cur.fetchall()
    for item in result:
        country.append(str(item[0]))
        num.append(item[1])

    cur.close()
    conn.close()
    return render_template("country.html",country=country,num=num)

@app.route('/peopletop10')
def peopletop10():
    people = []  #评论人数
    title = []    #书名
    s=[]
    conn = pymysql.Connect(
        host='192.168.43.100',
        port=3306,
        user='root',
        passwd='Root@123',
        db='doubanbook',
        charset='utf8'
    )
    cur = conn.cursor()
    sql = "select * from book_people_title"
    data = cur.execute(sql)
    result = cur.fetchall()
    for item in result:
        s.append(item)
        people.append(str(item[0]))
        title.append(item[1])

    cur.close()
    conn.close()
    return render_template("peopletop10.html", people=people,title=title)



@app.route('/presstime')
def presstime():
    year = []
    num = []
    s=[]
    conn = pymysql.Connect(
        host='192.168.43.100',
        port=3306,
        user='root',
        passwd='Root@123',
        db='doubanbook',
        charset='utf8'
    )
    cur = conn.cursor()
    sql = "select * from book_presstime_num"
    data = cur.execute(sql)
    result = cur.fetchall()
    for item in result:
        s.append(item)
        year.append(str(item[0]))
        num.append(item[1])

    cur.close()
    conn.close()
    return render_template("presstime.html", year=year,num=num)


@app.route('/publisher')
def publisher():
    year = []
    num = []
    s=[]
    conn = pymysql.Connect(
        host='192.168.43.100',
        port=3306,
        user='root',
        passwd='Root@123',
        db='doubanbook',
        charset='utf8'
    )
    cur = conn.cursor()
    sql = "select * from book_publisher_num"
    data = cur.execute(sql)
    result = cur.fetchall()
    for item in result:
        s.append(item)
        year.append(str(item[0]))
        num.append(item[1])

    cur.close()
    conn.close()
    return render_template("publisher.html", year=year,num=num)



@app.route('/word')
def word():
    return render_template("word.html")

@app.route('/team')
def team():
    return render_template("team.html")


if __name__ == '__main__':
    app.run()
