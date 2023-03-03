# Click Assignment
 
This assignment is to use python's click module for training purpose.

## SETUP

 1. Create a virtual environment at the root of project and activate it using command:
    ```
    virtualenv venv

    . venv/bin/activate
    ```

 2. Run the command:

    ```
    pip install --editable .
    ```

3. Now you are able to use the cli commands

4. Run any command with *--help* argument to get the details about it.

    e.g;
    ```
     mycommand --help
    ```

## Commands

1. *main* : Usage: main [OPTIONS] NAME

    Print Hello from {name} upto {number} times

    Options:
    --number TEXT  number of greetings
    --help         Show this message and exit.

    e.g; 
    ```
    main myname
    ```
    
    Output:
    ```
    Number of count please: 2
    Hello from myname
    Hello from myname
    ```

2. *clearsc*: Usage: clearsc [OPTIONS]

    Clears the screen

    e.g;
    ```
    clearsc
    ```

3. *weather*: Usage: weather [OPTIONS]

    Print Weather

    Options:
    --weather [sunny|rainy|winter]

    e.g;
    ```
    weather --weather=sunny
    ```

    Output:
    ```
    Weather is sunny
    ```

4. *utilalias*: Example to demonstrate alias name also work like pul for pull command etc
    The idea is, if someone provide some misspelled commands, that should match with most nearest correct command automatically and execute

    Commands:
        pull
        push

    e.g;
    ```
    utilalias pus
    ```

    Output:

    ```
    Pushing to the repo
    ```

5. *switch*: Options:
    --switch / --no-switch  Using as a toggle if switch is on/off

    Commands:
    sync

    e.g;
    ```
    switch --switch sync
    ```

    Output:
    
    ```
    Switch is on
    Syncing
    ```

6. *restaurant*: This command used for pick lunch/dinner from restaurant
    Commands:
        dinner
        lunch

    e.g;

    ```
    restaurant dinner pizza

    restaurant lunch burger 
    ```

    Output:

    ```
    Enjoy your pizza
    Enjoy your burger
    ```

7. *convert*: This command used for converting the case of any text like lower case or upper case.
    
    Commands:
        lower  Convert to lower case
        upper  Convert to upper case

    e.g;

    ```
    convert upper 'my name is Faizan'

    convert lower 'MY Name is Faizan'
    ```

    Output:

    ```
    MY NAME IS FAIZAN

    my name is faizan
    ```

8. *calculator*: This command is used for calculating the result of two numbers like as calculator.

    Commands:
        difference  Return difference of two nos
        divide      Return division of two nos
        product     Return multiplication of two nos
        sum         Return sum of two nos

    e.g;

    ```
    calculator difference 7 8

    calculator sum 7 8

    calculator product 7 8

    calculator divide 7 8
    ```

    Output:

    ```
    -1

    15

    56

    0.875
    ```
    