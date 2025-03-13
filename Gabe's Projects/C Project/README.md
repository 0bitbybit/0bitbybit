# Welcome to My Mastermind
***

## Task
This my_mastermind game gives you a default of 10 chances to guess four comninations of colors. The 'colors' here 
are represented by digits 0 through 8. If you guess them all in order, you win!  The game starts by allowing 
the game master to set the secret code, with and the number of rounds aka chances, default is a random four digit number
and 10 chances. If you guess some right, the game will tell you how many you guessed correctly that are in the correct 
position and how many in the wrong position. For example, if the secret code is '1131' and you enter '1310', 
you will be told well placed = 2 , misplaced = 1.

## Description
This game's code was first written in Python to more quickly get down most of the game logic. It was then 
translated to C.  No pointers were used except for the one in the command line functions for the secret code.
The EOF functionality relies on a return error triggered in the entry function and checked in the main function. 

## Installation
Go to your IDE, create a new folder, drop in the mastermind C program "main.c", drop in the Makefile.  

## Usage
Go to your IDE terminal, make sure you're in the folder where you dropped the files, if not, navigate to it using
cd.  In the terminal type: ./main -c 1234 -t 5. The '-c' and '-t' set the secret code and number of rounds, respectively.
Or you can just run the defaults.   

### The Core Team


<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px' /></span>
