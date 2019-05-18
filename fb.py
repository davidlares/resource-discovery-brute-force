import requests
from threading import Thread
import sys
import getopt
import re
from termcolor import colored

# func for displaying the name
def banner():

    print "==============================="
    print "davidBrute"
    print "==============================="

# printing the how to use
def usage():
    print "Usage:"
    print "	-w: url (http://somesite.com/WORD)"
    print "	-t: threads"
    print "	-c: excluding status-code"
    print "	-d: dictionary file\n"
    print " usage: fb.py -w http://www.target.com/WORD -t 5 -d dictionaries/common.txt\n"

class Attack(Thread):
    # constructor
    def __init__( self, word, url, hidecode):
        Thread.__init__(self)
        try:
            self.word = word.split("\n")[0]
            self.urly = url.replace('WORD',self.word) # replacing WORD for the dictionary string
            self.url = self.urly
            self.hidecode = hidecode
        except Exception(e):
            print e

    # performs the request
    def run(self):
        try:
            r = requests.get(self.url)
            lines = str(r.content.count("\n"))
            chars = str(len(r._content))
            words = str(len(re.findall("\S+", r.content)))
            code = str(r.status_code)

            if self.hidecode != code:
                if '200' <= code < '300':
                    print colored(code, 'green') + "\t\t" + chars + " \t\t" + words + " \t\t " + lines +"\t" + self.url + "\t\t"
                elif '400' <= code < '500':
                    print colored(code, 'red') + "\t\t" + chars + " \t\t" + words + " \t\t " + lines +"\t" + self.url + "\t\t"
                elif '300' <= code < '400':
                    print colored(code, 'blue') + "\t\t" + chars + " \t\t" + words + " \t\t " + lines +"\t" + self.url + "\t\t"
                else:
                    print colored(code, 'yellow') + "\t\t" + chars + " \t\t" + words + " \t\t " + lines +"\t" + self.url + "\t\t"
            # print self.url + " - " + str(r.status_code)) # url and status code
            i[0] =i[0] - 1 # update the thread counter (remove)
        except Exception(e):
            print e

# start program
def start(argv):
    banner()
    # checking parameters
    if len(sys.argv) < 5:
           usage()
           sys.exit() # stop the executon

    # assign URL, dictionary and Number of Threats
    try:
        opts, args = getopt.getopt(argv,"w:d:t:c:")
    except getopt.GetoptError:
        print "Error in arguments"
        sys.exit()

    hidecode = 000
    # actions flags
    for opt,arg in opts:
        if opt == '-w' :
            url = arg
        elif opt == '-d':
            dict = arg
        elif opt == '-t':
            threads = arg
        elif opt == '-c':
            hidecode = arg

    # opening Dictionary
    try:
        f = open(dict, "r")
        words = f.readlines()
    except:
        print "Failed opening file: " + dict + "\n"
        sys.exit()

    # calling the launcher with the dictionary, the urls and the words
    launcher_thread(words, threads, url, hidecode)

# THREADS manage
def launcher_thread(names, th, url, hidecode):
    global i
    i=[]
    resultlist=[]
    i.append(0)
    print ""
    print "Code" + "\t\tchars\t\twords\t\tlines\t\tURL"
    print ""

    while len(names):
        try:
            if str(i[0]) < th:
                n = names.pop(0)
                i[0]=i[0]+1
                thread = Attack(n, url, hidecode) # Word and URL assignation to the class
                thread.start() # starting for each for

        except KeyboardInterrupt:
            print "davidBrute interrupted by user. Finishing attack."
            sys.exit()
        thread.join()
    return

if __name__ == "__main__":
    try:
        start(sys.argv[1:])
    except KeyboardInterrupt:
        print "davidBrute interrupted by user, killing threats"
