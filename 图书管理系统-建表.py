import pymysql

connection = pymysql.connect(
    host='10.0.0.200',
    user='fang',
    password='123456',
    port=3306,
    database='library_db'
)
cursor = connection.cursor()

create_user_table = """
CREATE TABLE IF NOT EXISTS Users(
  id INT primary key auto_increment,
  name VARCHAR(50) not null,
  email VARCHAR(100) unique not null
)"""

cursor.execute(create_user_table)

create_books_table = """
CREATE TABLE IF NOT exists Books(
  id INT primary key auto_increment,
  title VARCHAR(100) not null,
  author VARCHAR(100) ,
  status enum('available','borrowed')default 'available'
)
"""
cursor.execute(create_books_table)

create_borrow_records_table = """
create table if not exists BorrowRecords(
  id INT primary key auto_increment,
  user_id INT not null,
  book_id INT not null,
  borrow_date INT not null,
  retire_date INT not null,
  foreign key (user_id) references Users(id),
  foreign key (book_id) references Books(id)
)
"""
cursor.execute(create_borrow_records_table)

connection.commit()
cursor.close()
connection.close()
