# pip install glob2
# pip install time

import glob2 as glob2
import pandas as pd
import numpy as np
import time
import os
import re
from datetime import date, datetime, timedelta

def walk_dir(path="C:/Users/shers/Desktop/SF/Буровая/data"):

    data_f = pd.DataFrame()

    # Датасет, который будем строить

    COLUMN_NAMES = ['Date/Time', 'TVD', 'DEPT', 'CDEPTH', 'HDTH', 'BPOS', 'HKLD', 'STOR', 'FLWI', 'RPM',
                    'SPPA', 'ECD', 'DLS', 'INCL', 'AZIM', 'GR', 'APRS', 'BVEL', 'RIG_STATE', 'Stick_Slip_Ratio',
                    'StickPercentage', 'ESD', 'hole', 'StuckPipe']
    data = pd.DataFrame(columns=COLUMN_NAMES)

    # Переименуем дублирующиеся колонки

    recolumn_1 = {
        'APRS_RT': 'APRS',
        'AZIM_CONT_RT': 'AZIM',
        'AZIMQ': 'AZIM',
        'ECD_RT': 'ECD',
        'ECD_ECO_RT': 'ECD',
        'DEPTH': 'DEPT',
        'INCL_CONT_RT': 'INCL',
        'INCLQ': 'INCL',
        'DHAP_DH_ECO_RT': 'APRS',
        'GR_ARC_RT': 'GR',
        'GRMA_ECO_RT': 'GR',
        'RIG_STATE_EXACT': 'RIG_STATE',
        'STICKRATIO': 'Stick_Slip_Ratio',
        'STICK_RT': 'StickPercentage'
    }
    recolumn_2 = {
        'APRS_RT': 'APRS',
        'AZIM_CONT_RT': 'AZIM',
        'AZIMQ': 'AZIM',
        'ECD_RT': 'ECD',
        'ECD_ECO_RT': 'ECD',
        'DEPTH': 'DEPT',
        'INCL_CONT_RT': 'INCL',
        'INCLQ': 'INCL',
        'DHAP_DH_ECO_RT': 'APRS',
        'GR_ARC_RT': 'GR',
        'GRMA_ECO_RT': 'GR',
        'RIG_STATE_EXACT': 'RIG_STATE',
        'STICKRATIO': 'StickPercentage',
        'STICK_RT': 'StickPercentage'
    }

    n=0
    for dirname, _, filenames in os.walk(path):
        for file in filenames:
            if file.split('.')[1] == 'xlsx' or file.split('.')[1]=='xls':
                data_f = pd.read_excel(path + '/' + file, skiprows=[1, 2])
            if file.split('.')[1] == 'csv':
                data_f = pd.read_csv(path + '/' + file, skiprows=[1, 2])

            data_f['hole'] = re.split(r'[-.]', file)[0]  # добавляем номер буровой
            if 'Stick_Slip_Ratio' in data_f.columns:
                data_f.rename(columns=recolumn_2, inplace=True)
            else:
                data_f.rename(columns=recolumn_1, inplace=True)

            if n == 0:
                data = data_f
                n += 1
            else:
                data = pd.concat([data, data_f], axis=0, ignore_index=True)
    data.to_csv('primary_data.csv', index=False)
# walk_dir()
