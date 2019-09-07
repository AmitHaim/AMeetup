from eventbrite import Eventbrite
from src import config

eventbrite = Eventbrite(config.api_key)
events = eventbrite.get('/events/search?location.address=vancovuer&location.within=10km&expand=venue')
print(events)
