import csv
import psycopg2

conn = psycopg2.connect("host=localhost dbname=gojek user=postgres password=admin")
cur = conn.cursor()

with open('/Users/ASUS/gojek/data/daily_order.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row.
    for row in reader:
        cur.execute(
            "INSERT INTO daily_order VALUES (%s, %s, %s, %s, %s)",
            row
        )
conn.commit()    