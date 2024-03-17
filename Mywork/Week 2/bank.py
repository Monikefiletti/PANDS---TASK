# bank.py
# This program will : - Prompt the user and read in two money amounts (in cent) 
#                     - Add the two amounts
#                     - Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 
# author: Monike Filetti

amount1= int(input("Enter price (in cent):"))
amount2= int(input("Enter price (in cent):"))
Total = (amount1+amount2)/100
formatted_result = "{:.2f}".format(Total)
print(f'The total of your purchase is €{formatted_result}\nThank you for buying with Tesco')
