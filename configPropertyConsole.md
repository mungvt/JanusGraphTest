:remote connect tinkerpop.server bin/remote.yaml session
:remote console
graph
g 
g.V().count()
mgmt = graph.openManagement()
mgmt.makePropertyKey('tokens').dataType(String.class).cardinality(LIST).make()
mgmt.makePropertyKey('balanceChangeLogTimestamps').dataType(Long.class).cardinality(LIST).make()
mgmt.makePropertyKey('balanceChangeLogValues').dataType(Double.class).cardinality(LIST).make()
mgmt.makePropertyKey('depositChangeLogTimestamps').dataType(Long.class).cardinality(LIST).make()
mgmt.makePropertyKey('depositChangeLogValues').dataType(Double.class).cardinality(LIST).make()
mgmt.makePropertyKey('borrowChangeLogTimestamps').dataType(Long.class).cardinality(LIST).make()
mgmt.makePropertyKey('borrowChangeLogValues').dataType(Double.class).cardinality(LIST).make()
mgmt.makePropertyKey('dailyFrequencyOfTransactions').dataType(Long.class).cardinality(LIST).make()
mgmt.makePropertyKey('dailyTransactionAmounts').dataType(Double.class).cardinality(LIST).make()
mgmt.commit()