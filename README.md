# **Search-Algorithms-Visualizer**
This project presents a visual representation of some AI Search Algorithms such as Dijkstra's Algorithm and A*, the project was developed using Python and Pygame.

## **Requirements**
To succesfully run this project you'll need to have installed `Python 3.8.10` or later and `pygame 2.1.2` or later.

### **How to install pygame**
To install pygame you need Python's package manager: `pip`.
Run in your command terminal the following line
```
pip install pygame
```
If you'd like to install a specific version of pygame
```
pip install pygame==v.v
```
where v.v is the version of the module.

## **Installation**
There are two options for downloading this project to your computer:
1. Clone the repository
2. Download the ZIP file

### 1. Clone the repository
1. To clone the repo to your computer, access the folder in which you would like to have the project.
2. Open the terminal on that folder
3. Run this command in the terminal:
```
git clone https://github.com/MarianaS01/Search-Algorithms-Visualizer.git
```

### 2. Download the ZIP file
You can download the ZIP file clicking the ```Download ZIP``` button as shown in the picture below.

![Download ZIP](https://user-images.githubusercontent.com/78234785/224164211-8156a336-6c7b-446c-b802-efc164ae3ae8.png)


After downloading, unzip the folder in your preferred directory.


## **Run the program**
After downloading the project, run the following commands in your terminal (depending on your OS):

### Linux or Mac
```
cd Search-Algorithms-Visualizer/
python3 code/main.py
```

### Windows
```
cd Search-Algorithms-Visualizer\
python code\main.py
```

## **How to use it**
The program has a grid in which the selected algorithm will find the destination given an origin an a goal, even with obstacles. It also has some buttons that will let the user interact with the program, this buttons are described below.
* **SET ORIGIN**: This button will let you select a cell as origin, this cell will be colored BLUE. 
* **SET GOAL**: This button will let you select a cell as goal, this cell will be colored RED.
* **BLOCK/UNBLOCK CELLS**: When clicked, this button will let you block or unblock cells of the grid to form obstacles, you only need to click the button once to select this option, if you want to unblock a cell that was previously blocked, you just need to click it again.
* **SPEED**: The speed buttons will let you increase or decrease the speed of the algorithm visualization.
* **DELETE PATH**: This button comes in handy when you already have run one algorithm and you want to select another without deleting the grid you have. The button will just delete the path and process found by the previous algorithm.
* **CLEAN GRID**: With this button you will clean completely the grid, deleting previous colored cells.
* **SELECT ALGORITHM**: This button displays a menu containing the algorithms available to select.
* **START SEARCH**: This button starts the search using the algorithm previously selected.

### Demo video
Here you have a video that shows the program in action.
https://user-images.githubusercontent.com/78234785/218279660-58483187-57f1-4252-90bc-e72e86201f7c.mp4

## **Future Work**
The next goal for this project is to add more algorithms.
