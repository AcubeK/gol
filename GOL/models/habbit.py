from mongoengine import Document,IntField,StringField

class Habbit(Document):
    tit = StringField()
    bnf = StringField()
    streak = IntField()
    st = IntField()
    knl = IntField()
    cre = IntField()
    per = IntField()
    soc = IntField()    