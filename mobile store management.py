class MobileStore:
    def __init__(self):
        self.mobiles = {
            1: "Samsung Galaxy",
            2: "Apple",
            3: "Vivo",
            4: "Oppo",
            5: "Xiaomi",
            6: "One Plus",
            7: "iQOO",
            8: "Realme",
            9: "Google Pixel",
            10: "Samsung Galaxy Flip"
        }
        self.models = {
            "Samsung Galaxy": {"Galaxy S23": 79999, "Galaxy A54": 34999},
            "Apple": {"iPhone 14": 79999, "iPhone SE": 49999},
            "Vivo": {"Vivo X90": 59999, "Vivo Y100": 24999},
            "Oppo": {"Oppo Reno10": 45999, "Oppo A78": 17999},
            "Xiaomi": {"Xiaomi 13 Pro": 69999, "Redmi Note 12": 21999},
            "One Plus": {"One Plus 11": 56999, "One Plus Nord 3": 33999},
            "iQOO": {"iQOO Neo 7": 31999, "iQOO Z7": 21999},
            "Realme": {"Realme GT 3": 42999, "Realme Narzo 60": 17999},
            "Google Pixel": {"Pixel 8": 85999, "Pixel 7a": 43999},
            "Samsung Galaxy Flip": {"Galaxy Flip 5": 99999, "Galaxy Flip 4": 84999}
        }

    def view_mobiles(self):
        """View all available mobile brands."""
        if not self.mobiles:
            print("No mobile brands available.")
        else:
            print("Available Mobile Brands:")
            for brand_id, brand_name in self.mobiles.items():
                print(f"{brand_id}. {brand_name}")

    def view_models(self):
        """View models and prices of a specific brand."""
        self.view_mobiles()
        try:
            brand_id = int(input("Enter the brand number to view models: "))
            brand_name = self.mobiles.get(brand_id)
            if brand_name and brand_name in self.models:
                print(f"Models for {brand_name}:")
                for model, price in self.models[brand_name].items():
                    print(f"{model}: Rs. {price}")
            else:
                print("Invalid brand number or no models available.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def purchase_mobile(self):
        """Purchase a mobile by selecting a brand and model."""
        self.view_models()
        try:
            brand_id = int(input("Enter the brand number: "))
            brand_name = self.mobiles.get(brand_id)
            if brand_name and brand_name in self.models:
                model_name = input("Enter the model name to purchase: ")
                if model_name in self.models[brand_name]:
                    price = self.models[brand_name][model_name]
                    print(f"Congratulations! You have purchased {model_name} for Rs. {price}.")
                else:
                    print("Invalid model name. Please try again.")
            else:
                print("Invalid brand number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def add_mobile(self):
        """Add a new mobile brand to the list."""
        new_brand = input("Enter the name of the new brand to add: ").strip()
        if new_brand:
            new_id = max(self.mobiles.keys()) + 1 if self.mobiles else 1
            self.mobiles[new_id] = new_brand
            self.models[new_brand] = {}
            print(f"{new_brand} has been added successfully.")
        else:
            print("Brand name cannot be empty.")

    def delete_mobile(self):
        """Delete an existing mobile brand."""
        self.view_mobiles()
        try:
            brand_id = int(input("Enter the brand number to delete: "))
            if brand_id in self.mobiles:
                brand_name = self.mobiles.pop(brand_id)
                self.models.pop(brand_name, None)
                print(f"{brand_name} has been deleted successfully.")
            else:
                print("Invalid brand number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    store = MobileStore()
    while True:
        print("\n--- Mobile Store Management System ---")
        print("1. View All Mobiles")
        print("2. View Models of a Brand")
        print("3. Purchase a Mobile")
        print("4. Add a New Mobile Brand")
        print("5. Delete a Mobile Brand")
        print("6. Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                store.view_mobiles()
            elif choice == 2:
                store.view_models()
            elif choice == 3:
                store.purchase_mobile()
            elif choice == 4:
                store.add_mobile()
            elif choice == 5:
                store.delete_mobile()
            elif choice == 6:
                print("Thank you for using the Mobile Store Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please choose a valid option.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
