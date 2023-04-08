import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = "./lms.db"

    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS books (
                                        book_id integer PRIMARY KEY,
                                        book_name text NOT NULL,
                                        book_author text,
                                        book_edition text,
                                        book_price text,
                                        date_of_purchase DATETIME,
                                        status text
                                    ); """

    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS issued_book (
                                    book_id integer,
                                    issued_to integer,
                                    issued_on DATETIME NOT NULL,
                                    expired_on DATETIME NOT NULL,
                                    is_miscellaneous integer DEFAULT 0 NOT NULL,
                                    FOREIGN KEY (book_id)
                                    REFERENCES books (book_id)
                                        ON UPDATE CASCADE
                                        ON DELETE CASCADE
                                    FOREIGN KEY (issued_to)
                                    REFERENCES student (id)
                                        ON UPDATE CASCADE
                                        ON DELETE CASCADE
                                );"""
    
    sql_create_tasks1_table = """CREATE TABLE IF NOT EXISTS student (
                                    id integer PRIMARY KEY,
                                    name integer NOT NULL,
                                    class text NOT NULL
                                );"""
    
    sql_create_tasks2_table = """CREATE TABLE IF NOT EXISTS fine_details (
                                    book_id integer,
                                    student_id integer,
                                    issued_on DATETIME NOT NULL,
                                    returned_date DATETIME NOT NULL,
                                    total_fine integer,
                                    no_of_day integer,
                                    FOREIGN KEY (book_id)
                                    REFERENCES books (book_id)
                                        ON UPDATE CASCADE
                                        ON DELETE CASCADE
                                    FOREIGN KEY (student_id)
                                    REFERENCES student (id)
                                        ON UPDATE CASCADE
                                        ON DELETE CASCADE
                                );"""
    
    
    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_projects_table)

        # create tasks table
        create_table(conn, sql_create_tasks_table)
        create_table(conn, sql_create_tasks1_table)
        create_table(conn, sql_create_tasks2_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()