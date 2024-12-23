import mysql.connector

# Connect to the database
con = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin'
)
cur = con.cursor()

# Create the database if it doesn't exist
cur.execute("CREATE DATABASE IF NOT EXISTS food_service")
cur.execute("USE food_service")

# Create branch_itanagar table if it doesn't exist
cur.execute("""
CREATE TABLE IF NOT EXISTS branch_itanagar (
    sno INT,
    products VARCHAR(20),
    cost INT
)
""")

# Insert initial data into branch_itanagar table
sql = "SELECT * FROM branch_itanagar"
cur.execute(sql)
res = cur.fetchall()
if res == []:
    cur.execute("INSERT INTO branch_itanagar VALUES (1, 'cake', 50)")
    cur.execute("INSERT INTO branch_itanagar VALUES (2, 'pastry', 20)")
    cur.execute("INSERT INTO branch_itanagar VALUES (3, 'juice', 60)")
    cur.execute("INSERT INTO branch_itanagar VALUES (4, 'butter', 20)")
    cur.execute("INSERT INTO branch_itanagar VALUES (5, 'cheese', 30)")
    con.commit()

# Create flavours table if it doesn't exist
cur.execute("""
CREATE TABLE IF NOT EXISTS flavours (
    sno INT,
    varities VARCHAR(20)
)
""")

# Insert initial data into flavours table
sql = "SELECT * FROM flavours"
cur.execute(sql)
res = cur.fetchall()
if res == []:
    cur.execute("INSERT INTO flavours VALUES (1, 'Vanilla')")
    cur.execute("INSERT INTO flavours VALUES (2, 'Chocolate')")
    cur.execute("INSERT INTO flavours VALUES (3, 'Strawberry')")
    cur.execute("INSERT INTO flavours VALUES (4, 'Butter_scotch')")
    cur.execute("INSERT INTO flavours VALUES (5, 'Jasmine')")
    con.commit()

# Function to display items in the shop
def items():
    print("Items in the shop:")
    sql = "SELECT * FROM branch_itanagar"
    cur.execute(sql)
    res = cur.fetchall()
    for item in res:
        print(item)

# Call the function to display items
items()


import mysql.connector

# Connect to the database
con = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin'
)
cur = con.cursor()
cur.execute("USE food_service")

# ITEMS IN SHOP
def items():
    print("Items in the shop: ")
    sql = "SELECT * FROM branch_itanagar"
    cur.execute(sql)
    res = cur.fetchall()
    for serial_no, products, cost in res:
        print(serial_no, ":\t", products, ":\t", 'cost', cost)

# VARIETIES OF CAKE
def item():
    print("Varieties available for Cakes: ")
    s = "SELECT * FROM flavours"
    cur.execute(s)
    rs = cur.fetchall()
    for serial_no, varieties in rs:
        print(serial_no, ":\t", varieties)

# USER INTERFACE
def for_order():
    print("What do you want to order?")
    items()
    d = int(input("Enter your serial No of the item to buy: "))
    if d == -1:
        print("Which cake do you want?")
        item()
        print("### NOTE: All Varieties Of Cake Have Same Cost As That Of Cake ###")
        print("Choose which cake you want:")
        ck = int(input("Enter your choice: "))
        if ck == 1:
            print("How much quantity of Vanilla cake do you want?")
            qty = int(input("Enter Qty: "))
            print("You have successfully ordered your item!")
            print("\n")
            da = cur.execute("SELECT cost FROM branch_itanagar WHERE products='cake'")
            da = cur.fetchall()
            da = da[0][0]
            c = int(da)
            print("Total Quantity of Vanilla Cake:", qty)
            print("Total amount:", qty * c)
            print("\n")
        elif ck == 2:
            print("How much quantity of Chocolate cake do you want?")
            qty = int(input("Enter Qty: "))
            print("You have successfully ordered your item!")
            print("\n")
            da = cur.execute("SELECT cost FROM branch_itanagar WHERE products='cake'")
            da = cur.fetchall()
            da = da[0][0]
            c = int(da)
            print("Total Quantity of Chocolate Cake:", qty)
            print("Total amount:", qty * c)
            print("\n") 
        elif ck == 3:
            print("How much quantity of Strawberry cake do you want?")
            qty = int(input("Enter Qty: "))
            print("You have successfully ordered your item!")
            print("\n")
            da = cur.execute("SELECT cost FROM branch_itanagar WHERE products='cake'")
            da = cur.fetchall()
            da = da[0][0]
            c = int(da)
            print("Total Quantity of Strawberry Cake:", qty)
            print("Total amount:", qty * c)
            print("\n")
        elif ck == 4:
            print("How much quantity of Butter_scotch cake do you want?")
            qty = int(input("Enter Qty: "))
            print("You have successfully ordered your item!")
            print("\n")
            da = cur.execute("SELECT cost FROM branch_itanagar WHERE products='cake'")
            da = cur.fetchall()
            da = da[0][0]
            c = int(da)
            print("Total Quantity of Butter_scotch Cake:", qty)
            print("Total amount:", qty * c)
            print("\n")
        elif ck == 5:
            print("How much quantity of Jasmine cake do you want?")
            qty = int(input("Enter Qty: "))
            print("You have successfully ordered your item!")
            print("\n")
            da = cur.execute("SELECT cost FROM branch_itanagar WHERE products='cake'")
            da = cur.fetchall()
            da = da[0][0]
            c = int(da)
            print("Total Quantity of Jasmine Cake:", qty)
            print("Total amount:", qty * c)
            print("\n")
   elif d == 2:
        print("How much pastry do you want?")
        past = int(input("Enter Quantity of pastry: "))
        print("You have successfully ordered", past, "pastry")
        d = cur.execute("SELECT cost FROM branch_itanagar WHERE products='pastry'")
        d = cur.fetchall()
        d = d[0][0]
        c = int(d)
        print("\n")
        print("Total quantity of pastry:", past)
        print("Total amount =", past * c)
        print("\n")
    elif d == 3:
        print("How much juice do you want?")
        jus = int(input("Enter your Qty of Juice: "))
        print("You have successfully ordered", jus, "juice")
        d = cur.execute("SELECT cost FROM branch_itanagar WHERE products='juice'")
        d = cur.fetchall()
        d = d[0][0]
        c = int(d)
        print("\n")
        print("Total quantity of Juice:", jus)
        print("Total amount =", jus * c)
        print("\n"
    elif d == 4:
        print("How much butter do you want?")
        but = int(input("Enter Quantity of Butter: "))
        print("You have successfully ordered", but, "Butter")
        d = cur.execute("SELECT cost FROM branch_itanagar WHERE products='butter'")
        d = cur.fetchall()
        d = d[0][0]
        c = int(d)
        print("\n")
        print("Total quantity of butter:", but)
        print("Total amount =", but * c)
        print("\n")
    elif d == 5:
        print("How much cheese do you want?")
        che = int(input("Enter your choice: "))
        print("You have successfully ordered", che, "cheese")
        d = cur.execute("SELECT cost FROM branch_itanagar WHERE products='cheese'")
        d = cur.fetchall()
        d = d[0][0]
        c = int(d)
        print("\n")
        print("Total quantity of cheese:", che)
        print("Total amount =", che * c)
        print("\n
# BILLING CODE
def Bill():
    print("....................")
    print("YOUR BILL")
    print("....................")
    print("Customer's name:", name)
    print("Contact no:", phone)

def bill():
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ THANK YOU FOR ORDERING THESE ITEMS @@@@@@@@@@@")
    print("@@@@@@@@ VISIT US AGAIN @@@@@@@@")

# ENTRANCE CODE
print(" Welcome ")
print("To")
print("Bakery Management System")
print("Made By - Nishtha Singh")
print("\n")
print("\n")
print("\n")
print("\n")

name = input("Enter your name: ")
phone = int(input("Enter your phone number: "))

# MAIN CODE
def Main():
    ch = 'Y'
    while ch != 'N' and ch != 'n':
        def funct():
            print("\n\nPLEASE CHOOSE\n1 FOR CUSTOMER \n2 FOR EXIT:\n\n")
            choice = int(input("Enter your choice: "))
            if choice == 2:
                return
            elif choice == 1:
                print('press 1 to see the MENU')
                print('press 2 to order any item')
                print('press 3 to EXIT')
                e = int(input('Enter your choice: '))
                if e == 3:
                    return
                elif e == 1:
                    print("Items in the shop:")
                    items()
                    funct()
                elif e == 2:
                    for_order()
                else:
                    print("Wrong Input")
                    funct()
        funct()
        ch = input("ARE YOU SURE TO EXIT FROM PROGRAM (Y/N)? ")
        if ch == 'y' or ch == 'Y':
            exit()

Main()
# BILLING CODE
def Bill():
    print("....................")
    print("YOUR BILL")
    print("....................")
    print("Customer's name:", name)
    print("Contact no:", phone)

def bill():
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ THANK YOU FOR ORDERING THESE ITEMS @@@@@@@@@@@")
    print("@@@@@@@@ VISIT US AGAIN @@@@@@@@")

# ENTRANCE CODE
print(" Welcome ")
print("To")
print("Bakery Management System")
print("Made By - Nishtha Singh")
print("\n")
print("\n")
print("\n")
print("\n")

name = input("Enter your name: ")
phone = int(input("Enter your phone number: "))

# MAIN CODE
def Main():
    ch = 'Y'
    while ch != 'N' and ch != 'n':
        def funct():
            print("\n\nPLEASE CHOOSE\n1 FOR CUSTOMER \n2 FOR EXIT:\n\n")
            choice = int(input("Enter your choice: "))
            if choice == 2:
                return
            elif choice == 1:
                print('press 1 to see the MENU')
                print('press 2 to order any item')
                print('press 3 to EXIT')
                e = int(input('Enter your choice: '))
                if e == 3:
                    return
                elif e == 1:
                    print("Items in the shop:")
                    items()
                    funct()
                elif e == 2:
                    for_order()
                else:
                    print("Wrong Input")
                    funct()
        funct()
        ch = input("ARE YOU SURE TO EXIT FROM PROGRAM (Y/N)? ")
        if ch == 'y' or ch == 'Y':
            exit()

Main()




