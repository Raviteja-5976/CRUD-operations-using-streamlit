# CRUD-operations-using-streamlit
An example code for CRUD operations in streamlit with mysql database 

### +-------+--------------+------+-----+---------+-------+
### | Field | Type         | Null | Key | Default | Extra |
### +-------+--------------+------+-----+---------+-------+
### | id    | int          | NO   | PRI | NULL    |       |
### | name  | varchar(100) | YES  |     | NULL    |       |
### +-------+--------------+------+-----+---------+-------+

The above database is the one that I have used to develop the structure of the database

# COMMANDS : 
## CREATE THE DATABASE : 
CREATE DATABASE database-name ;

## CREATE THE TABLE :
CREATE TABLE table_name (id int PRIMARY KEY, name varchar(100));

##In the program I have given the database name as 'gdsc_data' and the table name as 'stu'
