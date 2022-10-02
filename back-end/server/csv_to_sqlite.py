import csv, sqlite3

con = sqlite3.connect("moonquakes.db") # change to 'sqlite:///your_filename.db'
cur = con.cursor()


query = "CREATE TABLE IF NOT EXISTS `moonquakes` (" + \
        "id INTEGER PRIMARY KEY AUTOINCREMENT, " +\
        "lat TEXT DEFAULT '' NOT NULL, " +\
        "lat_err TEXT DEFAULT '' NOT NULL, " +\
        "long TEXT DEFAULT '' NOT NULL, " +\
        "long_err TEXT DEFAULT '' NOT NULL, " +\
        "type TEXT DEFAULT '' NOT NULL, " +\
        "sub_type TEXT DEFAULT '' NOT NULL, " +\
        "side TEXT DEFAULT '' NOT NULL, " +\
        "year TEXT DEFAULT '' NOT NULL, " +\
        "depth TEXT DEFAULT '' NOT NULL, " +\
        "depth_err TEXT DEFAULT '' NOT NULL, " +\
        "assumed TEXT DEFAULT '' NOT NULL" +\
        ");" # use your column names here

cur.execute(query)

with open('../../csv/nakamura_2005_dm_locations.csv.','r') as f: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(f) # comma is default delimiter
    to_db = [(i['Lat'], i['Lat_err'], i['Long'], i['Long_err'], 'moonquake', 'Deep', i['Side'], '2005', i['Depth'], i['Depth_err'], i['Assumed']) for i in dr]
    #print(to_db)


cur.executemany("INSERT INTO moonquakes (lat, lat_err, long, long_err, type, sub_type, side, year, depth, depth_err, assumed) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
con.commit()
con.close()