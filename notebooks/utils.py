import os.path
import urllib
import pandas as pd

def load_channel_data(site_id, channel_id):
    series_id = '%d-%d' % (site_id, channel_id)
    file_path = '../dataset/channels-7879-site/channels-%s.csv' % series_id
    if os.path.isfile(file_path):
        df = pd.read_csv(file_path, parse_dates=['time'])
    else:
        url = "http://13.77.168.238/data/channel/%s/data" % series_id
        df = pd.read_csv(url, parse_dates=['time'])
        df.to_csv(file_path, index=False)
    return df.set_index('time')['value']


def get_channel_id(site_channels, name):
    ids = site_channels[site_channels['channelName'] == name]['channelId']    
    return ids.iloc[0]
