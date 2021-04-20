from __future__ import absolute_import
from pyti import catch_errors
from pyti.function_helper import fill_for_noncomputable_vals
from six.moves import range


def exponential_moving_average(data, period):
    """
    Exponential Moving Average.

    Formula:
    ema[0] = data[0], when i == 0
    ema[i] = ((data[i] * 2) + (period-1) * ema[i-1]) / float(period+1)
    """
    emas = data.copy()
    for i in range(1, len(data)):
        emas[i] = ((data[i] * 2) + (period-1) * emas[i-1]) / float(period+1)
    return emas
