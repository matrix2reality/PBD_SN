
# open file and read it
attempts_file = 'attempts.txt'
# use strip to strip out spaces and trim the line
data = [line.strip() for line in open(attempts_file, 'r')]

print len(data)

attempts_output = open('attempts.csv', 'w')
attempts_output.write('course, student number, email\n')

### printing all the data in command prompt
for item in data:
	entry = {}
	columns = item.split(' ')
	#print len(columns)
	#print columns[23]
	#line = columns[23].split('?')[1]
	line = columns[23].split('?')[1].strip('",')  ###cleaner looking data
	print line
	values = line.split('&')
	print values[0],
	print values[2],
	print values[3]
	attempts_output.write('%s, %s, %s\n' %  
		(values[0].split('=')[1], values[3].split('=')[1], values[2].split('=')[1]))
	
attempts_output.close()
