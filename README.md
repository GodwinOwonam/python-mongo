***pymongo*** is a Python library that allows you to interact with MongoDB databases. In this tutorial, we will learn how to use the library to perform various operations on a MongoDB database.

In this project, we take it a step further by providing database management with pymongo package.

We provide a means for creating collections, dropping collections and updating collections.
Each collection is represented by a Model stored in the 'models' directory.

To create the collections, add them to the collection as a class in a single file stored in a python file.
Then import the class in the 'manage_database.py' file in the 'create_models' array.
Next, run the 'manage_database.py' file to create the collections by passing the 'up' argument like *python3 manage_database.py up*.
The 'up' argument indicates that the collections should be created.


To update the collections, add the fields to be updated in the class in the python file.
Then import the class in the 'manage_database.py' file in the 'update_models' array.
Next, run the 'manage_database.py' file to update the collections by passing the 'update' argument like *python3 manage_database.py update*.
The 'update' argument indicates that the collections should be updated.

To drop the collections, import the class in the 'manage_database.py' file in the 'drop_models' array.
Next, run the 'manage_database.py' file to drop the collections by passing the 'drop' argument like *python3 manage_database.py down*.
The 'down' argument indicates that the collections should be dropped.