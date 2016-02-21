#!/usr/bin/env python
#
# TapeBagel interpreter by zlowram (@zlowram_)
#
# Based on language specs: https://esolangs.org/wiki/TapeBagel

import os
import sys
import re

class tapeBagel:
    def __init__(self):
        self.tape = [0]*3
        self.ptr = 0
        self.integers = {'*': 0, '**': 1, '***': 2} 
        self.alphabet = [' '] + [chr(i) for i in xrange(ord('A'), ord('Z')+1)]

    def exec_instr(self, instr):
        if re.match("^%(\+\+|--|#|&|%)$", instr):
            if instr[1:] == "++":
                self.tape[self.ptr] += 1
            elif instr[1:] == "--":
                self.tape[self.ptr] -= 1
            elif instr[1] == "#":
                self.ptr += 1
            elif instr[1] == "&":
                # Not implemented 
                pass
            elif instr[1] == "%":
                self.ptr = 0

        if re.match("^#(#|%)$", instr):
            if instr[1] == "#":
                for i in range(0, len(self.tape)):
                    self.tape[i] = 0
            elif instr[1] == "%":
                for i in range(0, len(self.tape)):
                    self.tape[i] = 1

        m = re.match("^(%|\*+)(\+|-|\^|$|&)(%|\*+)$", instr)
        if m:
            ops = [m.group(1), m.group(3)]
            if m.group(2) == '&':
                self.tape[self.ptr] = self.tape[self.integers[ops[0]]] * self.tape[self.integers[ops[1]]]
            if m.group(2) == '+':
                self.tape[self.ptr] = self.tape[self.integers[ops[0]]] + self.tape[self.integers[ops[1]]]
            if m.group(2) == '$':
                self.tape[self.ptr] = self.tape[self.integers[ops[0]]] / self.tape[self.integers[ops[1]]]
            if m.group(2) == '-':
                self.tape[self.ptr] = self.tape[self.integers[ops[0]]] - self.tape[self.integers[ops[1]]]
            if m.group(2) == '^':
                self.tape[self.ptr] = self.tape[self.integers[ops[0]]] ** self.tape[self.integers[ops[1]]]

        m = re.match("^(@|@@)(%|\*+)$", instr)
        if m:
            if m.group(1) == "@":
                print self.alphabet[self.tape[self.integers[m.group(2)]]]
            if m.group(1) == "@@":
                print self.tape[self.integers[m.group(2)]]

        if re.match("^&(&|@)$", instr):
            if instr[1] == '&':
                # Not implemented 
                pass
            elif instr[1] == '@':
                os.system('cls' if os.name=='nt' else 'clear')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "usage: " + sys.argv[0] + " <script>"
        sys.exit(1)

    f = open(sys.argv[1])
    instructions = f.read().split()
    tp = tapeBagel()
    for inst in instructions:
        tp.exec_instr(inst)    
