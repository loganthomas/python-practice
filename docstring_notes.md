# Personal Python Docstring notes
> A set of notes I have compiled pertaining to docstring formatting.   
> I find following the concepts laid out in [Google Style Python Docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html) and
[PEP 257](https://www.python.org/dev/peps/pep-0257/) most appealing.  
> I am __not__ claiming to be the author of these ideas, just compiling them for my personal benefit. 


## PEP 257 notes
- For flowing long blocks of text with fewer structural restrictions (docstrings or comments), the line length should be limited to __72 characters__ (PEP 8).
- For consistency, always use `"""triple double quotes"""` around docstrings.
- Use `r"""raw triple double quotes"""` if you use any backslashes in your docstrings.

- One-line Docstrings
  - Triple quotes are used even though the string fits on one line.
  - Closing quotes are on the same line as the opening quotes (this looks better for one-liners).
  - There's no blank line either before or after the docstring.
  - The docstring is a phrase ending in a period (as it prescribes the function or method's effect as a command not a description).

- Multi-line Docstrings
  - Consist of a __summary line__, followed by a blank line, followed by a more elaborate description.
    - Summary line should fit on one line and be separated from the rest of the docstring by a blank line.
    - Summary line can be on the same line as the opening quotes or on the next line (I prefer to use the next line).  
  - Insert a blank line after all docstrings (one-line or multi-line) that document a __class__. Generally speaking, the class's methods are separated from each 
  other by a single blank line, and the docstring needs to be offset from the first method by a blank line.
  - The docstring for a __function__ or __method__ should summarize its behavior and document its arguments, return value(s), side effects, exceptions raised, 
  and restrictions on when it can be called (all if applicable).
    - Optional arguments should be indicated.
    - It is best to list each argument on a separate line. 
 

## Google Style Python Docstring notes

```python
def module_level_function(param1, param2, param3, param4=None, *args, **kwargs):
    """
    Example of a module level function.

    Function parameters should be documented in the Args section. The name
    of each parameter is required. The type and description of each paramter
    is optional, but should be included if not obvious.

    If *args or **kwargs are accepted, they should be listed as such.

    The format for a parameter is:
    	name (type): description
	    The description may span multiple lines. Following
	    lines should be indented. The "(type)" is optional.

	    Multiple paragraphs are supported in parameter
	    descriptions.

    Args:
	param1 (int): The first parameter.
        param2 (:obj:`list` of :obj:`str`): The second parameter.
        param3 (:obj:`ndarray` of :obj:`float`): 2D array containing data with `float` type.
	param4 (:obj:`str`, optional): The third parameter. Defaultes to None.
	    Second line of description should be indented.
	*args: Variable length argument list.
	**kwargs: Arbitrary keyword arguments.

    Returns:
    	bool: The return value. True for success, False otherwise.

    Raises:
        AttributeError: The Raises section is a list of all exceptions
	    that are relevant to the interface.
	ValueError: If `param2` is equal to `param1`.
    """
    if param1 == param2:
        raise ValueError('param1 may not be eqaul to param2')
    return True
``` 


```python
def example_generator(n):
    """
    Generators have a ``Yields`` section instead of a ``Returns`` section.

    Args:
        n (int): The upper limit of the range to generate, from 0 to `n` - 1.

    Yields:
        int: The next number in the range of 0 to `n` - 1.

    Examples:
        Examples should be written in doctest format, and should illustrate how
        to use the function.

        >>> print([i for i in example_generator(4)])
        [0, 1, 2, 3]

    """
    for i in range(n):
        yield i
```
 
