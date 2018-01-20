import sys
import re

fname_in = sys.argv[1]

mpiRE = re.compile(r'(Sun|Mon|Tue|Wed|Thr|Fri|Sat)\s+(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d+\s+\d+:\d+:\d+\s+\d+<(stdout|stderr)>:\s?(.*)')

def mpifilt(fin):
    for line in fin:
        # Strip off MPI-added header
        match = mpiRE.match(line)
        if (match is None):
            yield line
        else:
            yield match.group(4)

beginRE = re.compile('-+ BEGIN parameters to snow_adv')
endRE = re.compile('-+ END parameters to snow_adv')

def parameters_filt(fin):

    # ------ Looking for BEGIN
    for line in fin:
        if beginRE.match(line) is not None:
            break

    for line in fin:
        if endRE.match(line) is not None:
            return
        yield line

# --------------------------------------------------
literals = {
    'F' : '.false.',
    'T' : '.true.',
    'NaN' : '0d0/0d0'
}

def format_literal(x):
    if x in literals:
        return literals[x]

    # Test for integer
    dot = x.find('.')
    if dot < 0:
        return x

    e = x.find('E')
    if e >= 0:
        y = list(x)
        y[e] = 'd'
        return ''.join(y)
    return x + 'd0'

        
# --------------------------------------------------
def out_general(words):
    if len(words) > 2:
        print('{} = (/{}/)'.format(words[0], ','.join([format_literal(x) for x in words[1:]])))
    else:
        print('{} = {}'.format(words[0], format_literal(words[1])))

def out_ijihp(words):
    print('xcol%i={}\nxcol%j={}\nxcol%ihp={}'.format(words[1], words[2], words[3]))

outputers = {
    'xcol%(i,j,ihp)' : out_ijihp
}

with open(fname_in, 'r') as fin:
    for line in parameters_filt(mpifilt(fin)):
        words = line.split()

        if words[0] in outputers:
            outputers[words[0]](words)
        else:
            out_general(words)
