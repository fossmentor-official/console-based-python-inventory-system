from inventory_system import InventorySystem

def main():
    system = InventorySystem()
    while True:
        print("\n--- Welcome to Inventory System ---")
        print("1. Login")
        print("2. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            if system.login():
                system.show_main_menu()
        elif choice == "2":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()