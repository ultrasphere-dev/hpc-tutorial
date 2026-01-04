#!/bin/bash -l
#PBS -q debug-g
#PBS -o out.log
#PBS -j oe
#PBS -m abe
#PBS -l select=1
#PBS -l walltime=03:00

cd ${PBS_O_WORKDIR}
uv run python -m hpc_tutorial.tutorial_normal
