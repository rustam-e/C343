#!/usr/bin/env python

import sys, math, kfasta

# Rolling hash impl
class RollingHash:
    
    # initializes the rolling hash with the hash value for string s
    def __init__(self, s):
        self.r = 0
        self.n = 0
        for character in s:
            self.append(character)
        
#        raise Exception("Not implemented!")
    
    # character c was appended to the current string
    # this function updates the current hash to reflect that change
    # has no return value
    def append(self, c):
        self.r = (self.r * 256 + ord(c)) % 41
        self.n += 1
#        raise Exception("Not implemented!")

    # returns the current hash
    def hash(self):
        return self.r
#        raise Exception("Not implemented!")
    
    # character c was deleted from the start of the curret string
    # this function updates the current hash to reflect that change
    # has no return value
    def skip(self, c):
        # self.u -= ord(c) * self.b**(self.n - 1)
        self.r = (self.r - ord(c) * (self.b**(self.n-1) % self.p)) % self.p
        self.n -= 1
#        raise Exception("Not implemented!")

# Multidict is similar to a Python dict except it holds a set of values for each key
# if the key is not present, returns an empty list
class Multidict:
    # initializes the multidict with pairs of the form (k, v) where k is the key and v is the associated value
    def __init__(self, pairs=[]):
        self.keys = {}
        for pair in pairs:
            self.put(pair[0],pair[1])
#        raise Exception("Not implemented!")
    
    # if k is not present, inserts k in the multidict with value v
    # if k is present, inserts v into the list of values associated with k
    def put(self, k, v):
        if k in self.keys:
            self.keys.get(k).append(v)
        else:
            self.keys[k] = [v]            
#        raise Exception("Not implemented!")
    
    # returns the list of values associated with k
    def get(self, k):
        if (k in self.keys):
            return self.keys[k]
        else:
            return []
#        raise Exception("Not implemented!")

# Searches for commonalities between sequences a and b by comparing subsequences
# of length k.  The sequences a and b should be iterators that return nucleotides.
# The table is built by computing one hash every m nucleotides (for m >= k).
def getExactSubmatches(a, b, k):
#     print "Building table from sequence A..."
    seqtable = Multidict(subsequenceHashes(a, k))
#     print "...done building table."
    for hashval, (bpos, bsubseq) in subsequenceHashes(b, k):
        for apos, asubseq in seqtable.get(hashval):
            if asubseq != bsubseq:
                continue
            yield (apos, bpos)
    return

def subsequenceHashes(seq, k):
    try:
        assert k > 0
        subseq = ''
        for i in range(0, k):
            subseq += seq.next()
        rh = RollingHash(subseq)
        pos = 0
        while True:
            yield (rh.hash(), (pos, subseq))
            rh.skip(subseq[0])
            nextitem = seq.next()
            subseq = subseq[1:] + nextitem
            rh.append(nextitem)
            pos += 1
    except StopIteration:
        return

def getExactSubmatchesByInterval(a, b, k, m):
    print "Building table from sequence A..."
    seqtable = Multidict(intervalSubsequenceHashes(a, k, m))
    print "...done building table."
    for hashval, (bpos, bsubseq) in intervalSubsequenceHashes(b, k, m):
        for apos, asubseq in seqtable.get(hashval):
            if asubseq != bsubseq:
                continue
            yield (apos, bpos)
    return

def intervalSubsequenceHashes(seq, k, m):
    assert m >= k
    try:
        pos = 0
        while True:
            subseq = ''
            for i in range(0, k):
                subseq += seq.next()
            rh = RollingHash(subseq)
            yield (rh.hash(), (pos, subseq))
            for i in range(0, m-k):
                seq.next()
            pos += m
    except StopIteration:
        return

def compareFasta(getExactSubmatches, afile, bfile, k):
    a = kfasta.FastaSequence(afile)
    b = kfasta.FastaSequence(bfile)
    return getExactSubmatchesByInterval(a, b, k, 100)

def run_batch():
    f=open('tests.txt', 'rb'); tests = eval(f.read()); f.close()
    for (a, b, k, expected) in tests:
        matches = list(getExactSubmatches(iter(a), iter(b), k))
        assert len(matches) == len(expected)
        for m in expected:
            assert m in matches
    print "all tests passed!"

if (len(sys.argv) == 2 and sys.argv[1] == 'test'):
    run_batch()
elif (len(sys.argv) == 4 and sys.argv[1] == 'runfasta'):
    matches = compareFasta(getExactSubmatches, sys.argv[2], sys.argv[3], 16)
    print sum(1 for m in matches)
else:
    foo = 'GCATCGGC'
    bar = 'CCATCGCCATCG'
    print list(getExactSubmatches(iter(foo), iter(bar), 5))
