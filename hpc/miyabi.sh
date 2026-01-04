#!/bin/sh
#PBS -q debug-mig
#PBS -o out.log
#PBS -j oe
#PBS -m abe
#PBS -l select=1

uv run python -m hpc_tutorial.tutorial_normal
