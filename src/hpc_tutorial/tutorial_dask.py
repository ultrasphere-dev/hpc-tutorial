import joblib
import numpy as np
from dask_mpi import initialize
from distributed import Client

initialize()
client = Client()
joblib.parallel_backend("dask")


def _task(seed: int) -> float:
    rng = np.random.default_rng(seed)
    A = rng.normal(size=(10, 1000, 1000))
    b = rng.normal(size=(10, 1000, 1))
    x = np.linalg.solve(A, b)
    return x.mean()


if __name__ == "__main__":
    results = joblib.Parallel(n_jobs=-1)(
        joblib.delayed(_task)(seed) for seed in range(10)
    )
    print(results)
