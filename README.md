# python-intro
uva library workshop on introduction to python

## Who am I?
* Erich Purpur

* I'm a librarian here at UVA [Research Data Services](https://data.library.virginia.edu/rds-staff/)
    -I'm a liaison to various engineering departments. Basically, if they need stuff from the library
    I try to make it available for them.  I also help people with GIS (Geographic Information Systems)
    projects and sometimes programming-related questions.
    
    * ep9k@virginia.edu 
    * Brown Science & Engineering Library office i046
    
* I like to be interrupted with questions! Please jump right in.

## Welcome to the UVA Library
* [Research Data Services](https://data.library.virginia.edu/)
* [Workshop Series](https://data.library.virginia.edu/training/)
  * Introduction to R (Jenn Huck)	                          Tuesday, 1/22	10:00 - 12:00	Brown 133
  * Data Preparation/Tidy Data in R (Michele Claibourn)       Tuesday, 1/29    10:00 - 12:00   Brown 133
  * Intro to QGIS (Erich Purpur)                              Monday, 2/4 10:00 - 12:00  Brown 133
  * Intro to Data Visualization with Tableau (Nancy Kechner)  Wednesday, 2/6  10:00 - 12:00 Brown 133
  
## Getting Python (this will take some time)
* [Windows](https://www.anaconda.com/download/#windows)
* [Mac](https://www.anaconda.com/download/#macos)


## Getting the files we are working with today
* Download the intro file here: https://github.com/epurpur/python-intro/blob/master/IntroToPython.py
  
# Goals for Today
1. Get python running
2. Get comfortable with python basics
3. Learn how to look up help

## Outline
1. Strings and Functions
2. Data types
3. Loops
4. Logic
5. How to import other libraries

### What is Python?
From www.python.org:
"Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance." 

Python is a general purpose programming language used for a huge variety of purposes. It's user community is growing rapidly!
(https://stackoverflow.blog/2017/09/06/incredible-growth-python/)




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

# Scripting vs Programming
It's a matter of modularity. Programs are designed to be modular and work with other programs. Scripts are designed to be single use.




# Learning Resources
* Pick up a book, there are many available through the UVA library website 
        * Learn Python the Hard Way (Available for free through UVA libraries)
        * [Link here](https://search.lib.virginia.edu/catalog/u7434195)
        
* CS 1110/1111 @ UVA
        * All resources available online!
        * https://cs1110.cs.virginia.edu/

* Resources available at UVA
        * Research Data Services - StatLab Fellows
        * https://data.library.virginia.edu/statlab/
        * statlab@virginia.edu
        
        * ARCS - Advanced Research Computing Services - Provides high performance computing expertise
        * https://arcs.virginia.edu/

* Many free resources online
  * [Practice Python](http://www.practicepython.org/)
  * [UVA Advanced Research Computing Services](https://arcs.virginia.edu/)
  * Ask me!
    * contact info at top of page
  * 





