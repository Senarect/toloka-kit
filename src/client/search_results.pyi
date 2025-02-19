__all__ = [
    'AggregatedSolutionSearchResult',
    'AssignmentSearchResult',
    'AttachmentSearchResult',
    'MessageThreadSearchResult',
    'ProjectSearchResult',
    'PoolSearchResult',
    'SkillSearchResult',
    'TaskSearchResult',
    'TaskSuiteSearchResult',
    'TrainingSearchResult',
    'UserBonusSearchResult',
    'UserRestrictionSearchResult',
    'UserSkillSearchResult',
    'WebhookSubscriptionSearchResult',
    'OperationSearchResult',
    'AppProjectSearchResult',
    'AppSearchResult',
    'AppItemSearchResult',
    'AppBatchSearchResult',
]
import toloka.client.aggregation
import toloka.client.app
import toloka.client.assignment
import toloka.client.attachment
import toloka.client.message_thread
import toloka.client.operations
import toloka.client.pool
import toloka.client.primitives.base
import toloka.client.project
import toloka.client.skill
import toloka.client.task
import toloka.client.task_suite
import toloka.client.training
import toloka.client.user_bonus
import toloka.client.user_restriction
import toloka.client.user_skill
import toloka.client.webhook_subscription
import typing


class AggregatedSolutionSearchResult(toloka.client.primitives.base.BaseTolokaObject):
    """The result of searching aggregated responses.

    Attributes:
        items: A list with found aggregated responses.
        has_more: A flag showing whether there are more matching aggregated responses.
            * `True` — There are more matching aggregated responses, not included in `items` due to the limit set in the search request.
            * `False` — `items` contains all matching aggregated responses.
    """

    def __init__(
        self,
        *,
        items: typing.Optional[typing.List[toloka.client.aggregation.AggregatedSolution]] = None,
        has_more: typing.Optional[bool] = None
    ) -> None:
        """Method generated by attrs for class AggregatedSolutionSearchResult.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    items: typing.Optional[typing.List[toloka.client.aggregation.AggregatedSolution]]
    has_more: typing.Optional[bool]


class AssignmentSearchResult(toloka.client.primitives.base.BaseTolokaObject):
    """The result of searching assignments.

    Attributes:
        items: A list with found assignments.
        has_more: A flag showing whether there are more matching assignments.
            * `True` — There are more matching assignments, not included in `items` due to the limit set in the search request.
            * `False` — `items` contains all matching assignments.
    """

    def __init__(
        self,
        *,
        items: typing.Optional[typing.List[toloka.client.assignment.Assignment]] = None,
        has_more: typing.Optional[bool] = None
    ) -> None:
        """Method generated by attrs for class AssignmentSearchResult.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    items: typing.Optional[typing.List[toloka.client.assignment.Assignment]]
    has_more: typing.Optional[bool]


class AttachmentSearchResult(toloka.client.primitives.base.BaseTolokaObject):
    """The result of searching attachments.

    Attributes:
        items: A list with found attachments.
        has_more: A flag showing whether there are more matching attachments.
            * `True` — There are more matching attachments, not included in `items` due to the limit set in the search request.
            * `False` — `items` contains all matching attachments.
    """

    def __init__(
        self,
        *,
        items: typing.Optional[typing.List[toloka.client.attachment.Attachment]] = None,
        has_more: typing.Optional[bool] = None
    ) -> None:
        """Method generated by attrs for class AttachmentSearchResult.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    items: typing.Optional[typing.List[toloka.client.attachment.Attachment]]
    has_more: typing.Optional[bool]


class MessageThreadSearchResult(toloka.client.primitives.base.BaseTolokaObject):
    """The result of searching message threads.

    Attributes:
        items: A list with found message threads.
        has_more: A flag showing whether there are more matching message threads.
            * `True` — There are more matching message threads, not included in `items` due to the limit set in the search request.
            * `False` — `items` contains all matching message threads.
    """

    def __init__(
        self,
        *,
        items: typing.Optional[typing.List[toloka.client.message_thread.MessageThread]] = None,
        has_more: typing.Optional[bool] = None
    ) -> None:
        """Method generated by attrs for class MessageThreadSearchResult.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    items: typing.Optional[typing.List[toloka.client.message_thread.MessageThread]]
    has_more: typing.Optional[bool]


class ProjectSearchResult(toloka.client.primitives.base.BaseTolokaObject):
    """The result of searching projects.

    Attributes:
        items: A list with found projects.
        has_more: A flag showing whether there are more matching projects.
            * `True` — There are more matching projects, not included in `items` due to the limit set in the search request.
            * `False` — `items` contains all matching projects.
    """

    def __init__(
        self,
        *,
        items: typing.Optional[typing.List[toloka.client.project.Project]] = None,
        has_more: typing.Optional[bool] = None
    ) -> None:
        """Method generated by attrs for class ProjectSearchResult.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    items: typing.Optional[typing.List[toloka.client.project.Project]]
    has_more: typing.Optional[bool]


class PoolSearchResult(toloka.client.primitives.base.BaseTolokaObject):
    """The result of searching pools.

    Attributes:
        items: A list with found pools.
        has_more: A flag showing whether there are more matching pools.
            * `True` — There are more matching pools, not included in `items` due to the limit set in the search request.
            * `False` — `items` contains all matching pools.
    """

    def __init__(
        self,
        *,
        items: typing.Optional[typing.List[toloka.client.pool.Pool]] = None,
        has_more: typing.Optional[bool] = None
    ) -> None:
        """Method generated by attrs for class PoolSearchResult.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    items: typing.Optional[typing.List[toloka.client.pool.Pool]]
    has_more: typing.Optional[bool]


class SkillSearchResult(toloka.client.primitives.base.BaseTolokaObject):
    """The result of searching skills.

    Attributes:
        items: A list with found skills.
        has_more: A flag showing whether there are more matching skills.
            * `True` — There are more matching skills, not included in `items` due to the limit set in the search request.
            * `False` — `items` contains all matching skills.
    """

    def __init__(
        self,
        *,
        items: typing.Optional[typing.List[toloka.client.skill.Skill]] = None,
        has_more: typing.Optional[bool] = None
    ) -> None:
        """Method generated by attrs for class SkillSearchResult.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    items: typing.Optional[typing.List[toloka.client.skill.Skill]]
    has_more: typing.Optional[bool]


class TaskSearchResult(toloka.client.primitives.base.BaseTolokaObject):
    """The result of searching tasks.

    Attributes:
        items: A list with found tasks.
        has_more: A flag showing whether there are more matching tasks.
            * `True` — There are more matching tasks, not included in `items` due to the limit set in the search request.
            * `False` — `items` contains all matching tasks.
    """

    def __init__(
        self,
        *,
        items: typing.Optional[typing.List[toloka.client.task.Task]] = None,
        has_more: typing.Optional[bool] = None
    ) -> None:
        """Method generated by attrs for class TaskSearchResult.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    items: typing.Optional[typing.List[toloka.client.task.Task]]
    has_more: typing.Optional[bool]


class TaskSuiteSearchResult(toloka.client.primitives.base.BaseTolokaObject):
    """The result of searching task suites.

    Attributes:
        items: A list with found task suites.
        has_more: A flag showing whether there are more matching task suites.
            * `True` — There are more matching task suites, not included in `items` due to the limit set in the search request.
            * `False` — `items` contains all matching task suites.
    """

    def __init__(
        self,
        *,
        items: typing.Optional[typing.List[toloka.client.task_suite.TaskSuite]] = None,
        has_more: typing.Optional[bool] = None
    ) -> None:
        """Method generated by attrs for class TaskSuiteSearchResult.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    items: typing.Optional[typing.List[toloka.client.task_suite.TaskSuite]]
    has_more: typing.Optional[bool]


class TrainingSearchResult(toloka.client.primitives.base.BaseTolokaObject):
    """The result of searching training pools.

    Attributes:
        items: A list with found training pools.
        has_more: A flag showing whether there are more matching training pools.
            * `True` — There are more matching training pools, not included in `items` due to the limit set in the search request.
            * `False` — `items` contains all matching training pools.
    """

    def __init__(
        self,
        *,
        items: typing.Optional[typing.List[toloka.client.training.Training]] = None,
        has_more: typing.Optional[bool] = None
    ) -> None:
        """Method generated by attrs for class TrainingSearchResult.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    items: typing.Optional[typing.List[toloka.client.training.Training]]
    has_more: typing.Optional[bool]


class UserBonusSearchResult(toloka.client.primitives.base.BaseTolokaObject):
    """The result of searching Tolokers' rewards.

    Attributes:
        items: A list with found rewards.
        has_more: A flag showing whether there are more matching rewards.
            * `True` — There are more matching rewards, not included in `items` due to the limit set in the search request.
            * `False` — `items` contains all matching rewards.
    """

    def __init__(
        self,
        *,
        items: typing.Optional[typing.List[toloka.client.user_bonus.UserBonus]] = None,
        has_more: typing.Optional[bool] = None
    ) -> None:
        """Method generated by attrs for class UserBonusSearchResult.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    items: typing.Optional[typing.List[toloka.client.user_bonus.UserBonus]]
    has_more: typing.Optional[bool]


class UserRestrictionSearchResult(toloka.client.primitives.base.BaseTolokaObject):
    """The result of searching Toloker restrictions.

    Attributes:
        items: A list with found Toloker restrictions.
        has_more: A flag showing whether there are more matching Toloker restrictions.
            * `True` — There are more matching Toloker restrictions, not included in `items` due to the limit set in the search request.
            * `False` — `items` contains all matching Toloker restrictions.
    """

    def __init__(
        self,
        *,
        items: typing.Optional[typing.List[toloka.client.user_restriction.UserRestriction]] = None,
        has_more: typing.Optional[bool] = None
    ) -> None:
        """Method generated by attrs for class UserRestrictionSearchResult.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    items: typing.Optional[typing.List[toloka.client.user_restriction.UserRestriction]]
    has_more: typing.Optional[bool]


class UserSkillSearchResult(toloka.client.primitives.base.BaseTolokaObject):
    """The result of searching Tolokers' skills.

    Attributes:
        items: A list with found skills.
        has_more: A flag showing whether there are more matching skills.
            * `True` — There are more matching skills, not included in `items` due to the limit set in the search request.
            * `False` — `items` contains all matching skills.
    """

    def __init__(
        self,
        *,
        items: typing.Optional[typing.List[toloka.client.user_skill.UserSkill]] = None,
        has_more: typing.Optional[bool] = None
    ) -> None:
        """Method generated by attrs for class UserSkillSearchResult.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    items: typing.Optional[typing.List[toloka.client.user_skill.UserSkill]]
    has_more: typing.Optional[bool]


class WebhookSubscriptionSearchResult(toloka.client.primitives.base.BaseTolokaObject):
    """The result of searching webhook subscriptions.

    Attributes:
        items: A list with found subscriptions.
        has_more: A flag showing whether there are more matching subscriptions.
            * `True` — There are more matching subscriptions, not included in `items` due to the limit set in the search request.
            * `False` — `items` contains all matching subscriptions.
    """

    def __init__(
        self,
        *,
        items: typing.Optional[typing.List[toloka.client.webhook_subscription.WebhookSubscription]] = None,
        has_more: typing.Optional[bool] = None
    ) -> None:
        """Method generated by attrs for class WebhookSubscriptionSearchResult.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    items: typing.Optional[typing.List[toloka.client.webhook_subscription.WebhookSubscription]]
    has_more: typing.Optional[bool]


class OperationSearchResult(toloka.client.primitives.base.BaseTolokaObject):
    """The list of found operations and whether there is something else on the original request

    It's better to use TolokaClient.get_operations(),
    which already implements the correct handling of the search result.

    Attributes:
        items: List of found operations
        has_more: Whether the list is complete:
            * `True` — Not all elements are included in the output due to restrictions in the limit parameter.
            * `False` — The output lists all the items.
    """

    def __init__(
        self,
        *,
        items: typing.Optional[typing.List[toloka.client.operations.Operation]] = None,
        has_more: typing.Optional[bool] = None
    ) -> None:
        """Method generated by attrs for class OperationSearchResult.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    items: typing.Optional[typing.List[toloka.client.operations.Operation]]
    has_more: typing.Optional[bool]


class AppProjectSearchResult(toloka.client.primitives.base.BaseTolokaObject):
    """The result of searching App projects.

    Attributes:
        content: A list with found App projects.
        has_more: A flag showing whether there are more matching App projects.
            * `True` — There are more matching App projects, not included in `content` due to the limit set in the search request.
            * `False` — `content` contains all matching App projects.
    """

    def __init__(
        self,
        *,
        content: typing.Optional[typing.List[toloka.client.app.AppProject]] = None,
        has_more: typing.Optional[bool] = None
    ) -> None:
        """Method generated by attrs for class AppProjectSearchResult.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    content: typing.Optional[typing.List[toloka.client.app.AppProject]]
    has_more: typing.Optional[bool]


class AppSearchResult(toloka.client.primitives.base.BaseTolokaObject):
    """The result of searching App solutions.

    Attributes:
        content: A list with found App solutions.
        has_more: A flag showing whether there are more matching App solutions.
            * `True` — There are more matching App solutions, not included in `content` due to the limit set in the search request.
            * `False` — `content` contains all matching App solutions.
    """

    def __init__(
        self,
        *,
        content: typing.Optional[typing.List[toloka.client.app.App]] = None,
        has_more: typing.Optional[bool] = None
    ) -> None:
        """Method generated by attrs for class AppSearchResult.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    content: typing.Optional[typing.List[toloka.client.app.App]]
    has_more: typing.Optional[bool]


class AppItemSearchResult(toloka.client.primitives.base.BaseTolokaObject):
    """The result of searching App task items.

    Attributes:
        content: A list with found task items.
        has_more: A flag showing whether there are more matching task items.
            * `True` — There are more matching task items, not included in `content` due to the limit set in the search request.
            * `False` — `content` contains all matching task items.
    """

    def __init__(
        self,
        *,
        content: typing.Optional[typing.List[toloka.client.app.AppItem]] = None,
        has_more: typing.Optional[bool] = None
    ) -> None:
        """Method generated by attrs for class AppItemSearchResult.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    content: typing.Optional[typing.List[toloka.client.app.AppItem]]
    has_more: typing.Optional[bool]


class AppBatchSearchResult(toloka.client.primitives.base.BaseTolokaObject):
    """The result of searching batches in an App project.

    Attributes:
        content: A list with found batches.
        has_more: A flag showing whether there are more matching batches.
            * `True` — There are more matching batches, not included in `content` due to the limit set in the search request.
            * `False` — `content` contains all matching batches.
    """

    def __init__(
        self,
        *,
        content: typing.Optional[typing.List[toloka.client.app.AppBatch]] = None,
        has_more: typing.Optional[bool] = None
    ) -> None:
        """Method generated by attrs for class AppBatchSearchResult.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    content: typing.Optional[typing.List[toloka.client.app.AppBatch]]
    has_more: typing.Optional[bool]
