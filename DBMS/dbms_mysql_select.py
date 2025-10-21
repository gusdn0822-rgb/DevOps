import pymysql

# mySQL 서버에 연결
conn = pymysql.connect(
    host="localhost",  #mySQL 서버 주소
    user="root",        #사용자명
    password="1234",     #비밀번호
    database="employees", #사용할 데이터베이스 명
   
    
)
#커서 생성 => 명령어 작성이 가능하다
cursor = conn.cursor()
#명령어 실행
sql = "SELECT * FROM employees"
cursor.execute(sql)
employees = cursor.fetchall()
for emplotee in employees:
    print(emplotee)
# print("현재 데이터 베이스:",cursor.fetchmany())
print('데이터 조회 완료')

# 연결 해제 
conn.close()
