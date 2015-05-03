# -*- coding: utf-8 -*-
import sys

try:
    data = open(sys.argv[1], 'r')

    for line in data:
        try:
            (author, message) = line.split(':', 1)
            print author + ' says: ' + message,
        except ValueError:
            pass

    data.close()

except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
