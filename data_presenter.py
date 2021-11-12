#problem 2
cupcakes_invoices = open('./CupcakeInvoices.csv')
#problem 3
# for row in cupcakes_invoices:
    # print(row)
#problem 4
for row in cupcakes_invoices:
    values = row.split(',')
    print(values[2])
#problem 5
for row in cupcakes_invoices:
    values = row.split(',')
# print(total)
# #problem 6
# total = 0




cupcakes_invoices.close()