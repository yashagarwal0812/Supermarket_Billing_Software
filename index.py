import mysql.connector

connection = mysql.connector.connect(host='localhost', database='SCHOOL', user='root', password='root')

choice1111 = 'Y'

from menu1 import menu1
from menu2 import menu2
from menu3 import menu3
from menu4 import menu4
from menu5 import menu5
from menu6 import menu6
from menu7 import menu7
from menu8 import menu8

while choice1111 == 'y' or choice1111=='Y':

    # MENU ITEMS
    print('*' * 110)
    print('\t\t\tAGARWAL SUPERMARKET')
    print('*' * 110)
    print('\t\t\t\tMENU')
    print('*' * 110)
    print('Press 1 To Display The Products Database')
    print('Press 2 To Add Products In The Database')
    print('Press 3 To Delete Products From The Database')
    print('Press 4 To Get A List Of All The Bills Issued')
    print('Press 5 To Create A Bill')
    print('Press 6 To Fetch An Old Bill')
    print('Press 7 To Delete An Old Bill')
    print('Press 8 To Increase Quantity In Inventory')
    print('Press 9 To Exit The System')
    print('*' * 110)
    print('\n\n')

    menu = int(input('Enter Your Choice = '))

    sql_select_query = 'select ID, NAME, COMPANY, MRP, INVENTORY from products'
    cursor = connection.cursor()
    cursor.execute(sql_select_query)
    records = cursor.fetchall()
    

    if menu == 1:      #To Display All products
        menu1()

    if menu == 2:      #To Add Product
        menu2()

    if menu == 3:     #To Delete Product
        menu3()

    if menu == 4:      #To Get The List Of Bills
        menu4()

    if menu == 5:      #To Create A Bill
        menu5()

    if menu == 6:      #To Fetch An Old Bill
        menu6()

    if menu == 7:      #To Delete A Bill
        menu7()

    if menu == 8:      #To Increase Inventory
        menu8()

    if menu == 9:      #To Exit
        break
    
    else:
        choice1111 = input("Press Y to Use Again Or N to Exit - ")
        
else:
    print('*' * 110)

        
    
    
    
