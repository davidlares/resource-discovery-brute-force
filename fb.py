import requests
from threading import Thread
import sys
import getopt

# func for displaying the name
def banner():
    print "*************************************** \n"
    print "* FB 0.1 \n"
    print "*************************************** \n"

# printing the how to use
def usage():
    print "Usage:"
    print "	-w: url (http://somesite.com/WORD)"
    print "	-t: threads"
    print "	-f: dictionary file\n"
    print " usage: fb.py -w http://www.target.com/WORD -t 5 -f dictionaries/common.txt\n"

class Attack(Thread):

    # constructor
    def __init__( self,word,url):
        Thread.__init__(self)
        try:
            self.word = word.split("\n")[0]
            self.urly = url.replace('WORD',self.word) # replacing WORD for the dictionary string
            self.url = self.urly
        except Exception, e:
            print e

    # performs the request
    def run(self):
        try:
            r = requests.get(self.url)
            print self.url + " - " + str(r.status_code) # url and status code
            i[0] =i[0] - 1 # update the thread counter (remove)
        except Exception, e:
                print e

# start program
def start(argv):
    banner()
    # checking parameters
    if len(sys.ar gv) < 5:
           usage()
           sys.exit() # stop the executon

    # assign URL, dictionary and Number of Threats
    try:
        opts, args = getopt.getopt(argv,"w:f:t:")
    except getopt.GetoptError:
        print "Error en arguments"
        sys.exit()

    # actions flags
    for opt,arg in opts:
        if opt == '-w' :
            url=arg
        elif opt == '-f':
            dict= arg
        elif opt == '-t':
            threads=arg

    # opening Dictionary
    try:
        f = open(dict, "r")
        words = f.readlines()
    except:
        print"Failed opening file: "+ dict+"\n"
        sys.exit()

    # calling the launcher with the dictionary, the urls and the words
    launcher_thread(words,threads,url)

# THREADS manage
def launcher_thread(names,th,url):
    global i
    i=[]
    resultlist=[]
    i.append(0)
    while len(names):
        try:
            if i[0]<th:
                n = names.pop(0)
                i[0]=i[0]+1
                thread = Attack(n,url) # Word and URL assignation to the class
                thread.start() # starting for each for

        except KeyboardInterrupt:
            print "FB interrupted by user. Finishing attack."
            sys.exit()
        thread.join()
    return

if __name__ == "__main__":
    try:
        start(sys.argv[1:])
    except KeyboardInterrupt:
        print "FB interrupted by user, killing threats"
