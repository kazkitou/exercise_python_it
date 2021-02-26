# このchapter 11-3 のプログラムを単独で動かす場合、pytestが終了しないため一時的にコメントアウトしておく
# from xmlrpc.server import SimpleXMLRPCServer


# def now():
#     from datetime import datetime

#     data = str(datetime.utcnow())
#     print("Server sent", data)
#     return data


# server = SimpleXMLRPCServer(("localhost", 6789))
# server.register_function(now, "now")
# server.serve_forever()
