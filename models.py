from mongoengine import EmbeddedDocument, Document
from mongoengine.fields import EmbeddedDocumentField, DateTimeField,  ListField, StringField, IntField, ReferenceField


class Phone(EmbeddedDocument):
    phone = IntField()


class Birthday(EmbeddedDocument):
    birthday = DateTimeField()

class Person(Document):
    name = StringField()
    birthday = EmbeddedDocumentField(Birthday)
    phones =ListField(EmbeddedDocumentField(Phone))


