from main import app

# /event/:eventId -> Event, Venue, Performer, Ticket[]
# /events/search?keyword={keyword}&start_date&end_date&page_size&page
# /<event>/book?ticketid=<id>
# /booking-confirmation?ticketid=<id>&transaction_id=<id>

@app.get('/event/{eventid}')
def get_event(eventid: str, q):
    return { 'event_id': 100 }