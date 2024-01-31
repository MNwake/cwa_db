import mongoengine as db


class Park(db.Document):
    name = db.StringField(required=True)
    state = db.StringField(required=True)
    abbreviation = db.StringField(required=True)
    team_name = db.StringField()
    cable = db.ListField(db.ReferenceField('Cable'))

