#!/usr/bin/python3

import sqlite3
conn = sqlite3.connect('software.db')

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE software
             (name text, latest text, date text, desc text, orig text, url text)''')

# Insert a row of data
c.execute("INSERT INTO software VALUES ('adljack','1.1.0','2018-08-13','OPL3/OPN2 synthesizer','github','https://github.com/jpcima/adljack/')")
c.execute("INSERT INTO software VALUES ('dexed','0.9.4','2018-03-19','DX7 synthesizer','github','https://github.com/asb2m10/dexed/')")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
