package org.apache.tinkerpop.gremlin.tinkergraph.structure;

import org.apache.tinkerpop.gremlin.driver.remote.DriverRemoteConnection;
import org.apache.tinkerpop.gremlin.structure.Vertex;

import java.util.List;

import static org.apache.tinkerpop.gremlin.process.traversal.AnonymousTraversalSource.traversal;

// Đã thêm thư viện thành công code nay chay gap loi, search khong ra, cam thay it nguoi hoi.

public class GraphTraversalSource {
    public static void main(String[] args) {
        org.apache.tinkerpop.gremlin.process.traversal.dsl.graph.GraphTraversalSource g = traversal().withRemote(
                DriverRemoteConnection.using("192.168.1.65", 8182));
        Vertex v1 = g.addV("person").property("name","marko").next();
        Vertex v2 = g.addV("person").property("name","stephen").next();
        g.V(v1).addE("knows").to(v2).property("weight",0.75).iterate();
        Vertex marko = g.V().has("person","name","marko").next();
        List<Vertex> peopleMarkoKnows = g.V().has("person","name","marko").out("knows").toList();
        System.out.println(peopleMarkoKnows);
    }

}