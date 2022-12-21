def menu():
    print("""**************************************
    **   Welcome to the Snakes Cafe!    **
    **   Please see our menu below.     **
    **                                  **
    ** To quit at any time, type "quit" **
    **************************************
    Appetizers
    ----------
    Wings
    Cookies
    Spring Rolls
    
    Entrees
    -------
    Salmon
    Steak
    Meat Tornado
    A Literal Garden
    
    Desserts
    --------
    Ice Cream
    Cake
    Pie
    
    Drinks
    ------
    Coffee
    Tea
    Unicorn Tears
    
    ***********************************
    ** What would you like to order? **
    ***********************************""")
    order_tab = {

    }

    order = input("> ")
    if order in order_tab:
        order_tab[order] += 1
    elif order == "quit":
        exit()
    else:
        order_tab[order] = 1
    print(f"You've added {order_tab[order]} {order}!")

    repeat = True
    while repeat:
        print("Would you like to add another item? (y/n)")
        choice = input("> ")
        if choice == "y":
            print("What would you like to order?")
            order = input("> ")
            print(f"You just ordered {order}")
            if order in order_tab:
                order_tab[order] += 1
            else:
                order_tab[order] = 1
            print(f"You've added {order_tab[order]} {order}!")
        elif choice == "quit":
            exit()
        else:
            break
    print(f"Your order consists of {order_tab[order]} {order}!")

menu()

