def menu1():
    import mysql.connector
    connection = mysql.connector.connect(host='localhost', database='SCHOOL', user='root', password='root')
    
    sql_select_query = 'select ID, NAME, COMPANY, MRP, INVENTORY from products'
    cursor = connection.cursor()
    cursor.execute(sql_select_query)
    records = cursor.fetchall()

    sql1 = 'select count(id) from products'
    cursor = connection.cursor()
    cursor.execute(sql1)
    record1 = cursor.fetchall()
    a = record1[0]
    b = a[0]

    print('\n\n')
    print('*' * 110)
    print('\t\t\tAGARWAL SUPERMARKET')
    print('*' * 110)
    print('ID\t',  'NAME', "(",  'COMPANY', ")",  '\n\t\t\t\t\tMRP\t', 'INVENTORY')
    print('*' * 110)
    for row in records:
        print(row[0], '\t', row[1], "(", row[2], ")",  '\n\t\t\t\t\t', row[3], '\t', row[4])
    print('*' * 110, '\n\n')
    
    return
        
