# Problem #1: List Practice
# Now practice writing code with lists! Implement the functionality described in the comments below.

# def main(): # Create a list called fruit_list that contains the following fruits: # 'apple', 'banana', 'orange', 'grape', 'pineapple'.

# # Print the length of the list.


# # Add 'mango' at the end of the list. 


# # Print the updated list.
# Problem #2: Index Game
# As a warmup, read this code and play the game a few times. Use this mental model of the list:

# Objective:
# Create a Python program that helps you practice accessing and manipulating elements in a list. This exercise will help you get comfortable with indexing, slicing, and modifying list elements.

# Instructions:
# Initialize a List:
# Create a list with at least 5 different elements. They can be numbers, strings, or a mix of both.

# Accessing Elements:
# Write a function that:

# Accepts a list and an index as inputs.
# Returns the element at the specified index.
# If the index is out of range, return an appropriate message.
# Modifying Elements:
# Write a function that:

# Accepts a list, an index, and a new value as inputs.
# Replaces the element at the specified index with the new value.
# If the index is out of range, return an appropriate message.
# Slicing the List:
# Write a function that:

# Accepts a list, a start index, and an end index as inputs.
# Returns a new list containing the elements from the start index up to (but not including) the end index.
# Handles cases where the indices are out of range.
# Game Interaction:
# Create a simple text-based game that:

# Prompts the user to select an operation (access, modify, slice).
# Asks for the necessary inputs (index, new value, etc.).
# Displays the result and the updated list.




# Problem #1: List Practice
def main():
    # Create a list with the given fruits
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']

    # Print the length of the list
    print("Length of the list:", len(fruit_list))

    # Add 'mango' at the end of the list
    fruit_list.append('mango')

    # Print the updated list
    print("Updated list:", fruit_list)


# Problem #2: Index Game

def access_element(lst, index):
    if 0 <= index < len(lst):
        return lst[index]
    else:
        return "Index out of range."


def modify_element(lst, index, new_value):
    if 0 <= index < len(lst):
        lst[index] = new_value
        return lst
    else:
        return "Index out of range."


def slice_list(lst, start, end):
    if 0 <= start < len(lst) and 0 <= end <= len(lst):
        return lst[start:end]
    else:
        return "Start or end index out of range."


def index_game():
    sample_list = ['red', 'blue', 'green', 'yellow', 'purple']

    while True:
        print("\nChoose an operation: access / modify / slice / exit")
        choice = input("Enter your choice: ").lower()

        if choice == 'access':
            index = int(input("Enter index to access: "))
            print("Result:", access_element(sample_list, index))

        elif choice == 'modify':
            index = int(input("Enter index to modify: "))
            new_value = input("Enter new value: ")
            result = modify_element(sample_list, index, new_value)
            print("Updated List:" if isinstance(result, list) else "Error:", result)

        elif choice == 'slice':
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print("Sliced List:", slice_list(sample_list, start, end))

        elif choice == 'exit':
            print("Exiting the game. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


# Running both main and game
main()
index_game()
