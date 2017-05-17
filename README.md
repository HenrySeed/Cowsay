# Cowsay

A styled cowsay, It uses a cleaner looking speech bubble and a variable line length.

So long as you're in the same directory you can just:
```
>>> from cowsay import *
>>> print(cowsay('Hello World'))
 _______________
/  Hello World  \
\_______________/
   V

    ^__^
    (oo)\_______
    (__)\       )\/\/
        ||----w\|
        ||     ||

>>>
```
or,
```
> python3 cowsay.py This works too
 __________________
/  This works too  \
\__________________/
   V

    ^__^
    (oo)\_______
    (__)\       )\/\/
        ||----w\|
        ||     ||
```

It can also do longer paragraphs too!
```
 ____________________________________________
/  You can do even longer sentences too      \
|  and the bubble will change along with     |
|  the words. You can change the line        |
|  length via the line_length var in         |
|  cowsay function.                          |
\____________________________________________/
   V

    ^__^
    (oo)\_______
    (__)\       )\/\/
        ||----w\|
        ||     ||
```
(c) Henry Seed 2017
