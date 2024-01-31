# Python - Test-driven development

In this project, I started practicing test-driven development using `docstring`and `unittest` in Python.

* [tests](./tests): Folder of test files. Includes both Holberton-provided ones as well as the following eight independently-developed:
  * [0-add_integer.txt](./tests/0-add_integer.txt)
  * [2-matrix_divided.txt](./tests/2-matrix_divided.txt)
  * [3-say_my_name.txt](./tests/3-say_my_name.txt)
  * [4-print_square.txt](./tests/4-print_square.txt)
  * [5-text_indentation.txt](./tests/text_indentation.txt)
  * [6-max_integer_test.py](./tests/6-max_integer_test.py)
  * [100-matrix_mul.txt](./tests/100-matrix_mul.txt)
  * [101-lazy_matrix_mul.txt](./tests/101-lazy_matrix_mul.txt)
* [doctests](./doctests): Folder of `.py` files with `doctest` in them. Includes the following eight:
  * [0-add_integer.py](./doctests/0-add_integer.py)
  * [2-matrix_divided.py](./doctests/2-matrix_divided.py)
  * [3-say_my_name.py](./doctests/3-say_my_name.py)
  * [4-print_square.py](./doctests/4-print_square.py)
  * [5-text_indentation.py](./doctests/5-text_indentation.py)
  * [6-max_integer.py](./doctests/6-max_integer.py)
  * [100-matrix_mul.py](./doctests/100-matrix_mul.py)
  * [101-lazy_matrix_mul.py](./doctests/101-lazy_matrix_mul.py)
  * [102-matrix_divided.py](./doctests/102-matrix_divided.py)
* [README.md](./README.md): This file.



Resources

Read or watch:

    doctest — Test interactive Python examples (until “26.2.3.7. Warnings” included)
    doctest – Testing through documentation
    Unit Tests in Python
    Unittest module
    Interactive and Non-interactive tests

Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
General

    Why Python programming is awesome
    What’s an interactive test
    Why tests are important
    How to write Docstrings to create tests
    How to write documentation for each module and function
    What are the basic option flags to create tests
    How to find edge cases
    How to write a test case for a function that takes a list of strings

Requirements
Python Scripts

    Allowed editors: vi, vim, emacs
    All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
    All your files should end with a new line
    The first line of all your files should be exactly #!/usr/bin/python3
    A README.md file, at the root of the folder of the project, is mandatory
    Your code should use the pycodestyle (version 2.8.*)
    All your files must be executable
    The length of your files will be tested using wc

Python Test Cases

    Allowed editors: vi, vim, emacs
    All your files should end with a new line
    All your test files should be inside a folder tests
    All your test files should be text files (extension: .txt)
    All your tests should be executed by using this command: python3 -m doctest ./tests/*
    All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
    All your functions should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)')
    A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
    We strongly encourage you to work together on test cases, so that you don’t miss any edge case – The Checker is checking for tests!
