import os



def splitFile(fd,block_size):
    """Takes a string of a file and splits file into array based on
    block size.

    fd - string of desired file to split
    Block_size - desire block size to split file
    """

    #new_block is a new array that contains the 
    #contents of the file, split based on block_size
    new_block = []
    with open(fd,'rb') as f:
        while True:
            block = f.read(block_size)
            if block:
                new_block.append(block)
            else:
                break
        
    return new_block

        
