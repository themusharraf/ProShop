import datetime
import uuid

from django.core.validators import RegexValidator, ValidationError
from django.db.models import Model, UUIDField, DateTimeField

MEDIA_TYPES = {
    r'^(jpg|jpeg|png|JPG)$': 'image',
    r'^(mp4)$': 'videos'
}

FILE_TYPES = {
    r'^(jpg|jpeg|png|JPG)$': 'image',
    r'^(pdf)$': 'documents',
    r'^(mp4)$': 'videos'
}


def upload_name(instance, filename):
    file_type = filename.split('.')[-1]
    today = str(datetime.datetime.today())[0:7]

    for regex, folder in FILE_TYPES.items():
        try:
            RegexValidator(regex).__call__(file_type)
            return 'file/%s/%s/%s.%s' % (folder, today, uuid.uuid4(), file_type)
        except ValidationError:
            pass
    raise ValidationError('File type is unacceptable')


class BaseMeta:
    abstract = True


class BaseIDModel(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta(BaseMeta):
        pass


class BaseDateModel:
    updated_at = DateTimeField(auto_now=True)
    created_at = DateTimeField(auto_now_add=True)
