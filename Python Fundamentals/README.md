## PYTHON FUNDAMENTALS: TABLE OF CONTENT:

1, 1st Commit: Fundamentals, String, Variables, Functions & Conditional Statement:
a, Interpreter fundaments:
b, String & variables:
c, Functions:
d, Conditional Statements:

2, 2nd Commit: Loops (while and for), Data Structures (Lists, Sets and Dictionaries)
a, Loops:
b, Lists: like array in JavaScript
c, Sets: like array but it's sorted and use different syntax
d, Dictionaries: like Object in Javascript

---

## PYTHON FUNDAMENTALS: COMMIT HISTORY:

1, 1st Commit: Fundamentals, String, Variables, Functions & Conditional Statement:

    a. Interpreter fundaments:
        - type in command line: $ python3 > can do some calculation
            (See in video 5)

    b, String & variables: much like Javascript

        - Assign && Declare
        greeting = "Hello"

        - Access:
        greeting[1] => will get 'e'

        - Concatenation:
        greeting + " Trung" => will get "Hello Trung"

        - Getting a substring:
        greeting[0:2] => getting the string index from 1 to 2 > will get 'hel'
        greeting[0:] => getting the whole string
        greeting[-1] => getting the last character of the string > will get 'o'
        greeting[:3] => getting 'hel'

    c, Functions: Much like Javascript. Examplary syntaxes:

        - Function Declaration:
            +, remember to go to a new line and put a tab after: def functionName(param1, param2):

        def multiplySomething(a, b):
            result = a * b
            print("The result is: ", result)
            return result

        - Calling a function:
            +, notes that function is also and object in python

        multiply =  multiplySomething

        multiply(3, 6)

        => should the the print and the output of 18

        mutiply2 = multiplySomething(3, 5)
        multiply2

        => should has the value of 15

    d, Conditional Statements:

        - Booleans in Python:
            +, True
            +, False

        - Comparision syntax:
            +, 1 <= 2
                => True
            +, 'Hello' == 'hello'
                => False
            +, 'a' < 'z'
                => True

        - Conditional Statement example:
            +, mind the tabs

            def describeWeather(temp):
                if temp > 80:
                    print("It's hot")
                else:
                    print("It's cool")

                return "returnning this regardless"

            +, Invoke the function:
            describeWeather(90)

2, 2nd Commit: Loops (while and for), Data Structures (Lists, Sets and Dictionaries)

    a, Loops:
        - While Loops Syntax:
            i = 0
            while i < 10:
                print(i)
                i = i + 1

        - For Loops Syntax:

            for z in range(10):
                print(z)

    b, Lists: like array in JavaScript

        colors = ['yellow', 'blue', 'red']
        colors
            => this will display the array
            should get: ['yellow', 'blue', 'red']

        colors.append('green')
        colors
            => this will show the array: ['yellow', 'blue', 'red', 'green']

        More List methods in this link:
            https://www.w3schools.com/python/python_ref_list.asp

    c, Sets: like array but it's sorted and use different syntax

        days = {"Monday", "Tuesday", "Wednesday", "Monday", "Tuesday"}
        days
            => this will show: {"Wednesday", "Monday", "Tuesday"}
                this is because the sets won't repeat an existing value
                and the values are sorted

        days.add("Thursday")
        days
            => this will show: {"Wednesday", "Monday", "Thursday", "Tuesday"}

        More Set methods in this link:
            https://www.w3schools.com/python/python_ref_set.asp

    d, Dictionaries: like Object in Javascript

        grades = {'Sam': 85, 'Beth': 92}
        grades['Fred'] = 88
        grades
            => will show {'Sam': 85, 'Beth': 92, 'Fred': 88}

        del grades['Fred']
        grades
            => will show {'Sam': 85, 'Beth': 92}

        list(grades.keys())
            => will show ['Sam', 'Beth']
            Basically all the keys in your dictionary

        - grades.keys() will return dict_keys(['Sam', 'Beth'])
            => See video 10 from minutes 7 to understand more about this
            grades.value() will return a list of values for this dictionary:
                dict_values([85, 92])
