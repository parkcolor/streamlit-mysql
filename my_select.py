import streamlit as st
import mysql.connector
from mysql.connector import Error
from datetime import datetime, date, time

import numpy as np
import pandas as pd
import json

def run_select():

    column_list = ['title','author_fname','author_lname','released_year','stock_quantity','pages']

    selected_column_list = st.multiselect('컬럼을 선택하세요',column_list)

    if len(selected_column_list) == 0:
        query  = """ select * from books; """
    else :
        column_str = ', '.join(selected_column_list)
        query = "select book_id " + column_str + " from books;"
    st.write(query)

    try : 
        # 1. 커넉터로부터 커넥션을 받는다.
        connection = mysql.connector.connect(
            host = 'database-2.ceq6zvnkjznb.us-east-2.rds.amazonaws.com',
            database = 'instar_pri',
            user = 'streamlit',
            password = 'dhghfk28'
        )

        if connection.is_connected() :
            cursor = connection.cursor(dictionary= True)
        #2. 쿼리 만들기
            cursor.execute(query)

            #3. select 이므로, fetchall한다
            results = cursor.fetchall()

            # 파이썬의 리스트 + 딕셔너리 조합을 json형식으로 바꾸는 것.
            json_results = json.dumps(results)
            
            df = pd.read_json(json_results)
            st.dataframe(df)
            


    except Error as e :
            print('디비 관련 에러 발생', e)
        
    finally :
        # 5. 모든 데이터베이스 실행 명령을 전부 끝냈으면,
        #    커서와 커넥션을 모두 닫아준다.
        cursor.close()
        connection.close()
        print("MySQL 커넥션 종료")
