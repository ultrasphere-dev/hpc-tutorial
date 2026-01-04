import numpy as np


def _task(seed: int) -> float:
    rng = np.random.default_rng(seed)
    A = rng.normal(size=(10, 1000, 1000))
    b = rng.normal(size=(10, 1000, 1))
    x = np.linalg.solve(A, b)
    return x.mean()


if __name__ == "__main__":
    print(_task(0))
