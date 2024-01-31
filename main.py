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
            else:
                print("Invalid option. Please enter a valid option number.")

    except ValueError as ve:
        print(f"Invalid input: {ve}")

    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    main()