##################
# Master rpc node 
#################

import time
import commonlib
import master_pb2
from grpc.beta import implementations

class MasterNode(master_pb2.BetaMasterNodeServicer):
    def Store(self,request,context):
        """Stores a file on the data node
        """
        
        print("storing file")
        
        return master_pb2.StoreReply(reply_msg=request.file_name)

    def Read(self,request,context):
        """Reads a file from data node
        """

        print("reading file ")


def main():
    """Creates Master Node server and listens onto port 50051"""
    print("\n\tStarting server on localhost:50051...")
    server = master_pb2.beta_create_MasterNode_server(MasterNode())
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(commonlib.TIMEOUT)
    except KeyboardInterrupt:
        print("\n\tKilling the server...\n")
        server.stop(grace=0)
        exit()
    except:
        print("Error has occured, please refer to log")



if __name__ == '__main__':
    main()
