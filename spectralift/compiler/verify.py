"""Verification harness for lifted kernel graphs."""


def verify_graph(graph, solver: str = "z3") -> bool:
    return graph.verify(solver=solver)
