"""
List:
    A list is an ordered collection of elements that can be of different data types.
    Elements in a list are indexed and accessible via integer indices, starting from 0.
    Lists are mutable, meaning you can modify, add, or remove elements after creation.
    Lists are created using square brackets [].

    Example: my_list = [1, 2, 'hello', 3.14]
Dictionary:
    A dictionary is an unordered collection of key-value pairs, where each key maps to a corresponding value.
    Keys in a dictionary must be unique and immutable (e.g., strings, numbers, tuples).
    Dictionary values can be of any data type and can be repeated.
    Dictionaries are mutable, allowing for modifications to the key-value mappings.
    Dictionaries are created using curly braces {} or with the dict() constructor.

    Example: my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

"""

def main():
    # Create a list of numbers
    numbers = [1, 2, 3, 4, 5]

    # Create a dictionary of student information
    student = {
        'name': 'Alice',
        'age': 20,
        'major': 'Computer Science',
        'courses': ['Programming', 'Data Structures', 'Algorithms']
    }

    # Access and print elements from the list
    print("Numbers List:")
    for num in numbers:
        print(num)

    # Access and print elements from the dictionary
    print("\nStudent Information:")
    print("Name:", student['name'])
    print("Age:", student['age'])
    print("Major:", student['major'])
    print("Courses:")
    for course in student['courses']:
        print("-", course)

    # Modify list and dictionary
    numbers.append(6)
    student['age'] = 21

    # Print modified list and dictionary
    print("\nModified Numbers List:", numbers)
    print("Modified Student Information:")
    print("Name:", student['name'])
    print("Age:", student['age'])
    print("Major:", student['major'])
    print("Courses:")
    for course in student['courses']:
        print("-", course)


if __name__ == "__main__":
    main()
