# Name: Praneet Jain

# Task: DNA analysis

# This program reads DNA sequencer output and computes statistics, such as
# the GC content. 


###########################################################################
### Libraries
###

# The sys module supports reading files, command-line arguments, etc.
import sys


###########################################################################
### Read the nucleotides into a variable named seq
###

# Specify a file name
if len(sys.argv) < 2:
    print "You must supply a file name as an argument when running this program."
    sys.exit(2)
# The file name specified on the command line, as a string.
filename = sys.argv[1]
# A file object from which data can be read.
inputfile = open(filename)

# All the nucleotides in the input file that have been read so far.
seq = ""
# The current line number (= the number of lines read so far).
linenum = 0


for line in inputfile:
    linenum = linenum + 1
    # if we are on the 2nd, 6th, 10th line...
    if linenum % 4 == 2:
        # Remove the newline characters from the end of the line
        line = line.rstrip()
        seq = seq + line


###########################################################################
### Compute statistics
###

# Total nucleotides seen so far.
total_count = 0
# Number of G and C nucleotides seen so far.
gc_count = 0
at_count = 0
a_count = 0
t_count = 0
g_count = 0
c_count = 0


# for each base pair in the string,
for bp in seq:
    # increment the total number of bps we've seen
    total_count = total_count + 1

    # if bp is A, increment its count
    if bp == 'A':
       a_count = a_count + 1
        
    # if bp is T, increment its count
    if bp == 'T':
       t_count = t_count + 1
    
    # if bp is G, increment its count
    if bp == 'G':
       g_count = g_count + 1
        
    # if bp is C, increment its count
    if bp == 'C':
       c_count = c_count + 1
    
    
    
    # next, if the bp is a G or a C,
    if bp == 'C' or bp == 'G':
        # increment the count of gc
        gc_count = gc_count + 1
    
    # if bp is A or T
    if bp == 'A' or bp == 'T':
        # increment the count of at
        at_count = at_count + 1

sum_ACTG = a_count+t_count+c_count+g_count
        
# divide the gc_count by the total_count
gc_content = float(gc_count) / sum_ACTG

#divide the at_count by the gc_count
at_gc_content_ratio = float(at_count)/gc_count

# divide at_count by the total_count and multiply the result by 100 to find percentage
at_content_percentage = (float(at_count) / sum_ACTG) * 100

#content type - high, low or moderate
gc_content_type=""
if gc_content*100 > 60:
    gc_content_type = "high GC content"
elif gc_content*100 < 40:
    gc_content_type = "low GC content"
else:
    gc_content_type = "moderate GC content"


# Print the content
print 'GC-content:', gc_content
print 'AT-content:', at_content_percentage
print 'G-count:', g_count
print 'C-count:', c_count
print 'T-count:', t_count
print 'A-count:', a_count
print 'Sum count', sum_ACTG
print 'Total count', total_count
print 'seq length', len(seq)
print 'AT/GC ratio:', at_gc_content_ratio
print 'GC Classification:',gc_content_type



