import json
from collections import Counter
import urllib.request
from urllib.error import URLError, HTTPError

ORPHAN_PLANET_INDICATOR = 3


class ExoPlanet:

    def __init__(self):

        self.dataset_ = None

    """
    Fetch the dataset json file using the url in the argument
    
    Args:
        url of dataset file
    """
    def fetch_dataset(self, url):

        try:
            response = urllib.request.urlopen(url).read()
            self.dataset_ = json.loads(response.decode('utf-8'))

        except HTTPError as e:
            print("Server unable to fulfil the request" + " reason code: " + e.reason)
            exit(0)

        except URLError as e:
            print("Failed to reach the server" + " reason: " + e.reason)
            exit(0)
        
        if not self.dataset_:
            print("dataset is empty")
            exit(0)

    """
    Get list of orphan planets based on the TypeFlag indicator
    
    Returns: list of orphan planets
    """
    def get_list_of_orphan_planet_name(self):
        try:
            return [planet['PlanetIdentifier'] for planet in self.dataset_ if
                    planet['TypeFlag'] == ORPHAN_PLANET_INDICATOR]

        except Exception as e:
            print("Error occurred while returning orphan planet list, type error: " + str(e))
            return []

    """
    Get planet orbiting hottest star identified based on HostStarTempK value

    Returns: dict containing the attributes of hottest planet
    """
    def get_planet_orbiting_hottest_star(self):
        try:
            return max(self.dataset_, key=lambda planet: planet['HostStarTempK'] if isinstance(planet['HostStarTempK'],
                                                                                           int) else float('-inf'))
        except Exception as e:
            print("Error occurred while returning planet orbiting hottest star, type error: " + str(e))
            return {}

    """
    Build the timeline of the number of planets discovered per year grouped by size - small, medium, large based on
    RadiusJpt.
    
    Returns:  timeline of the number of planets discovered per year grouped by size 
    """
    def get_planet_timeline(self):

        timeline = {}

        try:
            for planet in self.dataset_:

                if isinstance(planet['RadiusJpt'], str) or isinstance(planet['DiscoveryYear'], str):
                    continue

                if planet['DiscoveryYear'] not in timeline:
                    timeline[planet['DiscoveryYear']] = Counter({'small': 0, 'medium': 0, 'large': 0})

                if 0.0 < planet['RadiusJpt'] < 1.0:
                    timeline[planet['DiscoveryYear']]['small'] += 1

                elif 1.0 < planet['RadiusJpt'] < 2.0:
                    timeline[planet['DiscoveryYear']]['medium'] += 1

                else:
                    timeline[planet['DiscoveryYear']]['large'] += 1

            return timeline

        except Exception as e:
            print("Error occurred while building planet discovery timeline, type error: " + str(e))
            return {}




