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
# sql1 = """ 
# INSERT INTO employees(ID,name,DeptID,ManagerID)
# VALUES(8,'kenneth',8,101)"""
#위아래 두가지 방법 데이터를 직접 넣어주거나 execute에 넣어주거나

sql1 = """
INSERT INTO employees(ID,name,DeptID,ManagerID)
VALUES(%s,%s,%s,%s)"""


# cursor.execute(sql1)
cursor.execute(sql1,(8,'kenneth',8,101))


conn.commit()
# print("현재 데이터 베이스:",cursor.fetchmany())
print('데이터 삽입 완료')

# 연결 해제 
conn.close()
