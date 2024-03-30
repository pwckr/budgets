# Budgets
Python-project for "Advanced Software Engineering" (WS 23/24) which serves user as budget tracking app. Users can define their monthly budget and save each expense, allowing them to keep track of their finances.

Usable through terminal with `python3 src/main/python/main.py`:
- User is asked for his username (no password requirement implemented)
- program checks if this username is in use, if not a "new account" will be stored as a record in `data_files/users.pkl`. Users are unique and thus stored in a pickled python-set.
- user can set/change his budget which will is stored in `data_files/budgets.pkl`which holds a python-dictionary with usernames as keys and budgets as values.
- user can then add a new expense for which only the price is stored. A timestamp of the current time is automatically created, the datetime and the price is stored in a `data_files/spendings.pkl`, again a dictionary, storing pairs of username - pd.DataFrame pairs.
 
The program is kept minimalistic while its structure is aimed at making further development easy to implement without major rethinking.

## Software Engineering


### 1. Git

See commit history [here](https://github.com/pwckr/budgets/commits/main/).


### 2. UML

Task description:

(At least 3 good different diagrams (PNGs or similiar). "good" means you can pump it up artificially as written in DDD.)


### 3. Domain Driven Design

Event Storming, Domain Chart and a Context Map can be found [here](https://github.com/pwckr/budgets/tree/main/DDD).


### 4. Metrics

Sonarcloud was used to check for multiple metrics which can be found here:

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=pwckr_budgets&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=pwckr_budgets) [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=pwckr_budgets&metric=bugs)](https://sonarcloud.io/summary/new_code?id=pwckr_budgets) [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=pwckr_budgets&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=pwckr_budgets) [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=pwckr_budgets&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=pwckr_budgets) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=pwckr_budgets&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=pwckr_budgets) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=pwckr_budgets&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=pwckr_budgets) [![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=pwckr_budgets&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=pwckr_budgets) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=pwckr_budgets&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=pwckr_budgets) [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=pwckr_budgets&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=pwckr_budgets)


### 5. Clean Code Development

Points addressed:
- Explanatory variable names
- Docstrings
- Parameter- and return-types
- Each unit-test has one assert-statement
- Consistent formatting (PEP8)
- Comments for clarity, not for explanation
- Single Responsibility Principle (each class has one responsibility)

Cheet Sheet can be found [here](https://github.com/pwckr/budgets/blob/main/CleanCodeCheatSheet.md)


### 6. Build

As build tool I chose [pybuilder](https://pybuilder.io). Pybuilder required to reformat the directory layout, additionally the python files `setup.py` and `build.py` were added. Folders `src`, `target` and `docs` were generated. The code lies in `src`.

As further reference, I added a [screenshot](https://github.com/pwckr/budgets/blob/main/BuildScreenShot.png).


Task description:

(Management with any Build System as Ant, Maven, Gradle, etc. (only Travis is perhaps not enough) Do e.g. generate Docs, call tests, etc. (it could be also disconnected from the project just to learn a build tool!) => to be merged with 7!)


### 7. Continious Delivery
I chose to use GitHub Action. I automated testing on every push of which a screenshot is found [here](https://github.com/pwckr/budgets/blob/main/GitHubActionTests.png). The YAML-file with the configuration can be found [here](https://github.com/pwckr/budgets/blob/main/.github/workflows/main-test.yml).


### 8. Unit Tests

Unit tests can be found [here](https://github.com/pwckr/budgets/blob/main/src/unittest/python/usermanagement_tests.py). They are automatically run with the build command of pybuilder. This is ensured by their location in the directory as well as sticking to pybuilder's naming conventions for tests.


### 9. IDE

I use "Visual Studio Code" with which I resort to both, standard and  self-made shortcuts:

- Switch cursor to terminal when the cursor is in a file, switch cursor to the current file when the cursor is in terminal: `cmd + shift + T`. This self made shortcut is super useful continuously executing terminal commands while programming. If I were to only use one short cut it would be this one.
- `shift+alt+left` for selecting the last work, hit `left` again to select the next work to left (and so on...). I find this useful when removing multiple words but not the whole line. `alt + left` for just moving the cursor in front of the previous word in case something was forgotten there. Both also work with `right` of course.
- `cmd + c`, `cmd + v`, `cmd + x` are obvious but still need to be in this list for their vast usefulness.
- `cmd + shift + a` deletes everything to the left of the cursor. Replacing `a` with `d` deletes everything to the right of the cursor (own shortcut).
- `cmd + shift + 7`comments out the current line.


### 10. DSL
A DSL Class can be found [here](https://github.com/pwckr/budgets/blob/main/src/main/python/dsl.py). It can mimic basic functions of the usermanagement class such as:
- create_account
- set_budget
- log_expense
A snippet of this language would be "log expense for Stefan". 


### 11. Functional Programming
For the functional programming part I chose to play with the [Rust language](https://www.rust-lang.org) because of its high performance and increasing demand in the industry. If you have installed rust, you may run the `functional` file in the terminal with `./functional`. The code can be found [here](https://github.com/pwckr/budgets/blob/main/functional.rs)


Task description:

Prove that you have covered all functional aspects in your code as:
- only final data structures
- (mostly) side-effect-free functions
- the use of higher-order functions
- functions as parameters and return values
- use closures / anonymous functions
- You can also do it outside of your project. Even in other languages such as F#, Clojure, Julia, etc. 