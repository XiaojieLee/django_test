from .converters import YearConverter,TimeDeltaConverter,UserConverter
from django.urls import converters


converters.register_converter(YearConverter,"year")
converters.register_converter(TimeDeltaConverter,type_name="timedelta")
converters.register_converter(UserConverter,type_name="user")