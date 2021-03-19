import streamlit as st
import mysql.connector
from mysql.connector import Error
from datetime import datetime, date, time

def main():

    # title = st.text_input('제목을 입력하세요')
    # author_fname = st.text_input('이름을 입력하세요')
    # author_lname = st.text_input('성을 입력하세요')
    # released_year = st.number_input('출판연도를 입력하세요')
    # stock_quantity = st.number_input('재고량을 입력하세요')
    # pages = st.number_input('책 페이지수를 입력하세요')
    # name = st.text_input('이름입력')
    # birth_date = st.date_input('생년월일')
    # birth_time = st.time_input('시간입력')

    # print(birth_date)
    # print(birth_time)
    if st.button('저장하기'):
        try:
            # 1. 커넥터로부터 연결받는다.
            connection = mysql.connector.connect(
                host = 'database-2.ceq6zvnkjznb.us-east-2.rds.amazonaws.com',
                database = 'instar_pri',
                user = 'streamlit',
                password = 'dhghfk28'
            )
            if connection.is_connected() :
                db_info = connection.get_server_info()
                print('MySQL server version :', db_info)

                #2. 커서를 가져온다
                cursor = connection.cursor()

                #3. 우리가 원하는 명령 실행 가능
                query = """insert into cats4(name,age) values
                            (%s,%s);"""
                record = [('냐웅이',1),('나비',3),('벌이',3)]
                # record = (name, birth_date, birth_time, datetime.combine(birth_date, birth_time))
                # query = """insert into books( title, author_fname, author_lname,
                #             released_year, stock_quantity, pages) values
                #             (%s,%s,%s,%s,%s,%s);"""
                # record = (title,author_fname,author_lname,released_year,stock_quantity,pages)
            
                cursor.executemany(query, record)
                connection.commit()
                print('{}개 적용됨'.format(cursor.rowcount))

                #4. 실행 후 커서에서 결과를 빼낸다.
                # record = cursor.fetchone()
                # print('Connected to db : ',record)

        
        except Error as e :
            print('DB error', e)
        
        finally :
            # 5. 모든 데이터베이스 실행 명령이 끝나면, 커서와 커넥션을 모두 닫는다
            cursor.close()
            connection.close()
            print('MySQL 커넥션 종료')


if __name__ == '__main__':
    main()