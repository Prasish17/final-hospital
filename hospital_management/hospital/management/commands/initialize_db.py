import psycopg2

hostname = 'localhost'
database = 'project_db'
username = 'postgres'
pwd = 'prasish@0912'
port_id = 5432

def get_db_connection():
    return psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id
    )

def tables():
    conn = None
    cur = None
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        with open('sql/create_tables.sql', 'r') as file:
            cur.execute(file.read())
        conn.commit()
        print("successful")
    except Exception as error:
        print(f'the error is {error}') 
    finally:
        if conn is not None:
            conn.close()
        if cur is not None:
            cur.close()

if __name__ == "__main__":
    tables()
