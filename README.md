# Puninator
*"A pun a day keeps the depression troll away."*

## Contents

- [Description](#description)
- [Dependencies](#dependencies)
- [How it works](#how-it-works)
- [Submitting more puns](#submitting-more-puns)
- [TODO](#todo)

## Description

**Puninator** is a Python-based pun generator. 'Nuff said.

## Dependencies

Puninator requires Python 2.x to run. The program was tested in Python 2.7.16 during development, but it may be compatible with older versions.

## How it works

Puninator consists of two distinct modules: **main.py** and **punlist.py**. The former contains the main code that Puninator runs on, while the latter is merely a list of the puns that the program can generate.

In order to generate a pun, you'll want to run main.py in a command line or similar environment. Upon running the module, it will display a random pun picked from punlist.py.

You only need to worry about punlist.py if you want to extend it with more puns. To add a pun to the list, open punlist.py in your code editor of choice and write it into the puns[] list between quotation marks (""). Don't forget to add commas (outside the quotation marks) at the end of each new line!

## Submitting more puns

Additional puns may be submitted by opening an issue with the "pun-suggestions" tag. List each pun on a separate line. Puns deemed worthy of being in the list will be added to punlist.py in a future commit.

## TODO

* Port from Python 2 to Python 3 (once I actually learn Python 3).
* Implement additional commands, e.g. to copy a pun to the clipboard.
* Implement pun categories.