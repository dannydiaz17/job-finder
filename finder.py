import config
import pandas as p
import numpy as n
from geopy.geocoders import Nominatim


def make_df(file):
    df = p.read_csv(file, na_values=[""],
            dtype={ "Business Name" : str ,
                    "Description" : str ,
                    "Industry Code" : str ,
                    "Industry" : str ,
                    "Employees" : str ,
                    "Address" : str ,
                    "Mailing Address": str ,
                    "Distance" : float ,
                    "Phone" : str ,
                    "Key Contact" : str ,
                    "Title" : str ,
                    "Web Site" : str,
                    "Established" : int })
    return df

def get_coordinates(df):
    geolocator = Nominatim(user_agent="job-finder")
    
    for n, items in df["Address"].iterrows():
        location = geolocator.geocode(df["Address"][n])
        print(location)

def __init__():
    data = make_df(config.csv_file)
    return data
