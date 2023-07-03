from functionality.interactions.registration import Registration
from functionality.interactions.regi import Registration

# import other object files as needed

def main():
    print("Choose an option:")
    print("1. Feeding | 2. Serving | 3. Refilling | 4. Registration")
    
    while True:
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            pass
            
        elif choice == "2":
            pass
            
        elif choice == "3":
            pass
            
        elif choice == "4":
            # Create an instance of the Registration class
            registration = Registration()
            # Call the check_token method to start the registration process
            registration.check_token()
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
