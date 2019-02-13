import pandas as pd
import pygslib

def test_read_gslib_to_pandas():
    df = pygslib.read_to_pandas('tests/jura_sample.dat')
    reference_df = pd.read_table('tests/jura_sample.dat', skiprows=13, names=['Xloc','Yloc','Landuse','Rock','Cd','Co','Cr','Cu','Ni','Pb','Zn'], delim_whitespace=True)
    assert df.equals(reference_df)
