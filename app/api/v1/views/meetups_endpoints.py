from flask import request, Blueprint, Response, json
from ..models import meetup_model

meetup = Blueprint('meetup', __name__, url_prefix='/api/v1')

meetup_object = meetup_model.Meetup()
rsvp_object = meetup_model.Rsvp()


@meetup.route('/meetups', methods=['POST'])
def post_meet():
    request_data = request.get_json()

    meetup_id = request_data.get("meetup_id")
    createdOn = request_data.get("createdOn")
    location = request_data.get("location")
    images = request_data.get("images")
    topic = request_data.get("topic")
    happeningOn = request_data.get("happeningOn")
    tags = request_data.get("tags")

    resp = json.dumps(meetup_object.create_meetup(
        meetup_id, createdOn, location, images, topic, happeningOn, tags))

    x = json.loads(resp)
    if x['status'] == 201:
        response = Response(resp, 201, mimetype='application/json')
        return response


@meetup.route('/meetups')
def view_meets():
    meetups = json.dumps(meetup_object.view_meetups())
    x = json.loads(meetups)
    if x['status'] == 404:
        return Response(meetups, 404, mimetype='application/json')
    else:
        return Response(meetups, 200, mimetype='application/json')


@meetup.route('/meetups/upcoming')
def view_upcoming():
    up_meets = json.dumps(meetup_object.get_upcoming())

    x = json.loads(up_meets)
    if x['status'] == 404:
        return Response(up_meets, 404, mimetype='application/json')
    else:
        return Response(up_meets, 200, mimetype='application/json')


@meetup.route('/meetups/<meetup_id>')
def view_meet(meetup_id):
    meet = json.dumps(meetup_object.get_meetup(meetup_id))
    x = json.loads(meet)
    if x['status'] == 404:
        return Response(meet, 404, mimetype='application/json')
    else:
        return Response(meet, 200, mimetype='application/json')


@meetup.route('/meetups/<meetup_id>', methods=['DELETE'])
def del_meet(meetup_id):
    resp = meetup_object.delete_meetup(meetup_id)
    response = Response(json.dumps(resp), 200, mimetype='application/json')
    return response


@meetup.route('/meetups/<meetup_id>/rsvps', methods=['POST'])
def rsvp_meet(meetup_id):
    request_data = request.get_json()

    rsvp_id = request_data.get("rsvp_id")
    meetup_id = request_data.get("meetup_id")
    user_id = request_data.get("user_id")
    response = request_data.get("response")

    resp = rsvp_object.create_rsvp(
        rsvp_id, meetup_id, user_id, response)

    response = Response(json.dumps(resp), 201, mimetype='application/json')
    return response
