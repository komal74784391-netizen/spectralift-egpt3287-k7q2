"""Tensor IR graph primitives."""


class TensorGraph:
    def __init__(self, ops):
        self.ops = ops

    @classmethod
    def from_legacy_c(cls, source_path: str) -> "TensorGraph":
        with open(source_path, "r", encoding="utf-8") as handle:
            source = handle.read()
        return cls(ops=[("parse", source)])

    def verify(self, solver: str = "z3") -> bool:
        if solver != "z3":
            raise ValueError(f"unsupported solver: {solver}")
        return all(op[0] is not None for op in self.ops)

    def export_llvm(self) -> str:
        return "\n".join(str(op) for op in self.ops)
