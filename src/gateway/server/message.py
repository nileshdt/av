import json
from util.json import CustomEncoder
from fastapi import Response


def setDict(self, d):
    for k, v in d.items():
        if isinstance(v, dict):
            for nested_key, nested_value in v.items():
                if isinstance(nested_value, dict):
                    for x_key, x_value in nested_value.items():
                        self.__dict__[x_key] = x_value
                else:
                    self.__dict__[nested_key] = nested_value
        else:
            self.__dict__[k] = v


class Message:
    def __init__(self, statusid=0, message=None, token=None, **kwargs):
        """
        Create empty base message
        """
        self.statusid = statusid
        self.message = message
        self.token = token
        print(kwargs)
        if 'list' in kwargs:
            print("list")
            self.__dict__ = kwargs
            print(self.__dict__)
        else:
            setDict(self, kwargs)

    def __setattr__(self, key, value):
        """
        Add or update key

        :param str key: object key name
        :param str or float or int value: object value
        """
        self.__dict__[key] = value

    def json(self, status=200) -> Response:
        """
        Encode response as json object

        :return: json response object
        :rtype: Response
        """
        o = self.__dict__
        if self.message is None:
            o.pop('message')

        # encode json object
        return Response(

            status_code=status,
            content=json.dumps(o, cls=CustomEncoder, ensure_ascii=False),
            headers={"ContentType": "application/json; charset=utf-8"}
        )
