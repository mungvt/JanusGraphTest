# JanusGraphTest
## Tutorial
- Download JanusGraph 0.6 từ trang chủ
- Start Janus server
./bin/janusgraph-server.sh console trava.yaml
- Start Gremlin Console để connect được đến server
+ ./bin/gremlin.sh
các command để connect
+ :remote connect tinkerpop.server bin/remote.yaml session
+ :remote console
+ graph
+ g
+ g.V().count()

** lưu ý chỉnh host trong remote.yaml và trava.yaml cho giống với ip của máy

- Muốn khai báo property dạng list, cần thực hiện trong console, command như sau
+ mgmt = graph.openManagement()
+ mgmt.makePropertyKey('tokens').dataType(String.class).cardinality(LIST).make()
+ mgmt.commit()

String.class, hoặc Long.class, Double.class tham khảo data type của janusgraph hoặc java để chọn cho phù hợp

** thực hiện add vertex bình thường trong code python
+ g.addV('wallet').property('address', 'w1').property('tokens', ['0x123','0x345'])

