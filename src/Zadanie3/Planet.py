class Planet:

    year_to_seconds = 31557600

    planet_times = {
        "Merkury": 0.2408467,
        "Wenus": 0.61519726,
        "Ziemia": 1,
        "Mars": 1.8808158,
        "Jowisz": 11.862615,
        "Saturn": 29.447498,
        "Uran": 84.016846,
        "Neptun": 164.79132
    }

    def count_age_on_planet(self, age_in_seconds, planet_name):

        if isinstance(age_in_seconds, int) or isinstance(age_in_seconds, float):
            if planet_name in self.planet_times:

                age_years = age_in_seconds / (self.year_to_seconds * self.planet_times[planet_name])
                return round(age_years, 2)
            else:
                raise ValueError
        else:
            raise ValueError
