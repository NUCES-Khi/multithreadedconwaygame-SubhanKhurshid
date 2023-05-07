# ASSIGNMENT # 03
## Name   - Muhammad Subhan Khurshid
## RollNo - 21k-3096

## Overview
For this assignment, I have implemented Conway's Game of Life algorithm in C language using a two-dimensional array to represent the grid of cells. The rules of the game were implemented using conditional statements. To run the algorithm concurrently, I created multiple POSIX threads to process different regions of the grid independently. I used mutexes and condition variables to synchronize access to the shared data structures such as the grid of cells. Finally, I used shell scripting to measure the speedup achieved by running the final application with various numbers of threads. The time command was used to measure the execution time of the program.

## Screenshots Of Output
### Program Output
<img width="354" alt="newAss3" src="https://user-images.githubusercontent.com/105592966/236699731-63392105-6c99-4036-a9d0-68ac3cba057a.PNG">


### Time Command Output
<img width="284" alt="newTime" src="https://user-images.githubusercontent.com/105592966/236699737-daaefbeb-b074-433e-9ef3-13411ed277db.PNG">


### Output After SpeedUp using Shell Scripting
<img width="367" alt="speedNew" src="https://user-images.githubusercontent.com/105592966/236699744-0ec825d0-0b35-4f4a-ba46-9b5d23916343.PNG">

