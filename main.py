'''
Copyright © MrCreativeOP 2023-2024



Dont't take it seriously xD
'''
import mysql.connector as a

con = a.connect(host="localhost", user="root", passwd="", database="employee", buffered=True)

def npersonal():
    n = input("Enter Employee Name:")
    c = input("Enter Employee's City Name:")
    d = input("Enter Employee's D.O.B:")
    p = input("Enter Employee Phone:")

    data = (n, c, d, p)

    sql = 'insert into personal values (%s, %s, %s, %s)'
    cursor = con.cursor()
    cursor.execute(sql, data)

    con.commit()
    print("Data Entered Successfully")

def view_personal():
    sql = "select * from personal"
    cursor = con.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()

    for i in data:
        print(i)

def noffice():
    ec = input("Enter Employee Code:")
    n = input("Enter Employee Name:")
    ps = input("Enter Employee Post:")
    j = input("Enter Employee joining date:")
    bp = int(input("Enter Assigned Salary:"))

    data = (ec, n, ps, j, bp)

    sql = 'insert into office values (%s, %s, %s, %s, %s)'
    cursor = con.cursor()
    cursor.execute(sql, data)

    con.commit()
    print("Data Entered Successfully")

def view_office():
    sql = "select * from office"
    cursor = con.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()

    for i in data:
        print(i)

def nsalary():
    ec = input("Enter Employee Code:")
    v = (ec,)

    sql = "select BasicPay from office where Ecode = %s"
    cursor = con.cursor()
    cursor.execute(sql, v)
    basic_pay = cursor.fetchone()[0]

    n = input("Enter Employee Name:")
    y = input("Enter Year:")
    m = input("Enter Month:")
    wd = int(input("Enter working days:"))
    td = int(input("Enter Total Days:"))
    fp = basic_pay / td * wd

    data = (ec, n, y, m, wd, fp)

    sql = 'insert into salary values (%s, %s, %s, %s, %s, %s)'
    cursor.execute(sql, data)

    con.commit()
    print("Data Entered Successfully")

def view_salary():
    sql = "select * from salary"
    cursor = con.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()

    for i in data:
        print(i)

def main():
    print("""
    1. Add New Employee Personal Details
    2. Display Employee Personal Details
    3. Add New Employee Office Details
    4. Display Employee Office Details
    5. Enter Salary Details of Employee
    6. Display Salary Details of Employee
    7. Exit
    """)

    while True:
        choice = input("Enter Task No:")

        if choice == '1':
            npersonal()
        elif choice == '2':
            view_personal()
        elif choice == '3':
            noffice()
        elif choice == '4':
            view_office()
        elif choice == '5':
            nsalary()
        elif choice == '6':
            view_salary()
        elif choice == '7':
            print("Thank You For Visiting!")
            break
        else:
            print("Invalid Input! Try Again")

if __name__ == "__main__":
    main()
