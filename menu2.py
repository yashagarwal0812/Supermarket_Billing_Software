def menu2():
    import mysql.connector
    connection = mysql.connector.connect(host='localhost', database='SCHOOL', user='root', password='root')

    while (True):
        try:
            id1 = int(input("Enter The Product ID = "))
            break
        except ValueError:
            print("Enter A Valid Value")
            
    name1 = (input("Enter The Name Of The Product = "))
    
    company1 = str(input("Enter The Company Name Of The Product = "))
    
    while (True):
        try:
            mrp = int(input("Enter The MRP Of The Product = "))
            break
        except ValueError:
            print("Enter A Valid Value")
       
    while (True):
        try:
            gst_rate = int(input("Enter The GST Rate = "))
            break
        except ValueError:
            print("Enter A Valid Value")
        
    while (True):
        try:
            discount_rate = int(input("Enter The Discount Rate = "))
            break
        except ValueError:
            print("Enter A Valid Value")
        
    while (True):
        try:
            inventory = int(input("Enter The Inventory Of This Product = "))
            break
        except ValueError:
            print("Enter A Valid Value")
        
    
    sql2 = "insert into products values (%s, %s, %s, %s, %s, %s, %s)"
    cursor = connection.cursor()
    cursor.execute(sql2, (id1, name1, company1, mrp, gst_rate, discount_rate, inventory))
    connection.commit()

    print('*' * 110)
    print("The Product Has Been Added In The Database")
    print('*' * 110, '\n\n')

    return
