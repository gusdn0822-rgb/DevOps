import pymysql

# mySQL 서버에 연결
conn = pymysql.connect(
    host="localhost",  #mySQL 서버 주소
    user="root",        #사용자명
    password="1234",     #비밀번호
    database="employees", #사용할 데이터베이스 명
    charset="utf8mb4",     #utf-9의 확장버전
    cursorclass=pymysql.cursors.DictCursor
)
#커서 생성 => 명령어 작성이 가능하다
cursor = conn.cursor()
#명령어 실행
cursor.execute("SELECT DATABASE()")
#한번 호출에 하나의 row를 가져올떄 사용
print("현재 데이터 베이스:",cursor.fetchone())
# print("현재 데이터 베이스:",cursor.fetchall())
# print("현재 데이터 베이스:",cursor.fetchmany())


# 연결 해제 
conn.close()
