from models.event import Event

event_1 = Event("22/07/2022","Kenny's birthday party", 8, "Edinburgh","Kenny turns 32", True )
event_2 = Event("27/07/2022","Dinner at fancy restaurant", 4, "Glasgow","Family in town", False )

events = [event_1, event_2]

def add_event(event):
    events.append(event)

def delete_event(event):
    events.remove(event)