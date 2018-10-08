#Local Variable   Global Variable

def discount(price, rate):
    old_price = 60
    print('1old_price : ', old_price)
    final_price = price*rate#Local Variale
    return final_price

old_price = float(input('old_price : '))
rate = float(input('the rate : '))
new_price = discount(old_price, rate)
print('2old_price : ', old_price)
print('new price: ', new_price)

#print(final_price)


