from geopy.geocoders import Nominatim

def get_location_data(address):
    geolocator = Nominatim(user_agent="django_geolocation")
    location = geolocator.geocode(address)
    return location
