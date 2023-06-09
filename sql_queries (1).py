# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create =  ("""

CREATE TABLE IF NOT EXISTS songplays (

songplay_id SERIAL,

start_time timestamp NOT NULL,

user_id int NOT NULL,

level varchar,

song_id varchar,

artist_id varchar,

session_id int NOT NULL,

location varchar,

user_agent varchar, 

PRIMARY KEY(songplay_id)

);

""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users ( 

user_id int NOT NULL, 
    
first_name varchar NOT NULL, 
    
last_name varchar NOT NULL, 
    
gender text, 
    
level text, 
    
PRIMARY KEY(user_id));
                     
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs ( 

song_id varchar NOT NULL, 

title varchar NOT NULL, 

artist_id varchar NOT NULL, 

year int NOT NULL, 

duration DOUBLE PRECISION NOT NULL, 

PRIMARY KEY(song_id));

""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists ( 

artist_id varchar NOT NULL,

name varchar NOT NULL, 

location varchar NOT NULL,

latitude float, 

longitude float, 

PRIMARY KEY(artist_id));

""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time ( 

start_time timestamp,

hour TIME NOT NULL,

day int NOT NULL, 

week int NOT NULL, 

month int NOT NULL, 

year int NOT NULL, 

weekday text,

PRIMARY KEY(start_time));

""")

# INSERT RECORDS

songplay_table_insert = ("INSERT INTO songplays(songplay_id, start_time ,user_id, level, song_id, artist_id, session_id, location, user_agent) VALUES(%s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING ")

user_table_insert = ("INSERT INTO users(user_id, first_name, last_name, gender, level) VALUES(%s, %s, %s, %s,  %s) ON CONFLICT DO NOTHING ")

song_table_insert = ("INSERT INTO songs(song_id, title, artist_id, year, duration) VALUES(%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING ")

artist_table_insert = (" INSERT INTO artists (artist_id, name,location, latitude, longitude) VALUES(%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING ")


time_table_insert = ("INSERT TIME time (start_time, hour, day, week, month, year) VALUES(%s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING ")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
