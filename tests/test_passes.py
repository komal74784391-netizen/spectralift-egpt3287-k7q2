from spectralift.ir import TensorGraph
from spectralift.compiler.passes import fuse_kernels


def test_fuse_policy():
    graph = TensorGraph(ops=[])
    fuse_kernels(graph, policy="balanced")
    assert graph.ops[-1][0] == "fuse"
