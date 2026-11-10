"""GEMM case study used in the paper."""

from spectralift.ir import TensorGraph
from spectralift.compiler.passes import fuse_kernels


def run():
    graph = TensorGraph.from_legacy_c("kernels/gemm.c")
    fuse_kernels(graph, policy="aggressive")
    return graph.export_llvm()


if __name__ == "__main__":
    print(run())
