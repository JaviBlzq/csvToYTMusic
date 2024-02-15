# csvToYTMusic

In this project, I want to trasnfer my own Spotify playlist to my Youtube Account, using the Youtube API v3.

## Installation

For installation, clone the repo and run:

`python3 main.py`

Ensure to:

- Have a **data** directory where the _.csv_ and the _.json_.
- Run `pip install -r requirements.txt`

## Usage
Be sure to make a public project in [Google Cloud APIS](https://console.cloud.google.com/apis/dashboard)

Once you have it, download the _OAuth2.0_ JSON, and save it in **data**.

I highly recommend using [Tune My Music](https://www.tunemymusic.com/es/transfer/spotify-to-file) to get the _.csv_.

Due to quota restrictions in APIs, the maximum transfer are 66 songs per day using one project in [Google Cloud APIS](https://console.cloud.google.com/apis/dashboard).

