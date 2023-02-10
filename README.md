# AirBnB Clone Made with Python.

![AirHBnB image](https://github.com/betascribbles/AirBnB_clone/blob/main/assets/hbnb_logo.png)

## Description

HBnB is a simple copy of the [AirBnb Website](https://www.airbnb.com/).
It implement some of its features not all ☺️ . Only the fundamental concepts of programming in the higher level track.

The project will be composed of:

- A command interpreter to manipulate data withour a visual interface, like in a shell.
- A website (the front-end) that shows the final product to everyone: static and dynamic
- A database or files that store data.
- An API that provides a communication interface between the front-end and you data (retrieve, create, delete, update)

### Data will be implemented as below:
![Data diagram](https://github.com/betascribbles/AirBnB_clone/blob/main/assets/data_diagram.jpg)

## Concepts Learnt
- Unit testing using `unittest` module
- Python packages
- Serialization and Deserialization
- `*args` and `**kwargs`
- The `datetime` module

## Implementation

To start the CLI just type `./console.py` in your commandline.
The CLI can `create` a new object, `retrieve` an object from a file or database, `count`, `compute stats`, `update` attributes and `destroy` an object.

**Example:**
```bash
karis@karispc~$ ./console.py
(hbnb)

```

**For help type `help` or `?`**
```bash
karis@karispc~$ ./console.py
(hbnb) help

Documented commands(type help <topic>):
=======================================
EOF help quit create show destroy
all update count

(hbnb)
(hbnb)
(hbnb) quit
karis@karispc:~$
```

**In non interactive mode:**
```bash
karis@karispc:~$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
=========================================
EOF help quit create show destroy all
update count
(hbnb)
karis@karispc:~$ cat test_help
help
karis@karispc:~$
karis@karispc:~$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
```

All tests should also pass in non-interactive mode: `$ echo "python3 -m unittest discover tests" | bash`
