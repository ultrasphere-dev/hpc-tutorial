#!/bin/bash -l
#PBS -q debug-g
#PBS -o out.log
#PBS -j oe
#PBS -m abe
#PBS -V
#PBS -l select=1
#PBS -l walltime=03:00
#PBS -l mail_power_info=true

#export UV_CACHE_DIR=/work//m
cd ${PBS_O_WORKDIR}
uv run python -m hpc_tutorial.tutorial_normal
