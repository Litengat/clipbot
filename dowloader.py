import requests, shutil

CLIENT_ID = '16oc7xr1rpnlocioot73wq6epos70l'
ACCESS_TOKEN = '6bsrf4plbxxiaxqq1lfcd81xrxvs2n'
CLIENT_SECRET = 'l15cragd310ucondtoczpranvf4wid'




def download_clip(url):
    clip_info = get_info(url)
    video_id = clip_info['data'][0]['id']
    clip_url = clip_info['data'][0]['thumbnail_url']
    url_to_download = clip_url.split('-preview', 1)[0] + '.mp4'
    print('Downloading clip... ', end='')
    try:
        with requests.get(url_to_download, stream=True) as response:
            with open(f'clip.mp4', 'wb') as file:
                shutil.copyfileobj(response.raw, file)
        print('Download success!')
    except Exception as error:
        print(error)
        pass

def get_info(url):
    try:
        clip_id = url.split('/')[-1]
        url = 'https://api.twitch.tv/helix/clips?id=' + clip_id
        headers = {
            'Client-ID':CLIENT_ID,
            'Authorization':f'Bearer {ACCESS_TOKEN}',
            "Accept":"application/vnd.twitchtv.v5+json"
        }
        r = requests.get(url, headers=headers)
        return r.json()
    except Exception as error:
        print(error)
        exit()

def get_new_access_token():
    try:
        url = "https://id.twitch.tv/oauth2/token"
    except Exception as error:
        print(error)
        exit()
    payload = {"client_id": CLIENT_ID, "client_secret": CLIENT_SECRET, "grant_type": "client_credentials"}
    headers = {'Client-ID': CLIENT_ID}
    resp = requests.post(url, params=payload, headers=headers)
    return resp.json()['access_token']

