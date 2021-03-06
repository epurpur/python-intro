# python-intro
uva library workshop on introduction to python

## Who am I?
* Erich Purpur
* Research Librarian for Science & Engineering

* I'm a librarian here at UVA [Research Data Services](https://data.library.virginia.edu/rds-staff/)
    -I'm a liaison to various engineering departments. Basically, if they need stuff from the library
    I try to make it available for them.  I do quite a bit of teaching both in one off workshops like
    this, ongoing series (PhD+), and for-credit courses. I teach courses releated to python programming and
    Geographic Information Systems (GIS) I also sometimes help people with GIS (Geographic Information Systems)
    projects and programming-related questions. And do various side projects as they arise.
    
    * ep9k@virginia.edu 
    * Brown Science & Engineering Library office i046
    
* I like to be interrupted with questions! Please jump right in.

## Welcome to the UVA Library
* [Research Data Services](https://data.library.virginia.edu/)
* [Workshop Series](https://data.library.virginia.edu/training/)

~R workshops
  * Intro to R                                                Tuesday, 1/21  10:00 - 12:00 Brown 133
  * Data Wrangling in R                                       Tuesday, 1/28  10:00 - 12:00 Brown 133
  * Data Visualization in R                                   Tuesday, 2/4   10:00 - 12:00 Brown 133
  
~Python Workshops
  * Intro to Python                                           Tuesday, 1/21  2:00 - 4:00 Brown 133
  * Python and APIs                                           Tuesday, 1/28  2:00 - 4:00 Brown 133
  * Data Visualization with MatPlotLib                        Tuesday, 2/4   2:00 - 4:00 Brown 133
  * Web Scraping in Python                                    Tuesday, 2/11  2:00 - 4:00 Brown 133


We are partnering with Research Computing to offer all workshops in one series this semester!
[Research Computing](https://www.rc.virginia.edu/)
  
* [StatLab](https://data.library.virginia.edu/statlab/)
  
## Getting Python (this will take some time)
* [Windows](https://www.anaconda.com/download/#windows)
* [Mac](https://www.anaconda.com/download/#macos)


## Getting the files we are working with today
* Go here: https://github.com/epurpur/python-intro
* Click "Clone or Download" (green button in upper right corner)
* Click "Download Zip"
* Unzip that directory and move it somewhere that is easy to find (like your Desktop, for example)
  
# Goals for Today
1. Get python running
2. Learn some fundamentals
3. Learn how to help yourself (Most Important!)

## Outline
1. Strings
2. Print Statement
3. Numbers (Int and Float)
4. Errors
5. Functions (Built-ins and custom)
6. Lists, Loops, Booleans, Indexing
7. Dictionaries
8. Import
9. Conditional Statements
10. Mutable vs. Immutable data types


### What is Python?
From www.python.org:
"Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance." 

Python is a general purpose programming language used for a huge variety of purposes. It's user community is growing rapidly!
(https://stackoverflow.blog/2017/09/06/incredible-growth-python/)


# Difference between R and Python?  (Simplified)
* They are both open source programming languages
* Python is general purpose while R is focused on statistics and data analysis
* You can also do stats with Python. Many packages available
    * NumPy
    * SciPy
    * Pandas


## A brief history
* Designed by [Guido van Rossum](https://www.google.com/search?q=google+image+search+guido+van+rossum&safe=off&rlz=1C5CHFA_enUS690US690&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjE_eGK6KHdAhXrRd8KHUzBDHsQ_AUICigB&biw=1440&bih=697)
* version 1.0 1994
* version 2.0 2000
* version 3.0 2008 (not widely adopted until a few years ago)
* [logo](https://www.google.com/search?q=python+logo&safe=off&rlz=1C5CHFA_enUS690US690&source=lnms&tbm=isch&sa=X&ved=0ahUKEwi9xN-J8aHdAhVBMt8KHT-WDEEQ_AUICigB&biw=1440&bih=697)
* [anaconda logo](https://www.google.com/search?q=anaconda+logo&safe=off&rlz=1C5CHFA_enUS690US690&source=lnms&tbm=isch&sa=X&ved=0ahUKEwin88Gf8aHdAhUhiOAKHeGLBHYQ_AUICigB&biw=1440&bih=697)


# Let's Get to It (hopefully everyone is done installing)
* open spyder [it looks like this](spyder.png)
* We are using Anaconda/Spyder today as it seems to be widely used throughout UVA. Adapted for data scientists
* Spyder is a Programming IDE (Integrated Development Environment)
  * text editor
  * variable explorer
  * console
  * control icons
  
  
## Strings
* A string is a 'string' of characters
  * 'apple'  # letters
  * 'blue42' # letters and numbers
  * 'i am the very model of a modern major general' # spaces are fine
  * '7 hills' # it can even start with a number
  
## Comments
We also introduce comments here, the computer will ignore everything after the '#' symbol. There are other forms but we'll see them later on.

## Variables
You can "save" things as variables. For those curious as to what's going on under the hood...in python a variable is actually just a pointer to the location in memory where the object lives.
* a = 'apple'
  * a is the variable
  * = is the assignment operator
  * 'apple' (a string) is the object assigned to a
  
* *Important Note*: the assignment operator is not like an equals sign
  * a=5
  * a=7
    * totally works, a was just reassigned to point to 7
    
## Error Messages
* Tell you when (and hopefully where) your code breaks.
* Some are more readable and helpful than others
* Read them from the bottom up
    
## Functions
* print(a) # this function will show us what a points to
* we know that print is a function because there is no space between print and the "("
* format of a function: name(arguments)
* we say we "call" a function
* *this is super important* in python the way to spot a function is no space before a "(" and a letter or number
  * [python built-in functions](https://docs.python.org/3/library/functions.html)
  * print(...)
  * type(...)
  * pow(...)
  * in an equation you may see 5*(2+3), you won't seet 5(2+3) (try it and see what happens)
  
## Indexing
* for objects with an order you can access individual elements
* [indexing](indexing.png)
* you can also pull out slices
  * syntax [X:Y]
    * starting at X
    * upto but not including Y

## Lists
* represented like functions but with [...]
* there is an order to the items
* the items can be of any type

## Dictionary
* represented like lits but with {...}
* there is no order to items
* items contain two pieces: a key and a value represented key:value and the key must be a string

## loops - used when you want to repeat code
* for loop
  * for X in Y: << code >>
    * X is a new variable created on the spot
    * Y is some preexisting iterable
    * << code >> is a block of code you want to repeat
    * eg: for x in range(10): print(x)

* while loop
  * while Z: << code >>
    * Z is a boolean
    * << code >> is a block of code you want to repeat
    * eg: while i<10: print i; i+=1

## if statements
* example
  * if X: << code A >>
  * else: << code B >>
    * X is a boolean
    * << code A >> is some code
    * << code B >> is some code, could be the same
    


# Import
* *This is the most important topic*
* The import command let's you bring in code from another file and use it
* one example: random number generation
  * import random
    * random.randint(0,10)
* Sometimes packages needed to be installed (3rd party packages)
    *pip - (https://pip.pypa.io/en/stable/installing/)
    *conda - (https://conda.io/docs/)


#Mutablility
* Some data types can be changed, others can't
* Many reasons for this, a big one is performance
    * Mutable data types (such as lists) are costly to CPU processingn power
    * Immutable data types (like arrays) take less memory and processing power


# Scripting vs Programming
It's a matter of modularity. Programs are designed to be modular and work with other programs. Scripts are designed to be 
single use.


# How to Help Yourself and Learn More

# Learning Resources
* Pick up a book, there are many available through the UVA library website 
        * Learn Python the Hard Way (Available for free through UVA libraries)
        * [Link here](https://search.lib.virginia.edu/catalog/u7434195)
        
* CS 1110/1111 @ UVA
        * All resources available online for free!
        * https://cs1110.cs.virginia.edu/
        
* Phd+ Course Materials
        * All resources available online for free!
        * https://workshops.rc.virginia.edu/lesson/python_shortcourse/python_introduction

* Other resources available at UVA
        * Research Data Services - StatLab Fellows
        * https://data.library.virginia.edu/statlab/
        * statlab@virginia.edu
        * Research Computing - Provides high performance computing expertise
            * https://www.rc.virginia.edu/

# Self Help via the Internet
  * Google 
        * Ex: "How to make dictionary python"
        * Ex: "python decorators"
        
  * Stack Overflow (https://stackoverflow.com/)
        * A question/answer site for programming questions (actually, not just programming any more)
        * Not only python
        * DO NOT just ask questions, do your research first!
            * Odds are very high someone has already asked your question, especially as a novice
     
  * Youtube
        - Corey Schafer (https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g)
            - If you have a question about a python programming concept, Corey Schafer has covered it
     
  * Practice Python (http://www.practicepython.org/)
        * Coding challenges for programmers of all levels
        
  * Python Tutor (http://pythontutor.com/)
        * Visualize what your code is doing step-by-step
        * Has limitations once you start importing libraries
        
  * TalkPython Training (https://training.talkpython.fm/)
        * Not free
        * Really awesome courses that help you get "real world" project experience
  
  






