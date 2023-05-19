def menu6():
    import mysql.connector
    connection = mysql.connector.connect(host='localhost', database='SCHOOL', user='root', password='root')
    while (True):
        try:
            billno = int(input("Enter The Bill No. = "))
            break
        except ValueError:
            print("Enter A Valid Value")
        
    sql13 = 'select * from billno_%s' %billno
    cursor = connection.cursor()
    cursor.execute(sql13)
    record3 = cursor.fetchall()
        
    print('\n\n')
    print('*' * 110)
    print('\t\t\tAGARWAL SUPERMARKET')
    print('*' * 110)
    print('Id \t Name \t\t Qty \t Amt \t GST \t Disc \t Total')
    for row1 in record3:
            
        print( row1[0], '\t', row1[1], '\n\t\t\t', row1[3], '\t',  row1[4], '\t', row1[6], '\t', row1[8], '\t',  row1[9])

    sql14 = 'select sum(final_amount) from billno_%s' %billno
    cursor = connection.cursor()
    cursor.execute(sql14)
    final_amount = cursor.fetchall()
    final_amount1 = final_amount[0]
    final_amount2 = final_amount1[0]
    
    sql15 = 'select sum(qty) from billno_%s' %billno
    cursor = connection.cursor()
    cursor.execute(sql15)
    qty = cursor.fetchall()
    qty1 = qty[0]
    qty2 = qty1[0]

        
    print('*' * 110)
    print('Total Qty =', qty2)
    print('Grand Total =', final_amount2)
    print('*' * 110)
    print('\n\n')
    
    return
