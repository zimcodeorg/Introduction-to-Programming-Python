12-week version of the Introduction to Programming: Python Course

Inside the textbook source directory you will find the source code for the
textbook pdf written in latex. Each chapter has a separate folder that conatins
all the relevant figures and text. This is to make the code more modular
rather than having everything in one file.

All dependencies can be found in the files and installed using any Tex package
manager. In addition, to compile the code you will need to install a Python
package called Pygments (as as python >2.7) used to format the coding environments.
It is mostly likely already installed with Python but if not, you can install it
using pip

pip install pygments

While changes can be made to any of the tex files in the subfolders, only the
main.tex file can be compiled to produce the pdf file. There template.tex file
can be used to make new chapters and gives examples for almost any use case for
formatting the book. All definitions in the preamble are done in structure.tex
