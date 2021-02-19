import psycopg2


def create_table():
    conn = psycopg2.connect(
        "dbname='db' user='postgres' password='postgres' host='127.0.0.1' port='5432'")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE if NOT EXISTS store( item TEXT, quantity INTEGER, price REAL)"
    )

    conn.commit()
    conn.close()


def insert(item, quantity, price):
    conn = psycopg2.connect(
        "dbname='db' user='postgres' password='postgres' host='127.0.0.1' port='5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)", (item, quantity, price))
    conn.commit()
    conn.close()


def view():
    conn = psycopg2.connect(
        "dbname='db' user='postgres' password='postgres' host='127.0.0.1' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(item):
    conn = psycopg2.connect(
        "dbname='db' user='postgres' password='postgres' host='127.0.0.1' port='5432'")
    cur = conn.cursor()
    cur.execute("delete FROM store where item=%s", (item,))
    conn.commit()
    conn.close()


def update(quantity, price, item):
    conn = psycopg2.connect(
        "dbname='db' user='postgres' password='postgres' host='127.0.0.1' port='5432'")
    cur = conn.cursor()
    cur.execute("update store set quantity=%s, price=%s where item=%s",
                (quantity, price, item))
    conn.commit()
    conn.close()


create_table()
# insert('Cup head', 8, 10.5)
# delete("Coffe Cup")
# update(11, 6, "Cup head")
print(view())
