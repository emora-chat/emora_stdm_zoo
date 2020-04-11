import spotipy as sp
import copy
from client_info import client_secret, client_id

empty_feature_dict = {
    'danceability': 0,
    'energy': 0,
    'key': 0,
    'loudness': 0,
    'mode': 0,
    'speechiness': 0,
    'acousticness': 0,
    'instrumentalness': 0,
    'liveness': 0,
    'valence': 0,
    'tempo': 0
}


class requester:

    def __init__(self):
        self.cl = sp.SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
        self.auth_token = self.cl.get_access_token()
        self.spotify = sp.Spotify(auth=self.auth_token)

    def search_for_song(self, track: str, artist: str = None):
        """
        Given a track and an artist, returns a list of track objects that
        Spotify api returns when searching for the song. Limited to size 10.
        :param track: name of the track
        :param artist: name of the artist (optional, default set to None)
        :return: List of spotify track dictionary objects
        """
        query_str = "track:" + track + " artist:" + artist
        user_q = self.spotify.search(query_str, type="track", limit=10)
        user_object = user_q['tracks']
        user_results = user_object['items']
        return user_results

    def search_for_album(self, album: str, artist: str = None):
        """
        Given an albums title and an artist, returns a list of track objects that
        Spotify api returns when searching for the song. Limited to size 10.
        :param album: name of the album
        :param artist: name of the artist (optional, default set to None)
        :return: List of spotify track dictionary objects
        """
        query_str = "album:" + album + " artist:" + artist
        user_q = self.spotify.search(query_str, type="album", limit=10)
        user_object = user_q['albums']
        user_results = user_object['items']
        return user_results

    def search_for_artist(self, artist: str):
        """
        Given an artist name or search terms for an artist,
        return a list of potential artists that the user is looking for
        :param artist: the name of the artist
        :return: a list of the artists that could match the query
        """
        query_str = "artist:" + artist
        user_q = self.spotify.search(query_str, type="artist", limit=10)
        user_object = user_q['artists']
        user_results = user_object['items']
        return user_results

    def get_song_features(self, track_id: str):
        """
        Given a song's track id, return its features
        :param track_id: the spotify id of the track
        :return: a dictionary of features for the inputted track
        """
        features_dict = copy.deepcopy(empty_feature_dict)
        track_feats = self.spotify.audio_features(track_id)[0]
        for feat in features_dict:
            features_dict[feat] = track_feats[feat]
        return track_feats

    def get_album_avg_features(self, album_id):
        """
        given an album_id, return the average of each
        quantitative feature by aggregating over all the tracks in the album
        :param album_id: the id of the album
        :return: a dictionary mapping features to their average across the album's tracks
        """
        tracks_query = self.spotify.album_tracks(album_id)
        track_list = tracks_query['items']
        features_dict = copy.deepcopy(empty_feature_dict)
        for track in track_list:
            cur_id = track['id']
            cur_feats = self.get_song_features(cur_id)
            for feat in features_dict:
                features_dict[feat] += cur_feats[feat]
        for feat in features_dict:
            features_dict[feat] /= len(track_list)
        return features_dict

    def get_artist_avg_features(self, artist_id):
        """
        aggregating over an artist's top 10 tracks, return the average features of those tracks
        :param artist_id: the id of the artist
        :return: a dictionary mapping features to their average across the artist's tracks
        """
        tracks_query = self.spotify.artist_top_tracks(artist_id)
        track_list = tracks_query['tracks']
        features_dict = copy.deepcopy(empty_feature_dict)
        for track in track_list:
            cur_id = track['id']
            cur_feats = self.get_song_features(cur_id)
            for feat in features_dict:
                features_dict[feat] += cur_feats[feat]
        for feat in features_dict:
            features_dict[feat] /= len(track_list)
        return features_dict

    def get_artist_genres(self, artist_name):
        """
        given an artist's name, return a list of genres associated with that artist
        :param artist_name: the name of the artist
        :return: list of genres associated with the artist
        """
        artist = self.search_for_artist(artist_name)[0]
        return artist['genres']  # REMEMBER, THIS IS A LIST

