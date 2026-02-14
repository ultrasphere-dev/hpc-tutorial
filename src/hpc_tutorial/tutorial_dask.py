import joblib
import numpy as np
from cm_time import timer
from dask_mpi import initialize
from distributed import Client


def _task(seed: int) -> float:
    rng = np.random.default_rng(seed)
    A = rng.normal(size=(100, 1000, 1000))
    b = rng.normal(size=(100, 1000, 1))
    x = np.linalg.solve(A, b)
    return x.mean()


if __name__ == "__main__":
    with timer() as t:
        initialize()
        client = Client()
        joblib.parallel_backend("dask")
    print(f"Initialized Dask client in {t.elapsed:g}s")

    with timer() as t:
        results = joblib.Parallel(n_jobs=-1)(
            joblib.delayed(_task)(seed) for seed in range(2)
        )
        print(results)
    print(f"Computed results in {t.elapsed:g}s")

    with timer() as t:
        client.retire_workers()
        client.close()
    print(f"Closed Dask client in {t.elapsed:g}s")
