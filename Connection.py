import psycopg2


def conekta():
    con = psycopg2.connect(
        host="000",
        database="hp",
        user="hopital",
        password="000"
    )
    return con
