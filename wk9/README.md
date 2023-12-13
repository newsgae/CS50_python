    # Arithmetic Game

    ## Video Demo:  https://youtu.be/oSPps_VYfN8

    ## Developer
       Xuan Li from Cincinati, Ohio, USA

    ## Description:
    This simple arithmetic game challenges players to solve a series of randomly generated math questions within a specified time frame. The game provides an opportunity to test and improve your mental math skills in addition, subtraction, and multiplication. Negative number arithmetic is avoided to simplify the game for lower school students.

    ## How to Play

    1. Run the code using a Python interpreter.
    2. Enter your name when prompted.
    3. Press Enter to start the Math Challenge.
    4. Answer the displayed arithmetic questions as quickly as possible.
    5. If the answer is incorrect, you will be asked to resolve until your answer is correct.
    6 The game consists of 10 questions, and your accuracy and completion time will be displayed at the end.

    ## Features

    * Random Questions: The game generates random arithmetic questions involving addition, subtraction, and multiplication. There is no negative number calculation for lower school students.
    * Timer: The game tracks the time taken to complete the challenge.
    * Accuracy Calculation: Your accuracy is calculated based on the number of correct answers.

    ## Code Structure

    main(): The main function that orchestrates the game, collects player input, and displays results.
    get_question(): Generates random arithmetic questions and ensures no negative number arithmetic.
    get_answer(): Calculates the correct answer for a given arithmetic expression.
    get_accuracy(): Calculates the player's accuracy based on the number of correct answers.

    ## Dependencies

    - Python 3.x
    - Required Modules:
        - `random`: Used for generating random numbers and selecting operators.
        - `time`: Used for measuring the time taken to complete the challenge.

    ## Improvements
    There are a few possible improvements, such as
    1. Expand to fraction and decimal calculations
    2. Create a login system to record players' historical data to show progress
    3. Implement different difficulty levels (easy, medium, hard) with varying ranges for operands.
    4. Introduce more complex operators like division or exponentiation for advanced players.
    5. Allow users to select specific operators they want to include in the game (e.g., addition only, multiplication only).
    6. Allow users to select specific ranges they want to include in the game (e.g., min and max operands).
    7. Consider using a graphical interface (GUI) for a more engaging and user-friendly experience.

    ## Reference
    https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
    
MIT License
Copyright (c) [2023] [X.Li]

