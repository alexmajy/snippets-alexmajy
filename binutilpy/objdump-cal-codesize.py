#!/usr/bin/python
# deal with objdump -D to calculate the code size

import re
import fileinput

funpt = re.compile(r"([0-9a-fA-F]+) <(\w+)>:")

class Fundeco(object):
    def __init__(self):
        self.dic = {}

    def __call__(self, f):
        if self.dic.has_key(f):
            self.dic[f] += 1
        else:
            self.dic[f] = 0

        if self.dic[f] == 0:
            return f
        else:
            return f + "$" + str(self.dic[f])
    
    

class Process(object):
    def __init__(self):
        self.state = 0
        self.dic = {}
        self.buf = ""
        self.fun = ""
        self.fdec = Fundeco()


    def __call__(self, line):
        if self.state == 0:
            f = funpt.search(line)
            if f == None:
                pass
            else:
                addr, fun = f.groups()
                fun = self.fdec(fun)
                self.fun = fun
                self.dic[fun] = int(addr,16)
                self.state = 1
        elif self.state == 1:
            if line == "\n" or line == "\t...\n":
                assert len(self.buf) != 0, '\n'.join(["last line, line:", self.buf, line ])
                s = self.buf.split('\t')
                eaddr = int(s[0][:-1],16)
                self.dic[self.fun] = eaddr - self.dic[self.fun] 
                self.dic[self.fun] += len(s[1].split())
                self.state = 0
            else:
                self.buf = line



p = Process()

for line in fileinput.input():
    p(line)

for k, v in p.dic.iteritems():
    print k, v
