################
# Client gRPC
###############
import commonlib
import master_pb2
from grpc.beta import implementations
import sys
def main():
    """Client makes a request to the MasterNode to either store or read
    file.
    """
    if sys.argv[1] == '-h' or len(sys.argv)<3:
        print("Incorrect paramater usage.  Please use the following:")
        print("1.) ./client -s file_name")
        print("2.) ./client -r file_name timestamp\n")
        print("\t\tOperations\n")
        print("-s\t\tStore operation")
        print("-r\t\tRead Operation")
        print("\t\tParameters\n")
        print("file_name\t name of desired file")
        print("timestamp\t set 0 if lastest file, otherwise specify previous file version")
        exit()

    #connection to masternode
    channel = implementations.insecure_channel('localhost',50051)
    stub = master_pb2.beta_create_MasterNode_stub(channel)
    #file descriptor name passed as paramater
    fd = sys.argv[2]
    blocks = str("1")
    try:
        if(sys.argv[1] == "-s"):
            response = stub.Store(master_pb2.StoreRequest(file_name=fd,file_content=blocks),commonlib.TIMEOUT)
            print(response.reply_msg)
        else:
            response =stub.Store(master_pb2.ReadRequest(file_name=sys.argv[2],timestamp=sys.argv[3]),commonlib.TIMEOUT)
    except:
        print("error occured")

if __name__ == '__main__':
    main()
