import pandas as pd
import pygslib

import os

def test_read_gslib_to_pandas():
    df = pygslib.read_to_pandas('tests/jura_sample.dat')
    reference_df = pd.read_csv('tests/jura_sample.dat', skiprows=13, names=['Xloc','Yloc','Landuse','Rock','Cd','Co','Cr','Cu','Ni','Pb','Zn'], delim_whitespace=True)
    assert df.equals(reference_df)


def test_write_pandas_to_gslib():
    df = pd.DataFrame({'X':[0,1,2,0,1,2,0,1,2], 'Y':[0,0,0,1,1,1,2,2,2], 'Z':[0, 1, 0, 1, 1, 1, 0, 1, 0]})
    gslib_file = 'tests/temp.gslib'
    pygslib.write_to_gslib(df, gslib_file)
    df_read = pygslib.read_to_pandas(gslib_file)
    os.remove(gslib_file)
    assert df.equals(df_read)
