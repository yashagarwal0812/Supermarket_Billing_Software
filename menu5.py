def menu5():
    import mysql.connector
    connection = mysql.connector.connect(host='localhost', database='SCHOOL', user='root', password='root')

    sql1 = 'select count(id) from products'
    cursor = connection.cursor()
    cursor.execute(sql1)
    record1 = cursor.fetchall()
    a = record1[0]
    b = a[0]

    while(True):
        while (True):
            try:
                billno = int(input("Enter The Bill No. = "))
                break
            except ValueError:
                print("Enter A Valid Value")

        while (True):
            try:
                items = int(input("Enter The Number Of Items To Be Purchased = "))
                break
            except ValueError:
                print("Enter A Valid Value")
        
        items1 = items

        sql5 = 'create table billno_%s (id int, product varchar(25), mrp int, qty int, amount int, gst_rate int, gst int, discount_rate int, discount int, final_amount int)' %(billno)
        cursor = connection.cursor()
        cursor.execute(sql5)
        connection.commit()
    
        while items1>0:
            while (True):
                try:
                    prodid = int(input("\nEnter The Product ID = "))
                    break
                except ValueError:
                    print("Enter A Valid Value")
            
            for i in range (1, b+1, 1):
                if prodid == i:
                    sql6 = 'select * FROM PRODUCTS WHERE ID = %s' %(i)
                    cursor = connection.cursor()
                    cursor.execute(sql6)
                    record2 = cursor.fetchall()
                    for a in record2:
                        print("The Product Is - ", a[1])
                        print("The Price Is - ", a[3])
                        id1 = a[0]
                        product = a[1]
                        price = a[3]
                        gst_rate = a[4]
                        discount_rate = a[5]
                        inventory = a[6]
                    while (True):
                        try:
                            qty1 = int(input("Please Tell The Quantity To Be Purchased - "))
                            break
                        except ValueError:
                            print("Enter A Valid Value")
                    
                    amt1 = price * qty1
                    gst = (amt1*gst_rate)/100
                    discount = (amt1*discount_rate)/100
                    amtf = amt1 + gst - discount
                    inventory1 = inventory - qty1

                    if inventory1 < 0:
                        print("Total Quantity To Be Purchased Is Not In Inventory")
                        break
                    else:
                        sqla = 'update products set inventory = %s where id = %s' %(inventory1, id1)
                        cursor = connection.cursor()
                        cursor.execute(sqla)
                        connection.commit()
                    
                    print("Amount Will Be - ", amtf)
                    sql7 = 'insert into billno_%s values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
                    cursor = connection.cursor()
                    cursor.execute(sql7, (billno, i, product, price, qty1, amt1, gst_rate, gst, discount_rate, discount, amtf))
                    connection.commit()
    
            items1 -= 1

        sql8 = 'select sum(final_amount) from billno_%s' %billno
        cursor = connection.cursor()
        cursor.execute(sql8)
        final_amount = cursor.fetchall()
        final_amount1 = final_amount[0]
        final_amount2 = final_amount1[0]
    
        sql9 = 'select sum(qty) from billno_%s' %billno
        cursor = connection.cursor()
        cursor.execute(sql9)
        qty = cursor.fetchall()
        qty1 = qty[0]
        qty2 = qty1[0]
    
        sql10 = 'select sum(amount) from billno_%s' %billno
        cursor = connection.cursor()
        cursor.execute(sql10)
        amount1 = cursor.fetchall()
        amount2 = amount1[0]
        amount3 = amount2[0]

        sql11 = 'select sum(gst) from billno_%s' %billno
        cursor = connection.cursor()
        cursor.execute(sql11)
        gst1 = cursor.fetchall()
        gst2 = gst1[0]
        gst3 = gst2[0]

        sql12 = 'select sum(discount) from billno_%s' %billno
        cursor = connection.cursor()
        cursor.execute(sql12)
        discount1 = cursor.fetchall()
        discount2 = discount1[0]
        discount3 = discount2[0]

        sql13 = 'select * from billno_%s' %billno
        cursor = connection.cursor()
        cursor.execute(sql13)
        record3 = cursor.fetchall()
        
        print('\n\n')
        print('*' * 110)
        print('\t\t\tAGARWAL SUPERMARKET')
        print("\t\t\t\t(Bill No. =", billno, ")")
        print('*' * 110)
        print('Id \t Name \t\t Qty \t Amt \t GST \t Disc \t Total')
        for row1 in record3:
            
            print( row1[0], '\t', row1[1], '\n\t\t\t', row1[3], '\t',  row1[4], '\t', row1[6], '\t', row1[8], '\t',  row1[9])
        print('*' * 110)
        
        print('\t\t\t', qty2,'\t', amount3, '\t', gst3, '\t', discount3, '\t', final_amount2)
        print('*' * 110)
        paid = int(input("Enter The Amount Paid = "))
        change = paid - final_amount2
        print("Change =", change)
        print('*' *110, '\n\n')
        
        return
