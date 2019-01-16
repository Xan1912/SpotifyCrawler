import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials
import scrapy



class SpotifyCrawler(scrapy.Spider):
    
    name = "spotispy"
    
    def parse(self, response):
        # Authenticating the API with the required credentials 
        client_credentials_manager = SpotifyClientCredentials(client_id='b7cf2f5f0e074d1ca984a546822797cc',
                                    client_secret='c435b02f49304b7db74ec08ddb7df6e7')
        spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

        # Get the data
        data = spotify.new_releases(country='DE', limit=20, offset=0)
        yield(data)
    
        

