# 30 Rovers to Mars

Solution to Mars Rovers problem from https://github.com/GetAmbush/code-challenge/blob/master/challenge2.md

---

Files structure:
- src
  - marsrovers (the package)
    - parser
    - plateau
    - position
    - rover
  - tests (unit tests)
    - mocks
      - input (we mock user input using text files)
      - output (the solutions to such input files)
    - test_parser
    - test_plateau
    - test_position
    - test_rover
  - mars.py (a script that can be called by command line to solve the problem)

---
### Execution

The solution can be called via command line using: `python mars.py`

Or you can pass a text file using: `python mars.py < yourInputFileHere.txt`

---
### Unit Tests

Unit tests were implemented using the **unittest** framework

To run the unit tests:
  1. Go to the source folder (Python cannot handle well relative imports): `cd src/`
  2. Call the discoverer from the unittest framework (it will handle things properly from here): `python -m unittest discover`

---

Things are pretty straightforward and (I believe) well documented.

*Still, in case of any questions regarding the code and how to execute it, just send me a message.*
