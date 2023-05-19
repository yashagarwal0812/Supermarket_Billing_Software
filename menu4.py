def menu4():
    import mysql.connector
    connection = mysql.connector.connect(host='localhost', database='SCHOOL', user='root', password='root')

    sql4 = 'show tables'
    cursor = connection.cursor()
    cursor.execute(sql4)
    record1 = cursor.fetchall()
    print('The Bills Are =')
    for rows in record1:
        if rows[0] != 'products':
            print(rows[0])
    print('*' * 110, '\n\n')

    return
