import json

from flask import Response


class NLPResponse(Response):
    def __init__(self, body, status_code, jsonfy=True):
        if body is not None:
            if jsonfy:
                super().__init__(json.dumps(body), status=status_code, mimetype='application/json')
            else:
                super().__init__(body, status=status_code)
        else:
            super().__init__(json.dumps(dict()), status=status_code, mimetype='application/json')
