from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from gremlin_python.process.anonymous_traversal import traversal
import json
import time

# Chạy cmd trong file confiPropertyConsole.md trong Gremlin Console trước khi run file này


def read_data(path):
    f = open(path, 'r')
    data = json.load(f)
    return data


def add_wallet(wallet):
    n = g.addV('wallet').property('address', wallet['address']).next()
    for item in dict(wallet).items():
        if isinstance(item[1], list):
            for e in item[1]:
                g.V(n).property(item[0], e).next()
        else:
            g.V(n).property(item[0], item[1]).next()
    v = g.V(n).valueMap().next()
    print(v)


data_import = read_data('1e2_nodes_wallet.json')

connection = DriverRemoteConnection('ws://0.0.0.0:8182/gremlin', 'g')
g = traversal().withRemote(connection)

start = time.time()
for w in data_import:
    add_wallet(w)
finish = time.time()
print(finish - start)
connection.close()


