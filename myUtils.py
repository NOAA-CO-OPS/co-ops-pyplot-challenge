#!python3

## By Elim Thompson (07/06/2020)
##
## This script contains util functions to download and massage data for the pyPlot Challenge. 
################################################################################################

#####################################
## Import libraries
#####################################
import requests, pandas, numpy

#####################################
## Define constant
#####################################
## API template 
api_template = 'https://tidesandcurrents.noaa.gov/api/datagetter?' + \
               'begin_date={begin_date}&end_date={end_date}&station={station}&' + \
               'product={product}&datum={datum}&time_zone={time_zone}&units={units}&format=json'

def pull_data (params):

    ''' Download data from API as JSON / dictionary.

        input param
        -----------
        params (dict): Must contain keys: begin_date, end_date, station, product, datum, time_zone, and units

        output param
        ------------
        content (dict): Downloaded data from API. None if invalid API / response.
    '''

    # Fill in the template to get the actual API
    api = api_template.format (**params)
    # Get the response of the API
    response = requests.get (api)
    # If the status code of the response is anything but 200, return nothing
    if not response.status_code == 200:
        print ('Connection failed with {0}.'.format (response.status_code))
        return None
    
    # Get the content of the API as JSON
    content = response.json()
    response.close ()
    # If the content is an error message, something is wrong with the input params.
    # Print the error and return nothing.
    if 'error' in content:
        print ('Error encountered: {0}.'.format (content['error']['message']))
        return None
    # If no data is available, tell user to check the API itself and return nothing.
    if len (content) == 0:
        print ('Empty content encountered. Please check API:\n{0}.'.format (api))
        return None
    
    return content

def pull_obs (station, begin_date, end_date, datum='MLLW', time_zone='gmt', units='metric'):

    ''' Download observed water level data from API as a dictionary

        input params
        ------------
        station (str)   : station ID
        begin_date (str): begin date in yyyyMMdd, MM/dd/yyyy, yyyyMMdd HH:mm, or MM/dd/yyyy HH:mm
        end_date (str)  : begin date in yyyyMMdd, MM/dd/yyyy, yyyyMMdd HH:mm, or MM/dd/yyyy HH:mm
        datum (str)     : E.g. MSL, STND, MHW, MLLW (default), MHHW, etc
        time_zone (str) : Either GMT (default), LST, or LST_LDT
        units (str)     : Either english or metric (defaut)

        output param
        ------------
        content (dict): Requested observation data from API. None if invalid inputs / API / response
    '''

    ## Put the requested parameters in a dictionary
    params = {'begin_date':begin_date, 'end_date':end_date, 'station':station,
              'product':'water_level', 'datum':datum, 'time_zone':time_zone, 'units':units}
    ## Call pull_data to download data
    return pull_data (params)

def pull_pred (station, begin_date, end_date, datum='MLLW', time_zone='gmt', units='metric'):

    ''' Download predicted water level data from API as a dictionary

        input params
        ------------
        station (str)   : station ID
        begin_date (str): begin date in yyyyMMdd, MM/dd/yyyy, yyyyMMdd HH:mm, or MM/dd/yyyy HH:mm
        end_date (str)  : begin date in yyyyMMdd, MM/dd/yyyy, yyyyMMdd HH:mm, or MM/dd/yyyy HH:mm
        datum (str)     : E.g. MSL, STND, MHW, MLLW (default), MHHW, etc
        time_zone (str) : Either GMT (default), LST, or LST_LDT
        units (str)     : Either english or metric (defaut)

        output param
        ------------
        content (dict): Requested prediction data from API. None if invalid inputs / API / response
    '''

    ## Put the requested parameters in a dictionary
    params = {'begin_date':begin_date, 'end_date':end_date, 'station':station,
              'product':'predictions', 'datum':datum, 'time_zone':time_zone, 'units':units}
    ## Call pull_data to download data
    return pull_data (params)

def massage_data (content, doPred=False):

    ''' Massage data downloaded from API to a pandas time-series dataframe. The keys for
        prediction and observation data are different.

        input params
        ------------
        content (dict)  : Data directly downloaded from API
        doPred (boolean): If True, input content is prediction data. If False, it is observations.

        output params
        -------------
        dataframe (pandas.DataFrame): a time-series dataframe of the download data.
                                      None if input content has invalid format.
    '''

    ## Define the key based on prediction / observation data
    apiKey = 'predictions' if doPred else 'data'
    myKey  = 'predicted' if doPred else 'observed'

    # Try to interpret API content as data frame
    try:
        # Convert dict content to a dataframe
        data = numpy.array ([[aTime['t'], aTime['v']] for aTime in content[apiKey]]).T
        dataframe = pandas.DataFrame ({'datetime':data[0], myKey:data[1].astype (float)})
        # Convert dataframe to a time-series dataframe
        dataframe.index = pandas.to_datetime (dataframe.datetime)
        dataframe = dataframe.drop (axis=1, columns=['datetime'])        
    except:
        print ('Failed to interpret data')
        return None

    return dataframe