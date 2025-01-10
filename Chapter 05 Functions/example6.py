"""
Example 6: Private Functions
When _private_function() is defined, it is treated like any other
function, but the underscore means it is for internal use.

Part 2:
In Python, a private function is a method within a class that is intended for internal use 
only and is not meant to be accessed directly from outside the class.

Why the Double Underscore Prefix (__)
    The double underscore prefix (__) before the function name is a convention in Python 
    to indicate that the method is private. This convention is called name mangling.

Name Mangling:
    When a method or attribute is prefixed with a double underscore, Python
    automatically modifies its name to a unique internal name.
    This makes it harder (but not impossible) to access the method from outside the class.

Here's how name mangling works:
    - Prefixing: If a method or attribute is defined as __private_method, Python internally
    changes its name to _ClassName__private_method, where ClassName is the name of the class.

    - Accessing from Outside: While you can still technically access the mangled name
    from outside the class, it's generally discouraged and considered a violation of the
    private method's intended purpose.

Key Points:
    - Private methods are not truly inaccessible, but the name mangling convention 
        makes it harder to access them from outside the class.
    - The primary purpose of private methods is to encapsulate the internal workings
        of a class, making the class more robust and maintainable.
    - While you can access private members from outside the class, 
        it's generally considered bad practice and can lead to unexpected behavior 
        if the class's implementation changes.

In Python, the concepts of "private" and "protected" in the context of class members
 (methods and attributes) refer to access control within the class and its subclasses,
  not to company-level copyright.

In summary:
    - Private and protected in Python's class context are about controlling access 
        within the class and its subclasses, not about legal copyright.
    - They are tools for better code organization and maintainability,
        not for preventing external use of the code.
"""

def _private_function():
    print("This is a private function.")
_private_function() # Output: This is a private function.

# Part 2
class MyClass:
    """Example of Object"""
    def __init__(self):
        self.__private_var = 10

    def __private_method(self):
        print("This is a private method")

    def public_method(self):
        self.__private_method()  # Accessing private method within the class

# Creating an object of the class
obj = MyClass()

# Attempting to access private members from outside (will raise an AttributeError)
print(obj.__private_var)  # Raises AttributeError
obj.__private_method()  # Raises AttributeError

# Accessing public method
obj.public_method()  # Output: This is a private method
