# Task Schedular

A Command line schedular that will allow the use to add, Update and view scheduled tasks

features:

- text based menu for options
- each entry will have an **ID** allows the user to use the same task title twice as well as change the task title will still keeping a **primary key** to each task
- **adding** new entries to the schedule
- **Update** schedule
- **viewing** schedule
- persistence of schedule through **CSV** file
- **urgency** value from 0 to 4
- the program will also store the **progress** on each task

functionality:

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
