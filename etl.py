config = {
    'sources' : {
        'noaa' : 'https://www.weather.gov/nwr/station_search',
        'amfm' : 'https://radio-locator.com/',
        'sw' : 'https://short-wave.info/index.php'
    }
}
import requests
import re
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

def parse_noaa_stations():
    response = requests.get(config['sources']['noaa'])
    response.raise_for_status()  # Ensure we notice bad responses

    # Extract the JavaScript data
    data = response.text

    # Regular expressions to capture the data arrays
    callsign_pattern = re.compile(r'STATIONCALLSIGN\[(\d+)\] = "(.*?)";')
    state_pattern = re.compile(r'SITESTATE\[(\d+)\] = "(.*?)";')
    sitename_pattern = re.compile(r'SITENAME\[(\d+)\] = "(.*?)";')
    lat_pattern = re.compile(r'TOWERLAT\[(\d+)\] = "(.*?)";')
    latd_pattern = re.compile(r'TLATD\[(\d+)\] = "(.*?)";')
    long_pattern = re.compile(r'TOWERLONG\[(\d+)\] = "(.*?)";')
    longd_pattern = re.compile(r'TLONGD\[(\d+)\] = "(.*?)";')

    # Initialize lists to store extracted data
    stations = []

    # Extract and store the data
    callsigns = callsign_pattern.findall(data)
    states = state_pattern.findall(data)
    sitenames = sitename_pattern.findall(data)
    lats = lat_pattern.findall(data)
    latds = latd_pattern.findall(data)
    longs = long_pattern.findall(data)
    longds = longd_pattern.findall(data)

    # Combine data into station dictionaries
    for i in range(len(callsigns)):
        station = {
            'Callsign': callsigns[i][1],
            'State': states[i][1],
            'Site Name': sitenames[i][1],
            'Latitude': lats[i][1],
            'Latitude Decimal': latds[i][1],
            'Longitude': longs[i][1],
            'Longitude Decimal': longds[i][1],
        }
        stations.append(station)

    return stations