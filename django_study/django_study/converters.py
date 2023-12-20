from django.urls import converters
from datetime import timedelta
class YearConverter(converters.IntConverter):
    """
    年份转换器
    """
    regex = r"(19|20)\d{2}"




class TimeDeltaConverter:

    regex = r"\d+(s|m|h|d)"
    def to_python(self, value):
        number = int(value[0: -1])
        unit = value[-1]
        if unit == "s":
            return timedelta(seconds=number)
        elif unit == "m":
            return timedelta(minutes=number)
        elif unit == "h":
            return timedelta(hours=number)
        return timedelta(days=number)



    def to_url(self, value):
        return str(value)

"""
编写一个user 参数类型转换器, 可以将 xxxx:yyy 格式的字符串转换成{username: XXX, password: yyy}
"""
class UserConverter:
    regex = r"\w+:\w+"
    def to_python(self, value):
        username,password = value.split(":")
        return {"username":username, "password":password}

    def to_url(self, value):
        return str(value)