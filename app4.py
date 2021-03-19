import streamlit as st
from my_select import run_select
from my_delete import run_delete
from my_insert import run_insert
from my_update import run_update

def main():
    st.title('MySQL 연동 프로젝뚜')
    menu = ['원하는 작업을 선택하세요', 'Select', 'Insert', 'Update', 'Delete'] 
    sel_menu = st.sidebar.selectbox("메뉴", menu)
  
    if sel_menu == 'Select':
        run_select()
    if sel_menu == 'Insert':
        run_insert()
    if sel_menu == 'Delete':
        run_delete()
    if sel_menu == 'Update':
        run_update()

if __name__ == '__main__':
    main()