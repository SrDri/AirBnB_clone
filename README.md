<h1 align="center">
	<img src="https://www.tabbykatz.com/hbnb.png">
	AirBnB_clone
</h1>

# Synopsis

The Airbnb clone project for which we are creating a copy of the [Airbnb](https://www.airbnb.com/).
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…


## Features

### Command Interpreter

#### Description
The Command Interpreter is used to manage the whole application's functionality from the command line.

#### Functionalities of this command interpreter
+ Crete a new object.
+ Retrieve an object from a file, database, etc.
+ Execute operation on objects. e.g. Count, compute statistics, etc.
+ Update object's attributes.
+ Destroy an object.

# Usage

To launch the console application in interactive mode simply run:

```bash
$ ./console.py
```

```bash
(hbnb)help

Documented commands (type help <topic>):


(hbnb)help all

Prints all string representation of
all instances based or not on the class name

(hbnb)help create

Creates an instance of a defined class.

(hbnb)destroy
** class name missing **

(hbnb)create BaseModel
17fa8a0a-f3f8-453f-b0d6-d636802fcafa

(hbnb)show BaseModel 17fa8a0a-f3f8-453f-b0d6-d636802fcafa
[BaseModel] (17fa8a0a-f3f8-453f-b0d6-d636802fcafa) {'id': '17fa8a0a-f3f8-453f-b0d6-d636802fcafa', 'created_at': datetime.datetime(2021, 7, 1, 2, 48, 30, 971047), 'updated_at': datetime.datetime(2021, 7, 1, 2, 48, 30, 971310)}


update BaseModel 17fa8a0a-f3f8-453f-b0d6-d636802fcafa first_name "Juan Carabali"
(hbnb)

(hbnb)show BaseModel 17fa8a0a-f3f8-453f-b0d6-d636802fcafa
[BaseModel] (17fa8a0a-f3f8-453f-b0d6-d636802fcafa) {'id': '17fa8a0a-f3f8-453f-b0d6-d636802fcafa', 'created_at': datetime.datetime(2021, 7, 1, 2, 48, 30, 971047), 'updated_at': datetime.datetime(2021, 7, 1, 2, 48, 30, 971310), 'first_name': 'Juan Carabali'}
```

### or to use the non-interactive mode run:

``` bash
echo "your-command-goes-here" | ./console.py
```

```bash
echo "help" | ./console.py

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

echo "help quit" | ./console.py
(hbnb)Quit command to exit the program

echo "create BaseModel" | ./console.py
(hbnb)acacc732-5d67-4d94-bc1a-b32b43dcabb6

echo "show BaseModel acacc732-5d67-4d94-bc1a-b32b43dcabb6" | ./console.py
(hbnb)[BaseModel] (acacc732-5d67-4d94-bc1a-b32b43dcabb6) {'id': 'acacc732-5d67-4d94-bc1a-b32b43dcabb6', 'created_at': datetime.datetime(2021, 7, 1, 3, 5, 45, 966638), 'updated_at': datetime.datetime(2021, 7, 1, 3, 5, 45, 967401)}

echo "show BaseModel 17e3e759-2f88-4555-825c-d2a1866772f9" | ./console.py
(hbnb)[BaseModel] (17e3e759-2f88-4555-825c-d2a1866772f9) {'id': '17e3e759-2f88-4555-825c-d2a1866772f9', 'created_at': datetime.datetime(2021, 7, 1, 2, 48, 30, 971047), 'updated_at': datetime.datetime(2021, 7, 1, 2, 48, 30, 971310), 'first_name': 'Juan Carabali'}
```


## Commands

Commands | Description | Usage
-------- | ----------- |-------- |
**help** or **?**| Displays the documented commands. | **help**
**quit**     | Exits the program. | **quit**
**EOF**      | Ends the program. Used when files are passed into the program. | N/A
**create**  | Creates a new instance of the \<class_name\>. Creates a Json file with the object representation. and prints the id of created object. | **create** \<class_name\>
**show**    | Prints the string representation of an instance based on the class name and id. | **show** \<class_name class_id\>
**destroy** | Deletes and instance base on the class name and id. | **destroy** \<class_name class_id\>
**all** | Prints all string representation of all instances based or not on the class name | **all** or **all** \<class_name class_id\>
**update** | Updates an instance based on the class name and id by adding or updating attribute | **update** \<class_name class_id key value\>

## Tests

If you wish to run at the test for this application all of the test are located
under the **test/** folder and can execute all of them by simply running:

``` bash
python3 -m unittest discover tests
```

from the root directory.


## Bugs

+ No known bugs at this time.
