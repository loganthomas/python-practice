# Personal Python Docstring notes
> A set of notes I have compiled pertaining to docstring formatting. 
> I find following the concepts laid out in [Google Style Python Docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html) and
[PEP 257](https://www.python.org/dev/peps/pep-0257/) most appealing.  
> I am __not__ claiming to be the author of these ideas, just compiling them for my personal benefit. 

## PEP 257 notes
- For consistency, always use `"""triple double quotes"""` around docstrings.
  - Use `r"""raw triple double quotes"""` if you use any backslashes in your docstrings.

- One-line Docstrings
  - Triple quotes are used even though the string fits on one line.
  - Closing quotes are on the same line as the opening quotes (this looks better for one-liners).
  - There's no blank line either before or after the docstring.
  - The docstring is a phrase ending in a period (as it prescribes the function or method's effect as a command not a description).

- Multi-line Docstrings
  - Consist of a __summary line__, followed by a blank line, followed by a more elaborate description.
    - It is important that the summary line fits on one line and is separate from the rest of the docstring by a blank line.
    - The summary line may be on the same line as the opening quotes or on the next line (I prefer to use the next line).  
  - Insert a blank line after all docstrings (one-line or multi-line) that document a __class__. Generally speaking, the class's methods are separated from each 
  other by a single blank line, and the docstring needs to be offset from the first method by a blank line.
  - The docstring for a __function__ or __method__ should summarize its behavior and document its arguments, return value(s), side effects, exceptions raised, 
  and restrictions on when it can be called (all if applicable). _Optional arguments should be indicated._ It is best to list each argument on a separate line. 
 

## Google Style Python Docstring notes
  
