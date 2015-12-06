import os
from grpc.beta import implementations

#global definitions used throughout program
MB = 1<<20
TIMEOUT = 10 
DEBUG = True


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


def loadBalancer(config_file):
    """Loads cf and determines which IP address has best ping.
    """ 
    best_ip =  []
    

    return best_ip
