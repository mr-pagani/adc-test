
QUESTION_LIST = []


class Question():
    def create_question(
                        self, question_id, createdOn, createdBy, meetup, title,
                        body, votes):
        self.single_query = {}
        self.single_query['question_id'] = question_id
        self.single_query['createdOn'] = createdOn
        self.single_query['createdBy'] = createdBy
        self.single_query['meetup'] = meetup
        self.single_query['title'] = title
        self.single_query['body'] = body
        self.single_query['votes'] = votes

        QUESTION_LIST.append(self.single_query)

        return {"status": 201,
                "data": self.single_query
                }

    def view_questions(self):
        if len(QUESTION_LIST) == 0:
            return {"status": 404,
                    "message": "questions not found"
                    }

        else:
            return {
                    "status": 200,
                    "data": QUESTION_LIST
                        }

    def get_question(self, question_id):
        question_item = [question for question in QUESTION_LIST if question["question_id"] == question_id]
        if question_item:

                res = {"status": 200,
                       "data": question_item
                        }
        else:
                res = {"status": 404,
                       "error": "Question with the given id not found"}

        return res

    def upvote(self, question_id):
        for question in QUESTION_LIST:
            if question["question_id"] == question_id:
                question["votes"] = question["votes"] + 1
            return question

    def downvote(self, question_id):
        for question in QUESTION_LIST:
            if question["question_id"] == question_id:
                question["votes"] -= 1
                QUESTION_LIST.update(question)

    def delete_question(self, question_id):
        for question in QUESTION_LIST:
            if question["question_id"] == question_id:
                QUESTION_LIST.remove(question)
                return {"status": 204,
                        "Message": "Question successfuly deleted"
                        }
            else:
                return {"status": 404,
                        "error": "Question with the id provided was not found"
                        }
