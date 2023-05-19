def menu7():
    import mysql.connector
    connection = mysql.connector.connect(host='localhost', database='SCHOOL', user='root', password='root')
    
    while (True):
        try:
            billno1 = int(input("Enter The Bill No. = "))
            break
        except ValueError:
            print("Enter A Valid Value")
        
    sql16 = 'drop table billno_%s' %billno1
    cursor = connection.cursor()
    cursor.execute(sql16)
    connection.commit()
    print('*' * 110)
    print("The Bill Has Been Deleted")
    print('*' * 110, '\n\n')
    
    return
