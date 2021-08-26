from app import app
from flask import render_template, request
from models.event_list import events, add_event
from models.event import Event


@app.route('/events')
def index():
    return render_template('index.html', title='Home', events=events)

@app.route('/events', methods=['POST'])
def add_new_event():
    print(request.form)
    event_date = request.form['date']
    event_name = request.form['name']
    event_num_of_guests = request.form['num_of_guests']
    event_location = request.form['location']
    event_description = request.form['description']

    if request.form['recurring'] == 'y':
        event_recurring = True
    elif request.form['recurring'] == 'n':
        event_recurring = False

    new_event = Event(event_date, event_name, event_num_of_guests, event_location, event_description, event_recurring)
    add_event(new_event)
    return render_template('index.html', title='Home', events=events)





