import csv

with open("network_data.csv") as f:
	print f.read()

with open("network_data.csv") as f:
	python_csv = csv.reader(f)
	for row in python_csv:
		print "{router} in {country} has ip {ip}".format(router=row[0],country=row[2],ip=row[1])
