users_list = []

# Use a loop to allow input for multiple users
while True:
    # Create an empty dictionary for each user
    user_data = {}

    # Take input for first name
    first_name = input("Please enter the first name: ")

    # Take input for age and convert to an integer
    age = int(input("Please enter the age: "))

    # Store the data in the user dictionary
    user_data['first_name'] = first_name
    user_data['age'] = age

    # Add the user data to the list of users
    users_list.append(user_data)

    # Ask if the user wants to continue entering data
    continue_input = input("Do you want to add another user? (yes/no): ").lower()

    # Break the loop if the user does not want to continue
    if continue_input != 'yes':
        break

# Print the list of users
print("User data saved for multiple users:")
for user in users_list:
    print(user)

