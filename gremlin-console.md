## Khởi tạo TinkerGraph
```conf = new BaseConfiguration()
conf.setProperty("gremlin.tinkergraph.vertexIdManager","LONG")
conf.setProperty("gremlin.tinkergraph.edgeIdManager","LONG")
conf.setProperty("gremlin.tinkergraph.vertexPropertyIdManager","LONG");[]
graph = TinkerGraph.open(conf)
g=graph.traversal()
:set max-iteration 1000
```

## Thêm đỉnh
```
g.addV('wallet').property('address', 'w1').property('timestamp', [19991222,12243124,132425,515]).property('value', [1.1,10.0002, 0.000005])
g.addV('wallet').property('address', 'w2').property('timestamp', [199932,12777124]).property('value', [10.0002, 100000000.000005])
```

## Thêm cạnh 
```
w1 = g.V().has('address', 'w1').next()
w2 = g.V().has('address', 'w2').next()
w1.addEdge('deposit', w2)
```

## Reference link 
- https://kelvinlawrence.net/book/Gremlin-Graph-Guide.html#ld
- https://kelvinlawrence.net/book/Gremlin-Graph-Guide.html#_adding_an_airport_vertex_and_a_route_edge
- https://kelvinlawrence.net/book/Gremlin-Graph-Guide.html#listprop