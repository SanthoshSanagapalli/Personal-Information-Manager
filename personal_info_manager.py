# Personal Information Manager - Beginner Level

people = []

while True:
    print("\n--- Personal Information Manager ---")
    print("1. Add Person")
    print("2. Show All People")
    print("3. View Person Details")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        city = input("Enter your city: ")
        hobbies = input("Enter your hobbies (comma separated): ")

        person = {
            "name": name,
            "age": age,
            "city": city,
            "hobbies": hobbies.split(",")
        }

        people.append(person)
        print("✅ Person added successfully!")

    elif choice == "2":
        if not people:
            print("No records found.")
        else:
            print("\nList of People:")
            for i, p in enumerate(people, 1):
                print(f"{i}. {p['name']}")

    elif choice == "3":
        search_name = input("Enter the name to view details: ")
        found = False
        for p in people:
            if p["name"].lower() == search_name.lower():
                print("\n--- Person Details ---")
                print("Name:", p["name"])
                print("Age:", p["age"])
                print("City:", p["city"])
                print("Hobbies:", ", ".join(p["hobbies"]))
                found = True
                break
        if not found:
            print("Person not found.")

    elif choice == "4":
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
