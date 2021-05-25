from .database import get_conn

def create_qualification(data):
    conn = get_conn()
    cur = conn.cursor()
    sql = """
        INSERT INTO resultados_trivial(username, score, finish_at) VALUES(?,?,?)
    """

    cur.execute(sql, data)
    conn.commit()
    return cur.lastrowid
