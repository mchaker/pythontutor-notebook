# credit: abbourne1486 on discord
# Sample Docstring for functions - using a version of Google docstring guidelines
# Note that Python's help function will use this docstring as the function's help text.
# (i.e. `help(add)` will print the docstring as help)
# Example of how to write and run Doctests for easy testing
# https://docs.python.org/3/library/doctest.html - doctest documentation

def add(num1: int, num2: int) -> int:
    """
    Add up two integer numbers.

    This function simply wraps the ``+`` operator, and does not
    do anything interesting, except for illustrating what
    the docstring of a very simple function looks like, and how to write
    doctests for a function

    Parameters:
    num1 : int
        First number to add.
    num2 : int
        Second number to add.

    Returns:
    int
        The sum of ``num1`` and ``num2``.

    Examples:
    >>> add(2, 2)
    4
    >>> add(25, 0)
    25
    >>> add(10, -10)
    0
    
    (Note that this last testcase will fail)
    >>> add(10, -10)
    10
    """
    return num1 + num2

# Run the doctests in this file when executed as a script
# doctest will look everywhere in the module (i.e. file) for text that looks like
# interactive Python sessions, and will run them as tests to see if the actual
# output matches the expected output. 
# See https://docs.python.org/3/library/doctest.html
# Note that the verbose=True argument makes doctest print out more information
# about what it is doing. Without it, you will only see output if a test fails.
if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
    
"""
Running this module, by entering "python -m doctest_example.py" 
on the command line produces:

Trying:
    add(2, 2)
Expecting:
    4
ok
Trying:
    add(25, 0)
Expecting:
    25
ok
Trying:
    add(10, -10)
Expecting:
    0
ok
Trying:
    add(10, -10)
Expecting:
    10
**********************************************************************
File "__main__", line 36, in __main__.add
Failed example:
    add(10, -10)
Expected:
    10
...
   1 of   4 in __main__.add
4 tests in 2 items.
3 passed and 1 failed.
***Test Failed*** 1 failure.
"""
