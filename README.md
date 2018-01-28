# IEX-orderbook-ripper
Python script that saves all order book and trade data from the IEX exchange using a NoSQL database.

0. Install Homebrew: shell> /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

1. Install MongoDB: shell> brew install mongodb

2. Create directory as root: shell> sudo mkdir -p /data/db

3. Make directory writeable by everyone: shell> sudo chmod -R go+w /data/db¬¬

4. Start mongod server in one terminal window: shell> mongod

5. In a new terminal window cd into IEX-orderbook-ripper: shell> cd IEX-orderbook-ripper

6. Start the mongo Shell in this new terminal window once cd is done: shell> mongo

7. To show databases: > show dbs

8. To use a specific dbs: > use name_of_database, Ex: I called mine "IEX_Database" in the .py script so command would be > use IEX_Database

9. To show collections: > show collections, mine returns "ticker_data_collections" because thats what i named it in the .py script

10. To query posts: > db.Ticker_Data.find({}), should return the post i made with the .py script

-------------------[ M i s c. ]-------------------
To stop MongoDB:
press Control + C in the terminal where the mongod instance is running

To look for instances of mongod running on the system use:
shell> ps ax | grep mongod

To kill a process:
shell> kill -9 0000 or sudo !!

-------------------[ A l t e r n a t i v e ]-------------------
If you have mongodb installed via homebrew, to show current running services:
shell> brew services list

To start mongodb:

shell> brew services start mongodb

To stop mongodb if it's already running:

shell> brew services stop mongodb
