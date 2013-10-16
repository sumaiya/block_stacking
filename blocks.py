#Sumaiya Hashmi
#problem set 6b part 3

import sys

def blockStacking(blocks):
    """takes an array of arrays of block dimensions """

    allBlocks = []
    #this will contain all the blocks we have to work with
    
    for block in blocks:
        allBlocks += makeOrientations(block)
    # include all 3 possible orientations
    
    # might have duplicates. uses more space but otherwise ok
    
    allBlocks.sort()
    # built in sort uses mergesort so is O(n log n)
    allBlocks.reverse()
    # sort blocks by their smallest base dimension, in decreasing order

    BS = [] # dynamic programming array will be len(allBlocks) x 1
    result = [None]*len(allBlocks) #keep track of blocks in the solution
    
    for i, block in enumerate(allBlocks):
        BS.append(block[2])
        # initialize with height of block

    for i, blockTop in enumerate(allBlocks):
        # for each block i in 1 ... n
        for j, blockBelow in enumerate(allBlocks[:i]):
            # for each block j in 1 ... i-1
            if biggerBase(blockBelow, blockTop):
                # check if block j can be stacked below block i
                
                heightWithBlockBelow = BS[j] + blockTop[2]
                heightWithoutBlockBelow = BS[i]

                # does including the stack ending in j improve the total height?
                if heightWithBlockBelow > heightWithoutBlockBelow:
                    result[i] = j # block j is below block i. keep track of this
                    BS[i] = heightWithBlockBelow # add i to stack ending in j

    tallest = max(BS) #find tallest tower
    top = BS.index(tallest) #find index of tallest block

    sequence = [top] #create a sequence of block indices

    nextBlock = result[top] #the block below top is at index top in result[]
    while nextBlock != None: #go through result[] until we reach None
        sequence.append(nextBlock) #add the block below
        nextBlock = result[nextBlock]
    numBlocks = len(sequence)
    
    print "The tallest tower has %d blocks and a height of %d" \
             % (numBlocks, tallest)

    sequence.reverse() #want to print bottom block to top block
    output = [numBlocks]
    #get list of block dimensions from indices in sequence
    for index in sequence:
        output.append(allBlocks[index])
    return output


def makeOrientations(block):
    orientations = []
    for i in range(3):
        orientations.append(getBlockWithOrientation(block, i))
    return orientations

def getBlockWithOrientation(block, h):
    height = block[h] #let the hth dimension be height
    dimensions = [0,1,2]
    dimensions.remove(h) #get the remaining 2 dimensions
    l, w = dimensions #set them as length and width
    #figure out which is smaller so we can create blocks in a consistent way
    smaller = block[l] if (block[l] < block[w]) else block[w]
    larger = block[l] if (block[l] > block[w]) else block[w]
    # return in consistent order: smaller dimension, larger dimension, height
    return [smaller, larger, height]

def biggerBase(base, top):
    #check if block base is larger than block top in both dimensions
    return base[0] > top[0] \
        and base[1] > top[1]


if __name__ == "__main__":
    if len(sys.argv) != 3: # make sure command line arguments are correct
        print "Wrong number of arguments"

    else:
        inputFile = sys.argv[1]
        outputFile = sys.argv[2]
        i = open(inputFile)
        lines = i.readlines() #read in the input file
        i.close()

        n = int(lines[0]) # first line of input file is number of blocks
        if n < 1:
            print "Wrong number of blocks"
        else:    
            f = open(outputFile, 'w')
            blocks = []
            # array of blocks starts on second line of input file
            for block in lines[1:]:
                blocks.append([int(n) for n in block.split()])

            solution = blockStacking(blocks)
            
            f.write(str(solution[0]) + '\n') # print the number of blocks in solution
            for block in solution[1:]:
                for dimension in block:
                    f.write(str(dimension) + ' ') # print the 3 dimensions on one line
                f.write('\n')  # iterate through the days and print each day's value
            f.close()
