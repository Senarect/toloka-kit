__all__ = [
    'Parameters',
    'IdempotentOperationParameters',
]
import toloka.client.primitives.base
import typing
import uuid


class Parameters(toloka.client.primitives.base.BaseTolokaObject):
    def unstructure(self) -> dict: ...

    def __init__(self) -> None:
        """Method generated by attrs for class Parameters.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]


class IdempotentOperationParameters(Parameters):
    """Parameters for idempotent operations such as tasks, task suites and user bonuses creation.

    Works only with async_mode = True

    Attributes:
        operation_id: The ID of the operation conforming to the [RFC4122 standard](https://tools.ietf.org/html/rfc4122).
        async_mode: Request processing mode:
            * `True` — Asynchronous operation is started internally.
            * `False` — The request is processed synchronously.

            Default value: `True`.
    """

    def __init__(
        self,
        *,
        operation_id: typing.Optional[uuid.UUID] = ...,
        async_mode: typing.Optional[bool] = True
    ) -> None:
        """Method generated by attrs for class IdempotentOperationParameters.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    operation_id: typing.Optional[uuid.UUID]
    async_mode: typing.Optional[bool]
