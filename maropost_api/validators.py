from .exceptions import (APPLICATION_ERROR, BAD_REQUEST, BadRequest, HttpError,
                         METHOD_NOT_ALLOWED, MethodNotAllowed, NOT_FOUND,
                         NotFound, REQUEST_LIMIT_EXCEED, RequestLimitExceed,
                         UNAUTHORIZED, Unauthorized, UNPROCESSABLE_ENTITY, UnProcessableEntity)


class MaropostValidator(object):
    def __init__(self):
        pass

    def __call__(self, response):
        self.response = response
        return self

    def validate(self):
        status_code = self.response.status_code
        data = {}
        try:
            data = self.response.json()
        except:
            pass

        if isinstance(data, dict) and data.get('status'):
            status_code = data.get('status')
        error_message = None
        if status_code < 200 or status_code > 299:
            error_message = data.get('message') if data else None
            if not error_message and data and 'base' in data and isinstance(data['base'], list):
                error_message = ';'.join(data['base'])
        if status_code == BAD_REQUEST:
            raise BadRequest(error_message)
        elif status_code == NOT_FOUND:
            raise NotFound(error_message)
        elif status_code == REQUEST_LIMIT_EXCEED:
            raise RequestLimitExceed(error_message)
        elif status_code == METHOD_NOT_ALLOWED:
            raise MethodNotAllowed(error_message)
        elif status_code == APPLICATION_ERROR:
            raise HttpError(error_message)
        elif status_code == UNAUTHORIZED:
            raise Unauthorized(error_message)
        elif status_code == UNPROCESSABLE_ENTITY:
            raise UnProcessableEntity(error_message)
        return data
