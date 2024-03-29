from Others.Exceptions.CustomExceptions import NotFoundError
from SpotifyScripts.Auth import AuthCode
from SpotifyScripts.SpotifyRecommendation import SpotifyRecommendation
import pytest

class TestSpotifyRecommendation():
    
    def test_get_item_ids(self):
        # ARRANGE
        sr = SpotifyRecommendation(AuthCode())
        data = {"tracks":[{"album":{"album_type":"SINGLE","artists":[{"external_urls":{"spotify":"https://open.spotify.com/artist/7CSdLmKke7VFyb0ZJfl3W1"},"href":"https://api.spotify.com/v1/artists/7CSdLmKke7VFyb0ZJfl3W1","id":"7CSdLmKke7VFyb0ZJfl3W1","name":"Heiakim","type":"artist","uri":"spotify:artist:7CSdLmKke7VFyb0ZJfl3W1"}],"external_urls":{"spotify":"https://open.spotify.com/album/6UVLrRj8uNRDAuCcMlOHkn"},"href":"https://api.spotify.com/v1/albums/6UVLrRj8uNRDAuCcMlOHkn","id":"6UVLrRj8uNRDAuCcMlOHkn","images":[{"height":640,"url":"https://i.scdn.co/image/ab67616d0000b2737aa8ec7181ddfec2c043ad24","width":640},{"height":300,"url":"https://i.scdn.co/image/ab67616d00001e027aa8ec7181ddfec2c043ad24","width":300},{"height":64,"url":"https://i.scdn.co/image/ab67616d000048517aa8ec7181ddfec2c043ad24","width":64}],"name":"super idol but it's chill","release_date":"2021-12-16","release_date_precision":"day","total_tracks":1,"type":"album","uri":"spotify:album:6UVLrRj8uNRDAuCcMlOHkn"},"artists":[{"external_urls":{"spotify":"https://open.spotify.com/artist/7CSdLmKke7VFyb0ZJfl3W1"},"href":"https://api.spotify.com/v1/artists/7CSdLmKke7VFyb0ZJfl3W1","id":"7CSdLmKke7VFyb0ZJfl3W1","name":"Heiakim","type":"artist","uri":"spotify:artist:7CSdLmKke7VFyb0ZJfl3W1"}],"disc_number":1,"duration_ms":112258,"explicit":"false","external_ids":{"isrc":"QZTAS2169062"},"external_urls":{"spotify":"https://open.spotify.com/track/0Y1eh3hzT4700xANxvv1zT"},"href":"https://api.spotify.com/v1/tracks/0Y1eh3hzT4700xANxvv1zT","id":"0Y1eh3hzT4700xANxvv1zT","is_local":"false","is_playable":"true","name":"super idol but it's chill","popularity":53,"preview_url":"https://p.scdn.co/mp3-preview/336fbab4dc3fb58b55f629ced30113cbc0673e54?cid=774b29d4f13844c495f206cafdad9c86","track_number":1,"type":"track","uri":"spotify:track:0Y1eh3hzT4700xANxvv1zT"},{"album":{"album_type":"ALBUM","artists":[{"external_urls":{"spotify":"https://open.spotify.com/artist/3rfgbfpPSfXY40lzRK7Syt"},"href":"https://api.spotify.com/v1/artists/3rfgbfpPSfXY40lzRK7Syt","id":"3rfgbfpPSfXY40lzRK7Syt","name":"Barry White","type":"artist","uri":"spotify:artist:3rfgbfpPSfXY40lzRK7Syt"}],"external_urls":{"spotify":"https://open.spotify.com/album/42Si9RbdXYGWQsfNTzjlnG"},"href":"https://api.spotify.com/v1/albums/42Si9RbdXYGWQsfNTzjlnG","id":"42Si9RbdXYGWQsfNTzjlnG","images":[{"height":640,"url":"https://i.scdn.co/image/ab67616d0000b273aa3252b7843a8a3426cc34bf","width":640},{"height":300,"url":"https://i.scdn.co/image/ab67616d00001e02aa3252b7843a8a3426cc34bf","width":300},{"height":64,"url":"https://i.scdn.co/image/ab67616d00004851aa3252b7843a8a3426cc34bf","width":64}],"name":"Can't Get Enough","release_date":"1974-02-15","release_date_precision":"day","total_tracks":7,"type":"album","uri":"spotify:album:42Si9RbdXYGWQsfNTzjlnG"},"artists":[{"external_urls":{"spotify":"https://open.spotify.com/artist/3rfgbfpPSfXY40lzRK7Syt"},"href":"https://api.spotify.com/v1/artists/3rfgbfpPSfXY40lzRK7Syt","id":"3rfgbfpPSfXY40lzRK7Syt","name":"Barry White","type":"artist","uri":"spotify:artist:3rfgbfpPSfXY40lzRK7Syt"}],"disc_number":1,"duration_ms":274000,"explicit":"false","external_ids":{"isrc":"USPR37407059"},"external_urls":{"spotify":"https://open.spotify.com/track/3mWpUEBYnv9SIFWfixSJFx"},"href":"https://api.spotify.com/v1/tracks/3mWpUEBYnv9SIFWfixSJFx","id":"3mWpUEBYnv9SIFWfixSJFx","is_local":"false","is_playable":"true","name":"Can't Get Enough Of Your Love, Babe","popularity":68,"preview_url":"null","track_number":4,"type":"track","uri":"spotify:track:3mWpUEBYnv9SIFWfixSJFx"},{"album":{"album_type":"ALBUM","artists":[{"external_urls":{"spotify":"https://open.spotify.com/artist/4VnomLtKTm9Ahe1tZfmZju"},"href":"https://api.spotify.com/v1/artists/4VnomLtKTm9Ahe1tZfmZju","id":"4VnomLtKTm9Ahe1tZfmZju","name":"Jackie Wilson","type":"artist","uri":"spotify:artist:4VnomLtKTm9Ahe1tZfmZju"}],"external_urls":{"spotify":"https://open.spotify.com/album/4OgYmImCWz3VK7At9GTWHN"},"href":"https://api.spotify.com/v1/albums/4OgYmImCWz3VK7At9GTWHN","id":"4OgYmImCWz3VK7At9GTWHN","images":[{"height":640,"url":"https://i.scdn.co/image/ab67616d0000b273e7ba7ec8dbf10a6db596cfe7","width":640},{"height":300,"url":"https://i.scdn.co/image/ab67616d00001e02e7ba7ec8dbf10a6db596cfe7","width":300},{"height":64,"url":"https://i.scdn.co/image/ab67616d00004851e7ba7ec8dbf10a6db596cfe7","width":64}],"name":"Higher And Higher","release_date":"1967","release_date_precision":"year","total_tracks":11,"type":"album","uri":"spotify:album:4OgYmImCWz3VK7At9GTWHN"},"artists":[{"external_urls":{"spotify":"https://open.spotify.com/artist/4VnomLtKTm9Ahe1tZfmZju"},"href":"https://api.spotify.com/v1/artists/4VnomLtKTm9Ahe1tZfmZju","id":"4VnomLtKTm9Ahe1tZfmZju","name":"Jackie Wilson","type":"artist","uri":"spotify:artist:4VnomLtKTm9Ahe1tZfmZju"}],"disc_number":1,"duration_ms":179120,"explicit":"false","external_ids":{"isrc":"USBWC0010022"},"external_urls":{"spotify":"https://open.spotify.com/track/5qyq1H5OPMlfuvZQ1wQNo7"},"href":"https://api.spotify.com/v1/tracks/5qyq1H5OPMlfuvZQ1wQNo7","id":"5qyq1H5OPMlfuvZQ1wQNo7","is_local":"false","is_playable":"true","name":"(Your Love Keeps Lifting Me) Higher & Higher","popularity":72,"preview_url":"https://p.scdn.co/mp3-preview/810e1a98f0c67622b1d0faf6c0ff071551f15650?cid=774b29d4f13844c495f206cafdad9c86","track_number":1,"type":"track","uri":"spotify:track:5qyq1H5OPMlfuvZQ1wQNo7"}],"seeds":[{"initialPoolSize":259,"afterFilteringSize":259,"afterRelinkingSize":259,"id":"172zA5Yn0YzayQWvEJuGAm","type":"TRACK","href":"https://api.spotify.com/v1/tracks/172zA5Yn0YzayQWvEJuGAm"},{"initialPoolSize":280,"afterFilteringSize":280,"afterRelinkingSize":280,"id":"4Cv6ongCvJy9JfSkWVnb5D","type":"TRACK","href":"https://api.spotify.com/v1/tracks/4Cv6ongCvJy9JfSkWVnb5D"}]}
        # ACT
        recommendedTrackIDs = sr.GetItemIDs(data)
        expected = [ '0Y1eh3hzT4700xANxvv1zT', '3mWpUEBYnv9SIFWfixSJFx', '5qyq1H5OPMlfuvZQ1wQNo7' ]
        # ASSERT
        assert expected == recommendedTrackIDs
        
    def test_filter_items(self):
        # ARRANGE
        sr = SpotifyRecommendation(AuthCode())
        data = [{'album': {'album_type': 'compilation', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/6J7biCazzYhU3gM9j1wfid'}, 'href': 'https://api.spotify.com/v1/artists/6J7biCazzYhU3gM9j1wfid', 'id': '6J7biCazzYhU3gM9j1wfid', 'name': 'Jamiroquai', 'type': 'artist', 'uri': 'spotify:artist:6J7biCazzYhU3gM9j1wfid'}], 'external_urls': {'spotify': 'https://open.spotify.com/album/290mciLlwjKmpNgv95xTSO'}, 'href': 'https://api.spotify.com/v1/albums/290mciLlwjKmpNgv95xTSO', 'id': '290mciLlwjKmpNgv95xTSO', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b273a74a5b6bd1da601e629cf58f', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e02a74a5b6bd1da601e629cf58f', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d00004851a74a5b6bd1da601e629cf58f', 'width': 64}], 'name': 'High Times: Singles 1992-2006', 'release_date': '2006-11-06', 'release_date_precision': 'day', 'total_tracks': 32, 'type': 'album', 'uri': 'spotify:album:290mciLlwjKmpNgv95xTSO'}, 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/6J7biCazzYhU3gM9j1wfid'}, 'href': 'https://api.spotify.com/v1/artists/6J7biCazzYhU3gM9j1wfid', 'id': '6J7biCazzYhU3gM9j1wfid', 'name': 'Jamiroquai', 'type': 'artist', 'uri': 'spotify:artist:6J7biCazzYhU3gM9j1wfid'}], 'disc_number': 1, 'duration_ms': 229360, 'explicit': False, 'external_ids': {'isrc': 'GBARL0601475'}, 'external_urls': {'spotify': 'https://open.spotify.com/track/49TQfrsm60j5ZFKS59JOdU'}, 'href': 'https://api.spotify.com/v1/tracks/49TQfrsm60j5ZFKS59JOdU', 'id': '49TQfrsm60j5ZFKS59JOdU', 'is_local': False, 'name': 'Virtual Insanity - Remastered', 'popularity': 70, 'preview_url': 'https://p.scdn.co/mp3-preview/61558874610716ab166a5509d9b9abf9a0c18efc?cid=cbef85907193457e978b1fe28885af1d', 'track_number': 6, 'type': 'track', 'uri': 'spotify:track:49TQfrsm60j5ZFKS59JOdU'},
                {'album': {'album_type': 'album', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/7dgrSH4XufRw3FlLYBMlgg'}, 'href': 'https://api.spotify.com/v1/artists/7dgrSH4XufRw3FlLYBMlgg', 'id': '7dgrSH4XufRw3FlLYBMlgg', 'name': 'Hip Hop Boyz', 'type': 'artist', 'uri': 'spotify:artist:7dgrSH4XufRw3FlLYBMlgg'}], 'external_urls': {'spotify': 'https://open.spotify.com/album/6jgMicPnvIcBNspJlgXQ5I'}, 'href': 'https://api.spotify.com/v1/albums/6jgMicPnvIcBNspJlgXQ5I', 'id': '6jgMicPnvIcBNspJlgXQ5I', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b273a01638126d9cc7527fe0fe55', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e02a01638126d9cc7527fe0fe55', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d00004851a01638126d9cc7527fe0fe55', 'width': 64}], 'name': 'Hip Hop Boys', 'release_date': '2022-07-07', 'release_date_precision': 'day', 'total_tracks': 50, 'type': 'album', 'uri': 'spotify:album:6jgMicPnvIcBNspJlgXQ5I'}, 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/7dgrSH4XufRw3FlLYBMlgg'}, 'href': 'https://api.spotify.com/v1/artists/7dgrSH4XufRw3FlLYBMlgg', 'id': '7dgrSH4XufRw3FlLYBMlgg', 'name': 'Hip Hop Boyz', 'type': 'artist', 'uri': 'spotify:artist:7dgrSH4XufRw3FlLYBMlgg'}], 'disc_number': 1, 'duration_ms': 121343, 'explicit': False, 'external_ids': {'isrc': 'GBPS84215838'}, 'external_urls': {'spotify': 'https://open.spotify.com/track/5hHKG1rIOkQcAFh0zFwU4e'}, 'href': 'https://api.spotify.com/v1/tracks/5hHKG1rIOkQcAFh0zFwU4e', 'id': '5hHKG1rIOkQcAFh0zFwU4e', 'is_local': False, 'name': 'Rising Virtual', 'popularity': 0, 'preview_url': 'https://p.scdn.co/mp3-preview/b7bfd8ebd9b611d688a14f337ae8faf59b366f08?cid=cbef85907193457e978b1fe28885af1d', 'track_number': 30, 'type': 'track', 'uri': 'spotify:track:5hHKG1rIOkQcAFh0zFwU4e'},
                {'album': {'album_type': 'single', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/7jbG8tDQ5FmqBbTCj5dJdy'}, 'href': 'https://api.spotify.com/v1/artists/7jbG8tDQ5FmqBbTCj5dJdy', 'id': '7jbG8tDQ5FmqBbTCj5dJdy', 'name': 'DG IMMORTALS', 'type': 'artist', 'uri': 'spotify:artist:7jbG8tDQ5FmqBbTCj5dJdy'}], 'external_urls': {'spotify': 'https://open.spotify.com/album/0nP1th7BVoMH1SOIffpdLT'}, 'href': 'https://api.spotify.com/v1/albums/0nP1th7BVoMH1SOIffpdLT', 'id': '0nP1th7BVoMH1SOIffpdLT', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b2731039c4c3ba2bcf181204c681', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e021039c4c3ba2bcf181204c681', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d000048511039c4c3ba2bcf181204c681', 'width': 64}], 'name': 'SYSTEM PAAD DENGE (DG x VIRTUAL_AF)', 'release_date': '2022-01-09', 'release_date_precision': 'day', 'total_tracks': 1, 'type': 'album', 'uri': 'spotify:album:0nP1th7BVoMH1SOIffpdLT'}, 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/7jbG8tDQ5FmqBbTCj5dJdy'}, 'href': 'https://api.spotify.com/v1/artists/7jbG8tDQ5FmqBbTCj5dJdy', 'id': '7jbG8tDQ5FmqBbTCj5dJdy', 'name': 'DG IMMORTALS', 'type': 'artist', 'uri': 'spotify:artist:7jbG8tDQ5FmqBbTCj5dJdy'}], 'disc_number': 1, 'duration_ms': 215873, 'explicit': True, 'external_ids': {'isrc': 'QZFYZ2233297'}, 'external_urls': {'spotify': 'https://open.spotify.com/track/70779of31cXSQatSdmWr0Z'}, 'href': 'https://api.spotify.com/v1/tracks/70779of31cXSQatSdmWr0Z', 'id': '70779of31cXSQatSdmWr0Z', 'is_local': False, 'name': 'SYSTEM PAAD DENGE (DG x VIRTUAL_AF)', 'popularity': 35, 'preview_url': 'https://p.scdn.co/mp3-preview/b85faeb46f3d5ba6b8ca0977f51f3b93f0a51652?cid=cbef85907193457e978b1fe28885af1d', 'track_number': 1, 'type': 'track', 'uri': 'spotify:track:70779of31cXSQatSdmWr0Z'}]
        # ACT
        sr.FilterItems(items=data, filter='virtual')
        # ASSERT
        assert len(data) == 1
    
    def test_does_genre_exist_success(self):
        # ARRANGE
        sr = SpotifyRecommendation(AuthCode())
        # ACT
        result = sr.DoesGenreExists(genre='edm')
        expected = "edm have been successfully found.\n"
        # ASSERT
        assert result == expected       
        
    def test_does_genre_exist_fail(self):
        # ARRANGE
        sr = SpotifyRecommendation(AuthCode())
        # ACT
        # ASSERT
        with pytest.raises(NotFoundError):
            sr.DoesGenreExists(genre='FortniteAmogUsSussyBaka')
            
    def test_does_genre_exist_input_is_blank(self):
        # ARRANGE
        sr = SpotifyRecommendation(AuthCode())
        # ACT
        result = sr.DoesGenreExists(genre='')
        expected = "You have decided to leave this blank."
        # ASSERT
        assert result == expected 
    
    def test_does_item_exists_found_track(self):
        # ARRANGE
        sr = SpotifyRecommendation(AuthCode())
        # ACT
        # Emulates the pubsub messaging part where the user selects the correct track
        sr.selectedTrackID = '6BOOnwbQFco9AV0rKXZ8VV'
        
        output, itemID = sr.DoesItemExists(item='Cello Suite No. 1 in G Major, BWV 1007: I. Prélude',type='track')
        # ASSERT
        assert f"Cello Suite No. 1 in G Major, BWV 1007: I. Prélude track have been successfully found.\n" == output
        
    def test_does_item_exists_didnt_found_track(self):
        # ARRANGE
        sr = SpotifyRecommendation(AuthCode())
        # ACT
        # Emulates the pubsub messaging part where the user selects the correct track (It should be left as None)
        sr.selectedTrackID = None
        
        # ASSERT
        with pytest.raises(NotFoundError):
            output, itemID = sr.DoesItemExists(item='BringBackFilthyFrankIMissYou',type='track')
            
    def test_does_item_exists_input_is_blank(self):
        # ARRANGE
        sr = SpotifyRecommendation(AuthCode())
        # ACT
        output, itemID = sr.DoesItemExists(item='',type='track')
        expected = "You have decided to leave this blank."
        # ASSERT
        assert expected == output
            