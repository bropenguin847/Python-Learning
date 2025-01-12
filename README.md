# 📖 Python Learning 🚀
For **Scientific Programming Course** which introduces the fundamentals of Scientific Programming.
The focus is on programming fundamentals, algorithm implementation, program design, and visualization, aiming to develop skills in scientific computing along with tools and techniques for solving engineering challenges.
<br>

There are 12 chapters in Scientific Programming course:
- Chapter 1: Overview of Languages
- Chapter 2: Introduction to Programming Platform (Python)
- Chapter 3: Complex Data Type
- Chapter 4: Control FLow
- Chapter 5: Functions
- Chapter 6: Input & Output
- Chapter 7: Debugging [Excluded]
- Chapter 8: Graphics
- Chapter 9: Data Interpolation
- Chapter 10: Polynomials
- Chapter 11: Data Analytics
- Chapter 12: Object Oriented Programming (OOP) [Excluded]
The notes for the excluded slides will still be provided
<br>

🐍🐍🐍

This repo is currently used as my personal notes, with scripts to aid my learning.

I would like to keep this as my way of learning how to maintain a repo, make documentation that is neat and user friendly.

In the future, perhaps I will make a wiki page for all the shortcuts to learn Python.

---
## [**Notes** ✍️](https://github.com/bropenguin847/Python-Learning/tree/main/Notes)
Contains notes for each chapter. Notes will be continually updated.
For array notes, contain specific notes regarding numpy arrays, numpy functions and so on.
Further references can be found in the appendix.

---
## [Exercises ᕙ(  •̀ ᗜ •́  )ᕗ](https://github.com/bropenguin847/Python-Learning/tree/main/exercises)
In exercises folder, contain exercises for python, such as array manipulation, bubble sort 
and mistakes that I have made during my tests
(regretting life)

---
## [Assignment 📚](https://github.com/bropenguin847/Python-Learning/tree/main/Assignment)
In the assignment folder, contains 3 tasks. All requires using Python to extract data from csv file using Python libraries such as Pandas.

In all the .py file, the problem scenario's are stated on the top.
datastat_module is a custom Python file that contains all the functions that can help out with the other files. It is essentially a custom library.

For the data in Assignment, outliers and missing values have been added in the .csv files.

---
## [Quiz](https://github.com/bropenguin847/Python-Learning/tree/main/Quiz)
In this folder, There are several questions from my quiz in class. Quiz 1 and Quiz 2 are very similar, with almost same way to solve the problems, just using different datas. A good way to learn how to read xlsx file using python and plot graphs.

---
## Scripts 📝
All the folders labeled with Chapter contain scripts for each chapter. Some have xlsx or csv files used as data. Feel free to try it out.

Some Python files are combined together to reduce clutter and because the codes are very similar.
Such as example1&2 are combination of example1 and example2 in Chapter 4.

In Chapter 8, the folder 'Signals' is for Signals and System course. It's an assignment, the code is an alternative to plotting graphs using MatLab. However, a MatLab version of the code is also available.

Chapter 7 (Debugging) and Chapter 12 (OOP) is not included in this repo, but I will try to find the notes for both of those chapter.

Additional links for Debugging and OOP:<br>
[Debugging in VS Code](https://www.youtube.com/watch?v=b4p-SBjHh28)<br>
[OOP](https://www.youtube.com/watch?v=JeznW_7DlB0)<br>

---
## Setup
This course uses Python as its high level programming language with various libraries such as NumPy and Matplotlib, with [VSCode as IDE](https://code.visualstudio.com/download).
A few setups are required when programming Python using VSCode. [Here are the steps](https://code.visualstudio.com/docs/languages/python).
Users will need to manually install Python and the [libraries](#libraries-) as well.

[Enable variable explorer in VSCode](https://stackoverflow.com/questions/69240557/does-vs-code-have-variable-explorer-object-like-we-have-it-in-spyder)

Alternatively, [SpyderIDE](https://www.spyder-ide.org/) can be used. Spyder IDE offers an integrated environment combining an editor, console, and variable explorer, making it ideal for scientific computing. It supports data visualization, efficient debugging, and preinstalled with libraries like NumPy, Pandas, and Matplotlib.

|IDE|Advantages|Disadvantages|
|---|---|---|
|VSCode|Vast library of extensions, built-in version control, versatile for various programming languages|Steep learning curve, manual setup for each language|
|Spyder|Strong focus on scientific programming, integrated variable explorer and plotter, easy to use|Limited extensions, less versatile|


Every Python file is saved in .py file format. Conventionally, Python files follow the camel_case naming style.<br>
Use #%% to create seperate cells in code to run them individually.
To create an interactive notebook, create a file that ends with ".ipynb"

### Pick your poison and learn Python ( ◡̀_◡́)ᕤ

---
## Libraries 📖
Numpy, Matplotlib, Pandas & SciPy. With links for official documentation.
```python
python -m pip install numpy
python -m pip install matplotlib
python -m pip install pandas
python -m pip install scipy
```
[🎲 NumPy documentation](https://numpy.org/doc/stable/user/absolute_beginners.html)<br>
[📈 MatPlotLib documentation](https://matplotlib.org/stable/index.html)<br>
[🐼 Pandas Documentation](https://pandas.pydata.org/docs/index.html)<br>
[🐍 SciPy Documentation](https://docs.scipy.org/doc/scipy/tutorial/index.html#user-guide)<br>

[NumPy Tutorial](https://www.w3schools.com/python/numpy/default.asp)<br>
[Matplotlib Tutorial](https://www.w3schools.com/python/matplotlib_intro.asp)<br>
[Pandas Tutorial](https://www.w3schools.com/python/pandas/default.asp)<br>
[SciPy Tutorial](https://www.w3schools.com/python/scipy/scipy_intro.php)<br>

---
## Appendix 📌
Cheatsheet for subscripting and operator precedence
<img src="images\appendix1.png" width="750" height="550" alt="subscripting"><br>
<img src="images\appendix2.png" width="700" height="700" alt="operator precedence"><br>
<img src="images\special_character.png" width="600" height="400" alt="Special Character"><br>
<img src="images\unicode_symbol.png" width="600" height="400" alt="Unicode Symbol"><br>


All the colors for matplotlib<br>
[Simple matplotlib markers, line style and color](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html)<br>
[🔴🔵🟡matplotlib colors🟢🟠🟣](https://matplotlib.org/stable/gallery/color/named_colors.html#css-colors)<br>

[Python SpeedSheet](https://speedsheet.io/s/python)<br>

How to write clean Python code<br>
[Pep8 Style Guide for Python Code](https://pep8.org/)<br>

---
## For beginners / Helpful Links
[CS50 Introduction to Python](https://www.youtube.com/playlist?list=PLhQjrBD2T3817j24-GogXmWqO5Q5vYy0V)

[Python explained simply](https://www.youtube.com/watch?v=x7X9w_GIm1s)

[Python Full Course for Beginners by Mosh Hamedani](https://www.youtube.com/watch?v=_uQrJ0TkZlc)

[Python in 1 hour by Mosh Hamedani](https://www.youtube.com/watch?v=kqtD5dpn9C8)

[Python Beginners by NeetCode (follow-along)](https://www.youtube.com/watch?v=s3KhqPjBPaQ)

[Python Exercises](https://www.w3schools.com/python/python_exercises.asp)<br>

[Python for coding interviews](https://www.youtube.com/watch?v=0K_eZGS5NsU)<br>

[Online Python Interpreter](https://www.onlinegdb.com/online_python_compiler)

[Python Online Game Tutorial Playlist](https://www.youtube.com/playlist?list=PLzMcBGfZo4-kR7Rh-7JCVDN8lm3Utumvq)

[Data Analysis with Python Full Course](https://www.youtube.com/watch?v=r-uOLxNrNk8)<br>


<br>
[Awesome ChatGPT prompts](https://github.com/f/awesome-chatgpt-prompts)

[ChatPGT prompts for writing and generating codes](https://dev.to/techiesdiary/chatgpt-prompts-for-writing-and-generating-codes-59kf)

### [A Comprehensive Guide to Using ChatGPT Prompts for Coding Tasks](https://www.learnprompt.org/chat-gpt-prompts-for-coding/)

---
## Feel free to raise any issues if you found any mistakes or outdated information in this repo. Have a nice journey into the world of Python. All the best ᯓ★!!
### *ੈ✩‧₊˚༺☆༻*ੈ✩‧₊˚
!need to make custom pdf for each chapter