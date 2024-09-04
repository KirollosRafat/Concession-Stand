## ----------------Concession Stand------------------- ##

Concession_stand = {"salt popcorn" : 30, 
    "carmel popcorn": 35, 
    "soda": 25, 
    "pizza": 15,
    "candy": 20, 
    "water": 10}


def Display_Menu():
    print("--------------The Concession Stand--------------\n")
    for element in Concession_stand.items():
        print(f"{element[0]} : {element[1]} L.E.")
        print("-"*30)


def get_order():
    order_list = []
    while True:
        order = input("What\'s your order: ").lower()
        order_list.append(order)
        order_end = input("Anything else(Y/N): ").lower()
        if order_end == 'n':
            break

    return order_list    


def Display_Order(order_list):
    print("------------------Your Order------------------")
    for order in order_list:
        print(f"{order} : {Concession_stand[order]} L.E.")


def order_cost(order_list):
    cost = 0
    for order in  order_list:
        cost += Concession_stand[order]

    print(f"{cost} L.E. is your total order cost.")


def main():
    Display_Menu()
    Customer_order= get_order()
    Display_Order(Customer_order)
    order_cost(Customer_order)
    print("Have a nice day!")




if __name__ == "__main__":
    main()