import sys
import xmlrpclib
rpc_srv = xmlrpclib.ServerProxy("http://localhost:8001/xmlrpc/")
result = rpc_srv.accessLiveSource("hello")
print result
