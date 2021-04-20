from __future__ import absolute_import
import numpy as np
import warnings
from pyti.function_helper import fill_for_noncomputable_vals
from pyti import catch_errors
from six.moves import range


def simple_moving_average(data, period):
    """
    Simple Moving Average.

    Formula:
    SUM(data / N)
    """
    # even if not enough period, we can still mean the avaiable data and better than np.nan
    return [np.mean(data[max(0,idx-(period-1)):idx+1]) for idx in range(0, len(data))]
