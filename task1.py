def kwargsAcceptFun(**kwargs):

    print("Keyword arguments received:")

    if kwargs:
        for key, value in kwargs.items():
            print(f"  {key}: {value}")

        if "name" in kwargs:
            name = kwargs["name"]
            print(f"\nName found: {name}")
        else:
            print("\nName not found.")


        age = kwargs.get("age")
        if age is not None:
            print(f"Age found: {age}")
        else:
            print("Age not found.")

        city = kwargs.get("city", "Unknown")
        print(f"City: {city}")

    else:
        print("  No keyword arguments provided.")



kwargsAcceptFun(name="Abduqodir", age=20, city="Tashkent", occupation="Student")
print("-" * 1)
kwargsAcceptFun(country="Uzbekistan", favorite_color="Green")
print("-" * 1)
kwargsAcceptFun()
print("-" * 1)
kwargsAcceptFun(fruit="Pomigranade", animal="Dog")
