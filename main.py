def main():
    while True:
        user_choice = input("Do you want to add a new To-Do item? (y/n) or type 'exit' to quit: ").lower()

        if user_choice == "exit":
            print("Thank you for using the To-Do program, come back again soon.")
            break

        elif user_choice == "y":
            new_item = input("Enter your new To-Do item: ")

            # append mode عشان ما يمسح القديم
            with open("to_do.txt", "a") as file:
                file.write(new_item + "\n")

            print("Item added successfully!\n")

        elif user_choice == "n":
            read_choice = input("Do you want to list your To-Do items? (y/n): ").lower()

            if read_choice == "y":
                try:
                    with open("to_do.txt", "r") as file:
                        items = file.readlines()

                        if not items:
                            print("Your To-Do list is empty.\n")
                        else:
                            print("\nYour To-Do List:")
                            for item in items:
                                print(item.strip())
                            print()

                except FileNotFoundError:
                    print("No To-Do list found yet.\n")

            elif read_choice == "n":
                print("Okay!\n")

            else:
                print("Invalid input.\n")

        else:
            print("Invalid input.\n")


# تشغيل البرنامج
main()