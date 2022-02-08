## PYTHON FUNDAMENTALS: TABLE OF CONTENT:

1, 1st Commit: Fundamentals, String, Variables, Functions & Conditional Statement:
a, Interpreter fundaments:
b, String & variables:
c, Functions:
d, Conditional Statements:

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
