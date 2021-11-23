# Task Scheduler

## 1 Introduction

The purpose of this Project is to provide a tool to organise and keep track of a given set of tasks. throughout the following document the Project will be referred to as TS for "Task Scheduler"

## 1.1 Requirements

- The program will need to be able to save and retrieve user tasks from the save file
- The program will need to be able to add, update and view tasks

features:

- text based menu for options
- each entry will have an **ID** allows the user to use the same task title twice as well as change the task title will still keeping a **primary key** to each task
- **adding** new entries to the schedule
- **Update** schedule
- **viewing** schedule
- persistence of schedule through **CSV** file
- **urgency** value from 0 to 4
- the program will also store the **progress** on each task

## 1.2 Analysis
**feature requirements**

```
The program will need to be able to save and retrieve user tasks from the save file
```
the users will be prompted with a **text based terminal menu** to add any task they may wish to add, the menu will be defined and designed in the successive sections of this document. The menu will be designed to allow users to access all the features of the final product.

```
The program will need to be able to add, update and view tasks
```
The saving function will be independent than the remaining features

In the following section the requirements listed above will be discussed in further details on why they are necessary

### Saving files

For TS to reach it's goal it must provide the users for a way to retrieve their agenda at a later date which is why it's vital to implement an agenda saving module.

### Urgency

In many cases the users might want to 'flag' a task as urgent even if the task may have a long deadline, which is why there is a need for an 'urgency' value for each task so users can

## 2 Design

## 2.1 Saving system

An important factor in user experience is to allow users to view their task even if the TS fails due to say a bug, to achieve this goal the agenda will be saved as CSV file to allow the user to open the agenda file in a moment of panic or hurry in other programs that support the format such as Microsoft Excel. This allows users to maintain control over their data as they do not necessary require TS to access their agenda, providing users with peace of mind and tranquillity.



functionality:

## 2 Design

### 2.1 Menu

The command line menu will be as follows:

```code
options:

		0: Quit
		1: View tasks
		2: Add new entry to the schedule
		3: Update entry
```

if options is:

- 0

	- the program will save and close the current schedule file
	- the program will then close

- 1

	- the program will display the current tasks as follows

		```code
		current tasks:

		| id | task title | Description or any notes | deadline | urgency | progress|
		| #1 | groceries | make sure to get milk | 21st November | 1 | on my way |
		```

	- the output format is likely to change

	- back to the menu

- 2

	- the user will be prompted to enter task name, notes, deadline and an urgency level
	- the data will be saved to the CSV file
	- back to the menu

- 3

	- the user will be prompted with the current task using code from option 1
	- the user will chose the ID of the task to change or update
	- the user will be prompted with each property of the entry if left empty the property will not be changed
	- once the user has updated the entry all the data will be saved in the CSV file
	- back to the menu

### 2.2 Task model


- the program will show the user the task in order of urgency based on deadline or 'urgency' parameter which will be set by user for particularly important task

Entries model:

| id   | task title | Description or any notes |   deadline    | urgency | progress  |
| :--: | :--------: | :----------------------: | :-----------: | :-----: | :-------: |
| #1   | groceries  |  make sure to get milk   | 21st November |    1    | on my way |

The task will be saved in a CSV file in much the same manner:

```csv
id; task title; notes; deadline; urgency; progress;
#1; groceries; make sure to get milk; 21st November; 1; on my way
```


**report needs the following**:

The documentation you will need to submit in addition to all source code, should be as follows:
•	Brief description of the aims of program
•	Analysis of the requirements of the program (1-2 pages)
•	Design – may be documented by flow charts, class diagrams etc. (2-4 pages)
•	Testing – table of tests to be undertaken to prove that the program achieves its goals (1-2 pages)
•	Critique – what worked, what didn’t and what could have been improved (up to 1 page)
