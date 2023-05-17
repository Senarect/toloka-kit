__all__ = [
    'UserBonus',
    'UserBonusCreateRequestParameters',
    'UserBonusesCreateRequestParameters',
]
import datetime
import decimal
import toloka.client.primitives.base
import toloka.client.primitives.parameter
import typing
import uuid


class UserBonus(toloka.client.primitives.base.BaseTolokaObject):
    """Issuing a bonus to a specific Toloker.

    It's addition to payment for completed tasks.

    Attributes:
        user_id: Toloker's ID to whom the bonus will be issued.
        amount: The bonus amount in dollars. Can be from 0.01 to 100 dollars per Toloker per time.
        private_comment: Comments that are only visible to the requester.
        public_title: Message header for the Toloker. You can provide a title in several languages
            (the message will come in the Toloker's language). Format {'language': 'title', ... }.
            The language can be RU/EN/TR/ID/FR.
        public_message: Message text for the Toloker. You can provide text in several languages
            (the message will come in the Toloker's language). Format {'language': 'message', ... }.
            The language can be RU/EN/TR/ID/FR.
        without_message: Do not send a bonus message to the Toloker. To award a bonus without a message, specify null
            for `public_title` and `public_message` and `True` for `without_message`.
        assignment_id: ID of the Toloker's response to the task a reward is issued for.
        id: Internal ID of the issued bonus. Read-only field.
        created: Date the bonus was awarded, in UTC. Read-only field.

    Example:
        How to create bonus with message for specific assignment.

        >>> new_bonus = toloka_client.create_user_bonus(
        >>>     UserBonus(
        >>>         user_id='1',
        >>>         amount='0.50',
        >>>         public_title={
        >>>             'EN': 'Perfect job!',
        >>>         },
        >>>         public_message={
        >>>             'EN': 'You are the best Toloker',
        >>>         },
        >>>         assignment_id='012345'
        >>>     )
        >>> )
        ...

        How to create bonus with message in several languages.

        >>> new_bonus = toloka_client.create_user_bonus(
        >>>     UserBonus(
        >>>         user_id='1',
        >>>         amount='0.10',
        >>>         public_title={
        >>>             'EN': 'Good Job!',
        >>>             'RU': 'Молодец!',
        >>>         },
        >>>         public_message={
        >>>             'EN': 'Ten tasks completed',
        >>>             'RU': 'Выполнено 10 заданий',
        >>>         }
        >>>     )
        >>> )
        ...
    """

    def __init__(
        self,
        *,
        user_id: typing.Optional[str] = None,
        amount: typing.Optional[decimal.Decimal] = None,
        private_comment: typing.Optional[str] = None,
        public_title: typing.Optional[typing.Dict[str, str]] = None,
        public_message: typing.Optional[typing.Dict[str, str]] = None,
        without_message: typing.Optional[bool] = None,
        assignment_id: typing.Optional[str] = None,
        id: typing.Optional[str] = None,
        created: typing.Optional[datetime.datetime] = None
    ) -> None:
        """Method generated by attrs for class UserBonus.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    user_id: typing.Optional[str]
    amount: typing.Optional[decimal.Decimal]
    private_comment: typing.Optional[str]
    public_title: typing.Optional[typing.Dict[str, str]]
    public_message: typing.Optional[typing.Dict[str, str]]
    without_message: typing.Optional[bool]
    assignment_id: typing.Optional[str]
    id: typing.Optional[str]
    created: typing.Optional[datetime.datetime]


class UserBonusCreateRequestParameters(toloka.client.primitives.parameter.IdempotentOperationParameters):
    """Parameters for creating bonus for Toloker.

    Used in methods 'create_user_bonus' of the class TolokaClient.

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
        """Method generated by attrs for class UserBonusCreateRequestParameters.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    operation_id: typing.Optional[uuid.UUID]
    async_mode: typing.Optional[bool]


class UserBonusesCreateRequestParameters(UserBonusCreateRequestParameters):
    """Parameters for creating bonuses for Tolokers.

    Used in methods 'create_user_bonuses' и 'create_user_bonuses_async' of the class TolokaClient,
    to clarify the behavior when creating bonuses.

    Attributes:
        operation_id: The ID of the operation conforming to the [RFC4122 standard](https://tools.ietf.org/html/rfc4122).
        async_mode: Request processing mode:
            * `True` — Asynchronous operation is started internally.
            * `False` — The request is processed synchronously.

            Default value: `True`.
        skip_invalid_items: Validation parameters of objects:
            * `True` — Award a bonus if the object with bonus information passed validation. Otherwise, skip the bonus.
            * `False` — Default behavior. Stop the operation and don't award bonuses if at least one object didn't pass validation.
    """

    def __init__(
        self,
        *,
        operation_id: typing.Optional[uuid.UUID] = ...,
        async_mode: typing.Optional[bool] = True,
        skip_invalid_items: typing.Optional[bool] = None
    ) -> None:
        """Method generated by attrs for class UserBonusesCreateRequestParameters.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    operation_id: typing.Optional[uuid.UUID]
    async_mode: typing.Optional[bool]
    skip_invalid_items: typing.Optional[bool]
