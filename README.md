Name: Mohammed Bilal M

Intern id: CS25RY20902

Domain name: Codsoft

Stream: Python Programming

Task 3: Custom password generator 

The task is a Custom Password Generator that allows users to generate passwords with different levels of complexity and a specified length. Here's a detailed description of its components and functionality:

1. Imports
random: The random module is imported to generate random selections from predefined character sets to create the password.

2. Character Sets
The code defines four custom character sets that are used to construct the password:

LOWER: A string of lowercase alphabets excluding some commonly ambiguous characters (i, l, o, 1, 0).

UPPER: A string of uppercase alphabets, excluding the same ambiguous characters.

DIGITS: A string of digits excluding 0 and 1 to avoid confusion with letters.

SYMBOLS: A string of special characters (@, #, %, &, *, !, ?), used to increase password complexity.

3. custom_password_generator(length, complexity) Function
This is the main function that generates a custom password based on the desired length and complexity level.

Parameters:

length: Specifies the desired length of the password.

complexity: Specifies the complexity level (1 for basic, 2 for medium, 3 for strong).

Logic:

Based on the complexity level, the function determines which character sets to include in the password. The complexity levels are:

Level 1 (Basic): Includes only lowercase letters and digits.

Level 2 (Medium): Includes lowercase letters, uppercase letters, and digits.

Level 3 (Strong): Includes lowercase letters, uppercase letters, digits, and special symbols.

The function ensures that at least one character from each required character set is included in the password:

For complexity level 1, it adds one lowercase letter and one digit.

For complexity level 2, it adds one uppercase letter as well.

For complexity level 3, it adds one symbol.

The rest of the password is filled randomly from the selected character pool.

The password is shuffled to ensure the structure is not predictable, making it more secure.

Error Handling:

If an invalid complexity level is provided, a ValueError is raised.

4. main() Function
The main function serves as the user interface:

It prompts the user to input the desired password length and complexity level.

Input Validation:

Ensures the password length is at least 4 characters.

Ensures the complexity level is one of the valid options (1, 2, or 3).

If the inputs are valid, the custom_password_generator() function is called to generate the password, and the password is displayed to the user.

Error Handling:

If non-numeric input is provided for either the password length or complexity, an error message is shown.

5. Execution Block
The if __name__ == "__main__": block ensures that the main() function is called when the script is executed directly, but not when it is imported as a module.

Example of Program Flow:
The program prompts the user to enter the desired password length (e.g., 12) and complexity level (e.g., 3 for "Strong").

Based on the input, it generates a password that includes a mix of lowercase letters, uppercase letters, digits, and symbols, ensuring a secure and randomized password.

The generated password is then displayed to the user.

Key Features:
Customizable Complexity: Users can select from three different complexity levels based on their security needs.

Randomization: The password is generated using random selections from predefined character sets and shuffled to avoid patterns.

Error Handling: The program gracefully handles invalid inputs for length and complexity and provides informative error messages.

Conclusion:
This Python code provides a flexible and secure way to generate random passwords with varying levels of complexity, making it useful for creating strong passwords for different applications.

Thanks for the codsoft team for giving this opportunity to be a part of this journey.

Output->

![Project3](https://github.com/user-attachments/assets/735723c6-5514-405a-ac34-db50ec6f0a5b)
