# ---------------------------------------------------------------------------
#  class_header_comment_sample.py
#
#  Description : Demonstrates a clean Python file header with a single class
#                and one function, including docstrings for both.
#
#  Author      : Sen SD (sen@example.com)
#  Created     : 2025-09-18
#  Version     : 1.0.0
#  License     : MIT
#
#  Usage       : python class_header_comment_sample.py
# ---------------------------------------------------------------------------


class Greeter:
    """
    A simple class to generate greeting messages.

    Attributes
    ----------
    name : str
        The name of the person to greet.

    Methods
    -------
    say_hello() -> str
        Return a greeting message for the person.
    """

    def __init__(self, name: str):
        """
        Initialize the Greeter with a name.

        Parameters
        ----------
        name : str
            Person's name to include in the greeting.
        """
        self.name = name

    def say_hello(self) -> str:
        """
        Construct and return a friendly greeting.

        Returns
        -------
        str
            A greeting message such as "Hello, Alice!".
        """
        return f"Hello, {self.name}!"


# Example usage when run as a script
if __name__ == "__main__":
    greeter = Greeter("World")
    print(greeter.say_hello())
