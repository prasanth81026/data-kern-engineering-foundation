quantity = 110
stock_available = 100
payment_completed = True
if quantity > stock_available:
    print("out of stock")
elif payment_completed == False:
    print("payment pending")
else:
    print("order confirmed")
