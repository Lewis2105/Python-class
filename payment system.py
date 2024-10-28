from datetime import datetime

bookID = input("Enter the book ID: ")

dueDate_input = input("Enter due date (YYYY-MM-DD): ")
returnDate_input = input("Enter return date (YYYY-MM-DD): ")

dueDate = datetime.strptime(dueDate_input, '%Y-%m-%d')
returnDate = datetime.strptime(returnDate_input, '%Y-%m-%d')

daysOverdue = (returnDate - dueDate).days

if daysOverdue <= 0:
    fineRate = 0
    fineAmount = 0
    print(f"\nBook returned on time or before due date. No fine.")
else:
    
    if daysOverdue <= 7:
        fineRate = 20
    elif 8 <= daysOverdue <= 14:
        fineRate = 50
    else:
        fineRate = 100

    fineAmount = daysOverdue * fineRate

    print(f"Book ID: {bookID}")
    print(f"Due Date: {dueDate.strftime('%Y-%m-%d')}")
    print(f"Return Date: {returnDate.strftime('%Y-%m-%d')}")
    print(f"Days Overdue: {daysOverdue}")
    print(f"Fine Rate: Ksh {fineRate} per day")
    print(f"Total Fine Amount: Ksh {fineAmount}")