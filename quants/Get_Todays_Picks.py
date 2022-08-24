#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 03:14:11 2022

@author: bonganisiamtinta
"""

from Stock_List import Access_Tickers
from Get_Data import GetData
import pandas as pd

def todays_stock_data():
    tickers = Access_Tickers().get_stocks()
    data_frames = []
    for ticker in tickers:
        t = GetData(ticker, True).prepare_data_for_training()
        t['ticker'] = ticker
        # Date and short_result are not needed
        t = t[t.columns.drop('date')]
        t = t[t.columns.drop('short_result')]
        data_frames.append(t)
    return pd.concat(data_frames)
