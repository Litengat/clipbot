import requests
import json
import datetime

client_id = '16oc7xr1rpnlocioot73wq6epos70l'
client_secret = 'l15cragd310ucondtoczpranvf4wid'
streamer_name = '50985620'


r = requests.post('https://id.twitch.tv/oauth2/token', {
    'client_id': client_id,
    'client_secret': client_secret,
    "grant_type": 'client_credentials'
})

#data output
keys = r.json()

headers = {
    'Client-ID': client_id,
    'Authorization': 'Bearer ' + keys['access_token']
}


def convert_to_RFC_datetime(year=1900, month=1, day=1, hour=0, minute=0):
    dt = datetime.datetime(year, month, day, hour, minute, 0).isoformat() + 'Z'
    return dt

def get_Clips():
    
    current_time = datetime.datetime.now()
    date = convert_to_RFC_datetime(year=current_time.year,month=current_time.month,day=current_time.day,hour=0, minute=1)
    stream = requests.get("https://api.twitch.tv/helix/clips?broadcaster_id="+ streamer_name + "&started_at=" + date + "&first=100", headers=headers)
    stream_data = stream.json()
    # Serializing json
    json_object = json.dumps(stream_data, indent=4)

    # Writing to sample.json
    with open("sample.json", "w") as outfile:
        outfile.write(json_object)

    return stream_data



streamdata = get_Clips()

# Serializing json
json_object = json.dumps(streamdata, indent=4)
 
# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)

def get_Clips_Urs():
    urls = []

    for i in range(len(streamdata['data'])):
        urls.append(streamdata['data'][i]['url'])

    return urls
