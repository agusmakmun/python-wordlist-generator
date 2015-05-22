"""
Name            : Python Wordlist Generator
Created By      : Agus Makmun (Summon Agus)
Blog            : bloggersmart.net - python.web.id
Documentation   : https://github.com/agusmakmun/Python-Wordlist-Generator/
License         : GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
Thanks to       : falsetru - http://stackoverflow.com/a/21559115
"""

import time
import itertools, string
print "Creating ..."
print "Start Time: ", time.strftime('%H:%M:%S')
chrs = string.printable.replace(' \t\n\r\x0b\x0c', '')      #use module string method for all chars
min_length, max_length = 1, 2                               #minimum and maximum created

create = open('wordlist.txt', 'w')
for n in range(min_length, max_length+1):                   #creating looping with 'for'
    for xs in itertools.product(chrs, repeat=n):            #itertools method
        #print ''.join(xs)                                  #you can test with it
        saved = ''.join(xs)                                 #create new variable
        create.write("%s\n" % saved)                        #create output for wordlist.txt

create.close()                                              #close create after looping 'for'
print "End Time: ", time.strftime('%H:%M:%S')
