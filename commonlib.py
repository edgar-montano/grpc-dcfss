import os



def splitFile(fd,block_size):
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

        
