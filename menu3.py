def menu3():
    import mysql.connector
    connection = mysql.connector.connect(host='localhost', database='SCHOOL', user='root', password='root')
    
    while (True):
        try:
            id1 = int(input("Please Enter The ID Of The Product You Want To Delete = "))
            break
        except ValueError:
            print("Enter A Valid Value")
       
    sql3 = "delete from products where id = %s" %(id1)
    cursor = connection.cursor()
    cursor.execute(sql3)
    connection.commit()
    print('*' * 110)
    print("The Product Has Been Deleted From The Database")
    print('*' * 110, '\n\n')

    return
