config = {
    sources : {
        'noaa' : 'https://www.weather.gov/nwr/station_search',
        'amfm' : 'https://radio-locator.com/',
        'sw' : 'https://short-wave.info/index.php'
    }
}
import requests
import pandas as pd
from bs4 import BeautifulSoup
import great_circle_calculator.great_circle_calculator as gcc

def coordinate_results(lat, lon):
    '''
    Processes the latitude and longitude and returns the radio station results

    Parameters
    ----------
    lat float
        The decimal degrees with WGS 84 projection representing the latitude
    lon float
        The decimal degrees with WGS 84 projection representing the longitude

    Returns
    -------
    '''
    return None

def distance(lat, lon, stations):
    '''
    Parameters
    ----------
    lat float
        The decimal degrees with WGS 84 projection representing the latitude
    lon float
        The decimal degrees with WGS 84 projection representing the longitude
    stations list of tuples (lat, lon)
        A list of the stations to calculate distance from the input lat, lon
    '''
    return [gcc.distance_between_points((lon, lat), (station[1], station[0])) for station in stations]