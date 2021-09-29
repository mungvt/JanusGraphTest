from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from gremlin_python.process.anonymous_traversal import traversal
from gremlin_python.process.traversal import Cardinality

# Code này chạy được và đã thêm được đỉnh cạnh, nhưng không có property dạng list

connection = DriverRemoteConnection('ws://192.168.1.65:8182/gremlin', 'g') # địa chỉ ip là của Gremlin-server
# The connection should be closed on shut down to close open connections with connection.close()
g = traversal().withRemote(connection)

# Reuse 'g' across the application

v1 = g.addV(
    'wallet'
).property(
    'address',
    '0xaced50ad963cb0ad712af7d1123341407ee033f0'
).next()

# g.V().drop().next()
v = g.V().count().next()
print(v)

connection.close()
