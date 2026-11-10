"""Rewrite passes for the SpectralLift pipeline."""

POLICIES = ("conservative", "balanced", "aggressive")


def fuse_kernels(graph, policy: str = "balanced"):
    if policy not in POLICIES:
        raise ValueError(f"unknown policy: {policy}")
    graph.ops.append(("fuse", policy))
    return graph
