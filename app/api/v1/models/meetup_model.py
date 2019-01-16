from datetime import datetime


MEETUP_LIST = []

RSVP_LIST = []


class Meetup():
    def create_meetup(self, meetup_id, createdOn, location, images, topic,
                      happeningOn, tags):
        self.single_meet = {}

        self.single_meet['meetup_id'] = meetup_id
        self.single_meet['createdOn'] = createdOn
        self.single_meet['location'] = location
        self.single_meet['images'] = images
        self.single_meet['topic'] = topic
        self.single_meet['happeningOn'] = happeningOn
        self.single_meet['tags'] = tags

        MEETUP_LIST.append(self.single_meet)
        return {"status": 201,
                "data": self.single_meet
                }

    def view_meetups(self):
        if len(MEETUP_LIST) == 0:

            return {"status": 404,
                    "message": "meetups not found"}

        else:
            return {
                        "status": 200,
                        "data": MEETUP_LIST
                        }

    def get_upcoming(self):
        upcoming = []
        for meetup in MEETUP_LIST:
            if datetime.strptime(meetup['happeningOn'],
                                 '%d %b %Y') > datetime.today():
                upcoming.insert(0, meetup)
        if len(upcoming) == 0 or len(MEETUP_LIST) == 0:
            return {"status": 404,
                    "message": "meetups not found"}

        else:
            return {
                        "status": 200,
                        "data": upcoming
                        }

    def get_meetup(self, meetup_id):
        val = []
        for meetup in MEETUP_LIST:
            if meetup['meetup_id'] == meetup_id:
                val.insert(0, meetup)
        if len(val) == 0:
            return {"status": 404,
                    "error": "Meetup with the given id not found"}
        else:
            return {
                        "status": 200,
                        "data": val
                        }

    def delete_meetup(self, meetup_id):
        i = 0
        for meetup in MEETUP_LIST:
            if meetup["meetup_id"] == meetup_id:
                MEETUP_LIST.pop(i)

                return {"status": 200,
                        "message": "delete successful"}
            i += 1
            return {"status": 404,
                    "error": "Meetup with the id provided was not found"
                    }


class Rsvp():
    def create_rsvp(self, rsvp_id, meetup_id, user_id, response):
        self.single_rsvp = {}

        self.single_rsvp['rsvp_id'] = rsvp_id
        self.single_rsvp['meetup_id'] = meetup_id
        self.single_rsvp['user_id'] = user_id
        self.single_rsvp['response'] = response

        RSVP_LIST.append(self.single_rsvp)

        return {"status": 201,
                "data": self.single_rsvp
                }
