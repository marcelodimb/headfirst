import sys

try:
    with open(sys.argv[1]) as data:
        man = []
        other = []

        for line in data:
            try:
                (author, message) = line.split(':', 1)

                message = message.strip()

                if author == 'Man':
                    man.append(message)
                elif author == 'Other Man':
                    other.append(message)

                try:
                    with open('man_file.txt', 'w') as man_file, open('other_file.txt', 'w') as other_file:
                    	for line in man:
                    		man_file.write(line + '\n')

                    	for line in other:
                    		other_file.write(line + '\n')
                except:
                    print "Error"

            except ValueError:
                pass

except IOError as e:
    print "Error: " + str(e.strerror)
