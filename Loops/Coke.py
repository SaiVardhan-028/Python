def main():
    amount = 50
    coke(amount)

def coke(amount):
    while amount > 0:
        print("Amount Due",amount)
        coin = insert_coin()
        
        if coin == 25 or coin == 10 or coin ==5:
            amount -= coin
    print("Changed owed", -amount)
            

def insert_coin():
    return int(input("insert_coin"))
        
main()
