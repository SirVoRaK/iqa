from mysql import connector

#host = 'mysql.rodolfoi.tech'
host = 'localhost'
username = 'rodolfo_infantini'
password = '12345678'
database = 'projeto_integrador_1'
def get_connection():
    if get_connection.connection == None:
        get_connection.connection = connector.connect(host=host, user=username, passwd=password, database=database)
    return get_connection.connection
get_connection.connection = None

def to_dict(result, columns):
    rows = []
    for i in range(len(result)):
        rows.append({})
        for j in range(len(columns)):
            rows[i][columns[j]] = result[i][j]
    return rows


def get_all_amostras():
    connection = get_connection()
    cursor = connection.cursor()
    query = 'SELECT id, mp10, `mp2.5`, o3, co, no2, so2 FROM amostras'
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()

    poluentes = ['id', 'mp10', 'mp2.5', 'o3', 'co', 'no2', 'so2']
    return to_dict(result, poluentes)

def save_amostra(amostra):
    connection = get_connection()
    cursor = connection.cursor()
    query = 'INSERT INTO amostras (mp10, `mp2.5`, o3, co, no2, so2) VALUES (%s, %s, %s, %s, %s, %s)'
    cursor.execute(query, (amostra['mp10'], amostra['mp2.5'], amostra['o3'], amostra['co'], amostra['no2'], amostra['so2']))
    connection.commit()
    cursor.close()

def update_amostra(id, amostra):
    connection = get_connection()
    cursor = connection.cursor()
    query = 'UPDATE amostras SET mp10 = %s, `mp2.5` = %s, o3 = %s, co = %s, no2 = %s, so2 = %s WHERE id = %s'
    cursor.execute(query, (amostra['mp10'], amostra['mp2.5'], amostra['o3'], amostra['co'], amostra['no2'], amostra['so2'], id))
    connection.commit()
    cursor.close()

def delete_amostra(id):
    connection = get_connection()
    cursor = connection.cursor()
    query = 'DELETE FROM amostras WHERE id = %s'
    cursor.execute(query, (id,))
    connection.commit()
    cursor.close()

def get_all_columns_avarage(result):
    if len(result) == 0:
        return {}

    avg = {}
    result_qnt = len(result)
    for col in result[0].keys():
        if col == 'id':
            continue
        sum = 0
        for row in range(result_qnt):
            sum += result[row][col]
        avg[col] = sum / result_qnt

    return avg
