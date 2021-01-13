import os
import pandas_datareader as pdr

SPY = pdr.get_data_tiingo('SPY', api_key='4d109a21f529efe178e73aae6e710b8c24330e71')
SPY.tail()