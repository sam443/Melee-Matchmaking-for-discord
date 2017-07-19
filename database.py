##  Melee matchmaking bot ##
##						  ##
##						  ##
##						  ##
##  Resources:            ##
##						  ##
## https://tutorials.botsfloor.com/creating-chatbots-for-discord-90407e1bf382
## http://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html#creating-a-new-sqlite-database


#This file handles database stuff

import sqlite3            #db library
from pathlib import Path  #check if file exists, reference: https://stackoverflow.com/questions/82831/how-do-i-check-whether-a-file-exists-using-python

def create_db():
	db_filename     = 'elo_db.sqlite' # name of the sqlite database file
	table_name      = 'users'   	  # name of the table to be created
	new_field       = 'userID'        # name of the column, user id and primary key; INTEGER
	username        = 'username'      # name of column, username, STRING
	field_elo       = 'ELO'           # name of column, ELO, INTEGER
	location        = 'location'	  # location of player
	integer         = 'INTEGER'       # column data type int. 8 bit signed.
	txt             = 'TEXT'		  # column data typt text.
	default_elo     = 1200			  # starting ELO value.

	# Connecting to the database file
	conn = sqlite3.connect(db_filename)
	c = conn.cursor()


	#userID primary key
	c.execute('CREATE TABLE IF NOT EXISTS {tn} ({nf} {ft} PRIMARY KEY)'\
		.format(tn=table_name, nf=new_field, ft=field_type))


	#adding elo column. Defaut value of 1200 (for now.)
	c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct} DEFAULT '{df}'"\
		.format(tn=table_name, cn=field_elo, ct=field_type_int, df=default_elo))


	#adding username column.
	c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct} "\
		.format(tn=table_name, cn=username, ct=field_type_txt))


	#adding location table
	c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct} "\
		.format(tn=table_name, cn=location, ct=field_type_txt))

	# Committing changes and closing the connection to the database file
	conn.commit()
	conn.close()
   

#returns true if db exists, else false
def db_exists():
	db_file = Path("elo_db.sqlite")
    if db_file.is_file():
    	return True
    else:
    	return False

#database initialization function. Checks if db exists and if not, creates it. called each time the bot is ran.
def db_init():
	if not db_exists():
		create_db()
	return


#called when user types !register. They also type a location
def db_register(user_id, username, location): #int, string, string
	
	table_name  = 'users'   	  # name of the table to be appended.
	col_name1   = 'userID'        # name of the column, user id and primary key; INTEGER
	col_name2   = 'username'      # name of column, username, STRING
	col_name3   = 'location'      # name of column, location, STRING


	# Connecting to the database file
	conn = sqlite3.connect(sqlite_file)
	c = conn.cursor()

	# A) Inserts an ID with a specific value in a second column
	try:
		c.execute("INSERT INTO {tn} ({idf}, {cn1}, {cn2), {cn3} VALUES (user_id, userID, username, location )"\
			.format(tn=table_name, idf=col_name1, cn1=col_name2, cn2=col_name3))
			#          'Users'		   'userID'       'username'     'location'

	except sqlite3.IntegrityError:
		print('ERROR: ID already exists in PRIMARY KEY column {}'.format(id_column))
		#returning false will have the bot say that user already registered.
		conn.close()
		return False

	conn.commit()
	conn.close()
	return True
