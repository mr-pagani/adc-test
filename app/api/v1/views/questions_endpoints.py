from flask import request, Blueprint, Response, json
from ..models import question_model

question = Blueprint('question', __name__, url_prefix='/api/v1')

question_object = question_model.Question()


@question.route('/questions', methods=['POST'])
def post_question():
    request_data = request.get_json()

    question_id = request_data.get("question_id")
    createdOn = request_data.get("createdOn")
    createdBy = request_data.get("createdBy")
    meetup = request_data.get("meetup")
    title = request_data.get("title")
    body = request_data.get("body")
    votes = request_data.get("votes")

    resp = json.dumps(question_object.create_question(
        question_id, createdOn, createdBy, meetup, title, body, votes))

    x = json.loads(resp)
    if x['status'] == 404:
        return Response(resp, 404, mimetype='application/json')
    else:
        return Response(resp, 200, mimetype='application/json')


@question.route('/questions/<question_id>/upvote', methods=['PATCH'])
def upvote(question_id):
    resp = question_object.upvote(question_id)
    response = Response(json.dumps(resp), 200, mimetype='application/json')
    return response


@question.route('/questions/<question_id>/downvote', methods=['PATCH'])
def downvote(question_id):
    response = Response("", 204)
    response.headers['Location'] = "/questions/" + str(question_id)
    return response


@question.route('/questions/<question_id>')
def get_question_by_id(question_id):
    qstn = json.dumps(question_object.get_question(question_id))

    x = json.loads(qstn)
    if x['status'] == 404:
        return Response(qstn, 404, mimetype='application/json')
    else:
        return Response(qstn, 200, mimetype='application/json')


@question.route('/questions')
def get_questions():
    questions = json.dumps(question_object.view_questions())

    x = json.loads(questions)
    if x['status'] == 404:
        return Response(questions, 404, mimetype='application/json')
    else:
        return Response(questions, 200, mimetype='application/json')


@question.route('/questions/<question_id>', methods=['DELETE'])
def del_question(question_id):
    resp = json.dumps(question_object.delete_question(question_id))

    x = json.loads(resp)
    if x['status'] == 404:
        return Response(resp, 404, mimetype='application/json')
    else:
        return Response(resp, 200, mimetype='application/json')
