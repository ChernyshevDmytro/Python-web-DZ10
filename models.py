from mongoengine import EmbeddedDocument, Document
from mongoengine.fields import DateTimeField,  ListField, StringField


class Person(Document):
    name = StringField()
    birthday = DateTimeField()
    phones =ListField(StringField()) 
