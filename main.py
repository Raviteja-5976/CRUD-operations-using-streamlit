import streamlit as st
import mysql.connector

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "*********",
    "database": "gdsc_data"
}

# Establish the connection
connection = mysql.connector.connect(**db_config)

# Create a cursor object
cursor = connection.cursor()


def show():
    
    display = '''
        SELECT * from stu
    '''
    cursor.execute(display)
    save_display = cursor.fetchall()
    for sd in save_display : 
        ids = st.write(f'id : {sd[0]}')
        name = st.write(f'name : {sd[1]}')
        st.write('-' * 50)

def select_show():
  #function to show the data
    ids = st.text_input('Enter ID')
    #mysql command to select the data
    display = '''
        SELECT id, name from stu WHERE id = %s
    '''
  # we use %s to get the input outside from the command (it can be in the code or from user)
    value = ids 
  # cursor.execute is to execute the mysql command
    cursor.execute(display,value)
  # we use fetchall / fetchone to save the data in a variable
    save_display = cursor.fetchall()
    st.write(save_display)

def insert():
  #function to insert data
    name = st.text_input('Enter Name : ')
    ids = st.text_input('Enter ID:')

    data_in = '''
        INSERT INTO stu(id , name) VALUES (%s, %s)
    '''
    value = (ids, name)
    if st.button("Insert"):
      # cursor.execute is to execute the mysql command
        cursor.execute(data_in,value)
      # connection.commit is to save the changes
        connection.commit()
        st.success('Data Inserted')

def update():
  #function to update data
    command = '''SELECT id from stu'''
    cursor.execute(command)
    id_data = cursor.fetchall()
    select_id = st.selectbox('Id: ', [ids for ids in id_data])

    if select_id : 
        updare_name = st.text_input('Enter Name: ')

        if st.button('Update'):
            update_comd = '''
            UPDATE stu
            SET name = %s
            WHERE id = %s
            '''
            val = (updare_name, select_id[0])
            cursor.execute(update_comd, val )
            connection.commit()
            st.success('Data Updated')

def delete():
  #function for deleting data
    command = '''SELECT id from stu'''
    cursor.execute(command)
    id_data = cursor.fetchall()
    select_id = st.selectbox('Id: ', [ids for ids in id_data]) 
    if select_id :
        display = '''
            SELECT id , name from stu where id = %s
        '''
        cursor.execute(display,select_id)
        save_display = cursor.fetchall()
        for sd in save_display : 
            st.write(f'id : {sd[0]}')
            st.write(f'name : {sd[1]}')
            st.write('-' * 50)
        if st.button('delete'):
            delete_comd = '''
                DELETE FROM stu
                WHERE id = %s
            '''
            value = select_id
            cursor.execute(delete_comd,value)
            connection.commit()
            st.success('data deleted')


def main():
    st.title('CRUD OPERATIONS')
    page = st.sidebar.selectbox('Select page', ['DISPLAY','INSERT','UPDATE','DELETE'] )

    if page == 'DISPLAY' :
        show()

    elif page == 'INSERT':
        insert()

    elif page == 'UPDATE':
        update()

    elif page == 'DELETE':
        delete()


if __name__ == "__main__":
    main()

        

        
