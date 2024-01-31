from manager import Manager
from config import Config

def main():
    config_obj = Config()
    config_obj.create_files()  # Call the create_files method on an instance of Config

    try:
        manager = Manager(config_obj)
        data = manager.load_data()

        while True:
            v_option = int(input("\n\nSelect one of the following options:\n"
                                 "1 - Balance\n"
                                 "2 - Sale\n"
                                 "3 - Purchase\n"
                                 "4 - Account\n"
                                 "5 - List\n"
                                 "6 - Warehouse\n"
                                 "7 - Review\n"
                                 "0 - End\n\n"))


            if v_option == 0:
                manager.save_data(data)
                print("\nThank you for using our system.\n\n")
                exit()
            elif 1 <= v_option <= 7:
                manager.assign(v_option, data)
            # elif v_option == 1:
            #     data = manager.f_balance(data)
            #     print(f"Your new balance is: {data['v_balance']}")
            # elif v_option == 2:
            #     data = manager.f_sale(data)
            # elif v_option == 3:
            #     data = manager.f_purchase(data)
            # elif v_option == 4:
            #     data = manager.f_account(data)
            # elif v_option == 5:
            #     data = manager.f_list(data)
            # elif v_option == 6:
            #     data = manager.f_warehouse(data)
            # elif v_option == 7:
            #     data = manager.f_review(data)
            else:
                print("Invalid option. Please enter a valid option number.")

            #elif v_option == "balance":
            #    data = manager.assign("balance", action=1, value=100)

            #elif v_option == "sale":
            #    data = manager.f_sale(data)
            #    data = manager.assign("sale", name="a", quantity=2)
            #data = manager.assign("sale", name="a", quantity=2)
    except ValueError as ve:
        print(f"Invalid input: {ve}")

    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    main()



# def print_menu():
#     print("\nSelect one of the following options:")
#     print("1 - Balance")
#     print("2 - Sale")
#     print("3 - Purchase")
#     print("4 - Account")
#     print("5 - List")
#     print("6 - Warehouse")
#     print("7 - Review")
#     print("0 - End")
#
# def main():
#     # Initialize data
#     # Config.create_files(self, "balance_file", "warehouse_file", "review_file")
#     # data = Manager.load_data(self)
#     #config = Config()
#     #manager = Manager(config)
#     #data = Manager.load_data()
#
#     # Initialize data
#     create_files()
#
#     try:
#         manager = Manager()
#         data = manager.load_data()
#
#         while True:
#             print_menu()
#             try:
#                 v_option = int(input("\nEnter option number: "))
#
#                 if v_option == 0:
#                     Manager.save_data(data)
#                     print("\nThank you for using our system.\n\n")
#                     sys.exit()
#
#                 elif 1 <= v_option <= 7:
#                     operation = Manager.get_operation(v_option)
#                     print("You chose the option {} to {}.".format(v_option, operation))
#                     data = getattr(Manager, operation)(data)
#
#                 else:
#                     print("Invalid option. Please enter a valid option number.")
#
#             except ValueError:
#                 print("Invalid input. Please enter a valid option number.")
#
#     except Exception as e:
#         print(f"An Error occurred: {e}")
#
#
# if __name__ == "__main__":
#     main()
