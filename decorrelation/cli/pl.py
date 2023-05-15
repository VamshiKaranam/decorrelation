# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/CLI/pl.ipynb.

# %% auto 0
__all__ = []

# %% ../../nbs/CLI/pl.ipynb 4
import math

import zarr
import cupy as cp
import numpy as np
from matplotlib import pyplot as plt
import colorcet

import dask
from dask import array as da
from dask import delayed
from dask.distributed import Client, LocalCluster
from dask_cuda import LocalCUDACluster

from ..pl import emi
from ..sparse import points2raster
from .utils.logging import get_logger, log_args
# from decorrelation.cli.utils.dask import pad_internal

from fastcore.script import call_parse
