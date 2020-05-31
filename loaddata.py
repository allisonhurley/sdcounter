import sys
import csv 
import random
from random import randint
from datetime import datetime
from datetime import timedelta
from dateutil.parser import parse
import psycopg2
import psycopg2.extras

# args - 
#      csv file
#      roomname

if len(sys.argv) < 3:
    print("""args: python fakeroom.py
      csv_file_name
      roomname""")
    sys.exit(-1)

fname = sys.argv[1]
roomname = sys.argv[2]
start = parse('4/1')
print(roomname)

connection = psycopg2.connect(database = "ahurley", user = "ahurley")
with connection:
    with connection.cursor(cursor_factory = psycopg2.extras.RealDictCursor) as cursor:
        try:
            cursor.execute("insert into rooms (name) values (%s)", (roomname, ))
        except psycopg2.Error:
            1 # ignore

with connection:
    with connection.cursor(cursor_factory = psycopg2.extras.RealDictCursor) as cursor:
        cursor.execute("select * from rooms where name = %s", (roomname, ))
        result = cursor.fetchone()
        if result == None:
            print(f"Error inserting {roomname}")
            sys.exit(-2)
        room_id = result["id"]

        prev_count = 0
        curdate = ""
        with open(fname, newline='') as csvfile:
            csvfile.readline()
            reader = csv.reader(csvfile)
            for row in reader:
                count = int(float(row[5]))
                found_date = f'{row[1]}/{row[3]}/{row[0]}'
                if found_date != curdate:
                    start = start + timedelta(days=1)
                    curdate = found_date
                date = f'{start} {row[2]}-0500'
                date = parse(date)
                # print(f'{date}: {row[5]} - {count}')

                delta = count - prev_count
                if delta != 0:
                    cursor.execute("INSERT INTO journal (room_id, previous_count, count, applied_at) VALUES(%s,%s,%s,%s)",
                            (room_id, prev_count, count, date))
                    prev_count = count 

