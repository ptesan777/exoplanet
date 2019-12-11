from src.exoplanet import ExoPlanet

"""
Entry point for app that downloads a catalog of exoplanet data and displays the following information:

1. The number of orphan planets (no star).
2. The name (planet identifier) of the planet orbiting the hottest star.
3. A timeline of the number of planets discovered per year grouped by size. Use the following groups: “small” is 
less than 1 Jupiter radii, “medium” is less than 2 Jupiter radii, and anything bigger is considered “large”. 
For example, in 2004 we discovered 2 small planets, 5 medium planets, and 0 large planets.
"""

if __name__ == "__main__":

    URL = "https://gist.githubusercontent.com/joelbirchler/66cf8045fcbb6515557347c05d789b4a/raw/9a196385b44d4288431eef74896c0512bad3defe/exoplanets"

    ep = ExoPlanet()

    ep.fetch_dataset(URL)

    orphan_planets = ep.get_list_of_orphan_planet_name()
    if orphan_planets:
        print("Orphan planet(s): ", ', '.join(map(str, orphan_planets)))
    else:
        print("No orphan planets found in the dataset or data unavailable")

    hottest_planet = ep.get_hottest_planet()
    if hottest_planet:
        print("Hottest planet: " + hottest_planet['PlanetIdentifier'])
    else:
        print("Planet temperature data is unavailable")

    timeline = ep.get_planet_timeline()

    if timeline:

        for year, size_count in sorted(timeline.items(), key=lambda item: item[0]):
            print("Planets discovered in {}".format(year), end=" - ")

            for size, count in size_count.items():
                print("{} {}".format(size, count), end=" ")
            print('\n')
    else:
        print("Timeline data is unavailable")








