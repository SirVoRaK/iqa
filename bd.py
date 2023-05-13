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
    query = 'SELECT mp10, `mp2.5`, o3, co, no2, so2 FROM amostras'
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()

    poluentes = ['mp10', 'mp2.5', 'o3', 'co', 'no2', 'so2']
    return to_dict(result, poluentes)

def get_all_columns_avarage(result):
    if len(result) == 0:
        return {}

    avg = {}
    result_qnt = len(result)
    for col in result[0].keys():
        sum = 0
        for row in range(result_qnt):
            sum += result[row][col]
        avg[col] = sum / result_qnt

    return avg
