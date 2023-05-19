def menu8():
    import mysql.connector
    connection = mysql.connector.connect(host='localhost', database='SCHOOL', user='root', password='root')
 
    while (True):
        try:
            id2 = int(input("Enter The ID Of The Product Of Which The inventory Is To Be Increased = "))
            break
        except ValueError:
            print("Enter A Valid Value")

    while (True):
        try:
            inventory7 = int(input('Enter The Quantity To Be Added = '))
            break
        except ValueError:
            print("Enter A Valid Value")
        
    sql17 = 'select * FROM PRODUCTS WHERE ID = %s' %(id2)
    cursor = connection.cursor()
    cursor.execute(sql17)
    record7 = cursor.fetchall()
    for b in record7:
        inventory2 = b[6]
    inventory3 = inventory7 + inventory2
    sqlb = 'update products set inventory = %s where id = %s' %(inventory3, id2)
    cursor = connection.cursor()
    cursor.execute(sqlb)
    connection.commit()
    print('*' * 110)
    print("Database Updated")
    print('*' * 110, '\n\n')
    
    return        
