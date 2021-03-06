# coding: utf-8
import suds
from functools import wraps
from exceptions import RsApiError


def expect_zero_status(func):
    """
    Декоратор, проверяющий результат вызова функций RS API, возвращающих статус в поле `RESULT.STATUS`.
    Если поле объекта `RESULT.STATUS` не найдено или `RESULT.STATUS != 0`, бросает исключение с кодом ошибки.

    :param func: функция, возвращающая `suds.sudsobject.Object`
    :raises: `RsApiError`
    :return: результат вызова функции (`suds.sudsobject.Object`)
    """
    @wraps(func)
    def with_handler(*args, **kwargs):
        response = func(*args, **kwargs)
        if hasattr(response, 'RESULT'):
            if hasattr(response.RESULT, 'STATUS'):
                if response.RESULT.STATUS != '0':
                    raise RsApiError(msg="%s call failed. Expected 0 status." % func.__name__,
                                     error_code=int(response.RESULT.STATUS))
            else:
                raise RsApiError(msg="%s call failed (?) Has 'RESULT' field ('%s'), but no 'STATUS' field (assumed error_code -1)"
                                     % (func.__name__, response.RESULT),
                                 error_code=-1)
        return response
    return with_handler


def expect_int_error_code(error_code):
    """
    Декоратор, проверяющий результат вызова функций RS API, возвращающих цисловой код ошибки.
    Если код не равен `error_code`, бросает исключение с кодом ошибки.

    :param int error_code: ожидаемый код ошибки ("успешно")
    """
    def wrapped_decorator(func):
        """
        :param func: функция, возвращающая `suds.sudsobject.Object`
        :raises: `RsApiError`
        :return: результат вызова функции (`suds.sudsobject.Object`)
        """
        @wraps(func)
        def with_handler(*args, **kwargs):
            try:
                response = func(*args, **kwargs)
                if int(response) != error_code:
                    raise RsApiError(msg="%s call failed (expected error code %s)" % (func.__name__, error_code),
                                     error_code=int(response))
                else:
                    return response
            except ValueError:
                raise RsApiError(msg="%s call failed. Expected error code %s, got non-integer response '%s' (assumed error_code -1)"
                                     % (func.__name__, error_code, response),
                                 error_code=-1)
        return with_handler
    return wrapped_decorator
