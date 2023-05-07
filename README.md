# ASSIGNMENT # 03
## Name   - Muhammad Subhan Khurshid
## RollNo - 21k-3096

## Overview
For this assignment, I have implemented Conway's Game of Life algorithm in C language using a two-dimensional array to represent the grid of cells. The rules of the game were implemented using conditional statements. To run the algorithm concurrently, I created multiple POSIX threads to process different regions of the grid independently. I used mutexes and condition variables to synchronize access to the shared data structures such as the grid of cells. Finally, I used shell scripting to measure the speedup achieved by running the final application with various numbers of threads. The time command was used to measure the execution time of the program.

## Screenshots Of Output
### Program Output
<img width="626" alt="pic1" src="https://user-images.githubusercontent.com/105592966/236698134-972e7f5a-8c7f-4206-bff3-91edcb3ae059.PNG">


### Time Command Output
<img width="516" alt="time" src="https://user-images.githubusercontent.com/105592966/236698151-cd616acd-0c9f-448d-af05-0f950967d0a9.PNG">

### Output After SpeedUp using Shell Scripting
<img width="608" alt="sp" src="https://user-images.githubusercontent.com/105592966/236698234-363e7b9b-d4da-4746-8c89-ebd0092dda03.PNG">
