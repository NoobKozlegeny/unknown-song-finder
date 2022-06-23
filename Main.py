import importlib
from Auth import AuthClientCredentials, AuthCode
from SpotifyRecommendation import SpotifyRecommendation
from SpotifySongGatherer import SpotifySongGatherer


def main():
    ssg = SpotifySongGatherer(AuthClientCredentials)
    sr = SpotifyRecommendation(AuthCode)
    
    sr.GetRecommendations()
    ssg.BeginTrackSearchAndUploading(genresToAvoid=[
        'ambient', 'bluegrass', 'bossanova', 'children', 'country', 'gospel',
        'indian', 'iranian', 'kids', 'malay', 'mandopop', 'mpb', 'opera', 'pagode',
        'philippines-opm', 'rainy-day', 'sertanejo', 'sleep', 'study', 'turkish'
        ])
        
        
if __name__ == '__main__':
    main()