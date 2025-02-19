__all__ = [
    'BaseTask',
    'Task',
    'CreateTaskParameters',
    'CreateTasksParameters',
    'TaskOverlapPatch',
    'TaskPatch',
]
import datetime
import toloka.client.primitives.base
import toloka.client.primitives.infinite_overlap
import toloka.client.primitives.parameter
import typing
import uuid


class BaseTask(toloka.client.primitives.base.BaseTolokaObject):
    """A base class for tasks.

    Attributes:
        input_values: A dictionary with input data for a task. Input field names are keys in the dictionary.
        known_solutions: A list of all responses considered correct. It is used with control and training tasks.
                        If there are several output fields, then you must specify all their correct combinations.
        message_on_unknown_solution: A hint used in training tasks.
        id: The ID of a task.
        origin_task_id: The ID of a parent task. This parameter is set if the task was created by copying.
    """

    class KnownSolution(toloka.client.primitives.base.BaseTolokaObject):
        """A correct response for a control or training task.

        Responses have a correctness weight.
        For example, if `correctness_weight` is 0.5,
        then half of the error is counted to the Toloker.

        Attributes:
            output_values: Correct values of output fields.
            correctness_weight: The correctness weight of the response.
        """

        def __init__(
            self,
            *,
            output_values: typing.Optional[typing.Dict[str, typing.Any]] = None,
            correctness_weight: typing.Optional[float] = None
        ) -> None:
            """Method generated by attrs for class BaseTask.KnownSolution.
            """
            ...

        _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
        output_values: typing.Optional[typing.Dict[str, typing.Any]]
        correctness_weight: typing.Optional[float]

    def __init__(
        self,
        *,
        input_values: typing.Optional[typing.Dict[str, typing.Any]] = None,
        known_solutions: typing.Optional[typing.List[KnownSolution]] = None,
        message_on_unknown_solution: typing.Optional[str] = None,
        id: typing.Optional[str] = None,
        origin_task_id: typing.Optional[str] = None
    ) -> None:
        """Method generated by attrs for class BaseTask.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    input_values: typing.Optional[typing.Dict[str, typing.Any]]
    known_solutions: typing.Optional[typing.List[KnownSolution]]
    message_on_unknown_solution: typing.Optional[str]
    id: typing.Optional[str]
    origin_task_id: typing.Optional[str]


class Task(toloka.client.primitives.infinite_overlap.InfiniteOverlapParametersMixin, BaseTask):
    """A task that is assigned to Tolokers.

    Tasks are grouped into [TaskSuites](toloka.client.task_suite.TaskSuite.md).

    Attributes:
        input_values: A dictionary with input data for a task. Input field names are keys in the dictionary.
        known_solutions: A list of all responses considered correct. It is used with control and training tasks.
            If there are several output fields, then you must specify all their correct combinations.
        message_on_unknown_solution: A hint used in training tasks.
        id: The ID of a task.
        pool_id: The ID of the pool that the task belongs to.
        remaining_overlap: The number of times left for this task to be assigned to Tolokers. Read-only field.
        reserved_for: IDs of Tolokers who have access to the task.
        unavailable_for: IDs of Tolokers who don't have access to the task.
        traits_all_of: The task can be assigned to Tolokers who have all of the specified traits.
        traits_any_of: The task can be assigned to Tolokers who have any of the specified traits.
        traits_none_of_any: The task can not be assigned to Tolokers who have any of the specified traits.
        origin_task_id: The ID of a parent task. This parameter is set if the task was created by copying.
        created: The UTC date and time when the task was created.
        baseline_solutions: Preliminary responses for dynamic overlap and aggregation of results by skill. They are used to calculate a confidence level of the first responses from Toloker.

    Examples:
        Creating a simple task with one input field.

        >>> task = toloka.client.Task(
        >>>     input_values={'image': 'https://some.url/img0.png'},
        >>>     pool_id='1'
        >>> )
        ...

        See more complex example in the description of the [create_tasks](toloka.client.TolokaClient.create_tasks.md) method.
    """

    class BaselineSolution(toloka.client.primitives.base.BaseTolokaObject):
        """A preliminary response.
        """

        def __init__(
            self,
            *,
            output_values: typing.Optional[typing.Dict[str, typing.Any]] = None,
            confidence_weight: typing.Optional[float] = None
        ) -> None:
            """Method generated by attrs for class Task.BaselineSolution.
            """
            ...

        _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
        output_values: typing.Optional[typing.Dict[str, typing.Any]]
        confidence_weight: typing.Optional[float]

    def __init__(
        self,
        *,
        input_values: typing.Optional[typing.Dict[str, typing.Any]] = None,
        known_solutions: typing.Optional[typing.List[BaseTask.KnownSolution]] = None,
        message_on_unknown_solution: typing.Optional[str] = None,
        id: typing.Optional[str] = None,
        infinite_overlap=None,
        overlap=None,
        pool_id: typing.Optional[str] = None,
        remaining_overlap: typing.Optional[int] = None,
        reserved_for: typing.Optional[typing.List[str]] = None,
        unavailable_for: typing.Optional[typing.List[str]] = None,
        traits_all_of: typing.Optional[typing.List[str]] = None,
        traits_any_of: typing.Optional[typing.List[str]] = None,
        traits_none_of_any: typing.Optional[typing.List[str]] = None,
        origin_task_id: typing.Optional[str] = None,
        created: typing.Optional[datetime.datetime] = None,
        baseline_solutions: typing.Optional[typing.List[BaselineSolution]] = None
    ) -> None:
        """Method generated by attrs for class Task.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    input_values: typing.Optional[typing.Dict[str, typing.Any]]
    known_solutions: typing.Optional[typing.List[BaseTask.KnownSolution]]
    message_on_unknown_solution: typing.Optional[str]
    id: typing.Optional[str]
    origin_task_id: typing.Optional[str]
    _infinite_overlap: typing.Optional[bool]
    _overlap: typing.Optional[int]
    pool_id: typing.Optional[str]
    remaining_overlap: typing.Optional[int]
    reserved_for: typing.Optional[typing.List[str]]
    unavailable_for: typing.Optional[typing.List[str]]
    traits_all_of: typing.Optional[typing.List[str]]
    traits_any_of: typing.Optional[typing.List[str]]
    traits_none_of_any: typing.Optional[typing.List[str]]
    created: typing.Optional[datetime.datetime]
    baseline_solutions: typing.Optional[typing.List[BaselineSolution]]


class CreateTaskParameters(toloka.client.primitives.parameter.IdempotentOperationParameters):
    """Parameters used with the [create_task](toloka.client.TolokaClient.create_task.md) method.

    If the operation is started in an asynchronous mode,
    we recommend that you send the `operation_id` to avoid creating the same tasks multiple times. You can use this ID later to get information about the operation.

    Attributes:
        operation_id: The ID of the operation conforming to the [RFC4122 standard](https://tools.ietf.org/html/rfc4122).
        async_mode: Request processing mode:
            * `True` — Asynchronous operation is started internally and `create_tasks` waits for the completion of it. It is recommended to create no more than 10,000 tasks per request in this mode.
            * `False` — The request is processed synchronously. A maximum of 5000 tasks can be added in a single request in this mode.
            Default value: `True`.
        allow_defaults: Active overlap setting:
            * `True` — Use the overlap that is set in the `defaults.default_overlap_for_new_tasks` pool parameter.
            * `False` — Use the overlap that is set in the `overlap` task parameter.

            Default value: `False`.
        open_pool: Open the pool immediately after creating a task suite, if the pool is closed.
            Default value: `False`.
    """

    def __init__(
        self,
        *,
        operation_id: typing.Optional[uuid.UUID] = ...,
        async_mode: typing.Optional[bool] = True,
        allow_defaults: typing.Optional[bool] = None,
        open_pool: typing.Optional[bool] = None
    ) -> None:
        """Method generated by attrs for class CreateTaskParameters.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    operation_id: typing.Optional[uuid.UUID]
    async_mode: typing.Optional[bool]
    allow_defaults: typing.Optional[bool]
    open_pool: typing.Optional[bool]


class CreateTasksParameters(CreateTaskParameters):
    """Parameters used with the [create_tasks](toloka.client.TolokaClient.create_tasks.md)

    and [create_tasks_async](toloka.client.TolokaClient.create_tasks_async.md) methods.

    If the operation is started in an asynchronous mode,
    we recommend that you send the `operation_id` to avoid creating the same tasks multiple times. You can use this ID later to get information about the operation.

    Attributes:
        operation_id: The ID of the operation conforming to the [RFC4122 standard](https://tools.ietf.org/html/rfc4122).
        async_mode: Request processing mode:
            * `True` — Asynchronous operation is started internally and `create_tasks` waits for the completion of it. It is recommended to create no more than 10,000 tasks per request in this mode.
            * `False` — The request is processed synchronously. A maximum of 5000 tasks can be added in a single request in this mode.
            Default value: `True`.
        allow_defaults: Active overlap setting:
            * `True` — Use the overlap that is set in the `defaults.default_overlap_for_new_tasks` pool parameter.
            * `False` — Use the overlap that is set in the `overlap` task parameter.

            Default value: `False`.
        open_pool: Open the pool immediately after creating a task suite, if the pool is closed.
            Default value: `False`.
        skip_invalid_items: Task validation option:
            * `True` — All valid tasks are added. If a task does not pass validation, then it is not added to Toloka. All such tasks are listed in the response.
            * `False` — If any task does not pass validation, then the operation is cancelled and no tasks are added to Toloka.

            Default value: `False`.
    """

    def __init__(
        self,
        *,
        operation_id: typing.Optional[uuid.UUID] = ...,
        async_mode: typing.Optional[bool] = True,
        allow_defaults: typing.Optional[bool] = None,
        open_pool: typing.Optional[bool] = None,
        skip_invalid_items: typing.Optional[bool] = None
    ) -> None:
        """Method generated by attrs for class CreateTasksParameters.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    operation_id: typing.Optional[uuid.UUID]
    async_mode: typing.Optional[bool]
    allow_defaults: typing.Optional[bool]
    open_pool: typing.Optional[bool]
    skip_invalid_items: typing.Optional[bool]


class TaskOverlapPatch(toloka.client.primitives.base.BaseTolokaObject):
    """Parameters for changing the overlap of a task.

    Attributes:
        overlap: The new overlap value.
        infinite_overlap:
            * `True` — The task is assigned to all Tolokers. It is usually set for training and control tasks.
            * `False` — An overlap value specified for the task or for the pool is used.

            Default value: `False`.
    """

    def __init__(
        self,
        *,
        overlap: typing.Optional[int] = None,
        infinite_overlap: typing.Optional[bool] = None
    ) -> None:
        """Method generated by attrs for class TaskOverlapPatch.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    overlap: typing.Optional[int]
    infinite_overlap: typing.Optional[bool]


class TaskPatch(TaskOverlapPatch):
    """Parameters for changing a task.

    Attributes:
        overlap: The new overlap value.
        infinite_overlap: * `True` — The task is assigned to all Tolokers. It is usually set for training and control tasks.
            * `False` — An overlap value specified for the task or for the pool is used.

            Default value: `False`.
        baseline_solutions: Preliminary responses for dynamic overlap and aggregation of results by a skill. They are used to calculate a confidence level of the first responses from Tolokers.
        known_solutions: A list of all responses considered correct. It is used with control and training tasks.
            If there are several output fields, then you must specify all their correct combinations.
        message_on_unknown_solution: A hint used in training tasks.
    """

    def __init__(
        self,
        *,
        overlap: typing.Optional[int] = None,
        infinite_overlap: typing.Optional[bool] = None,
        baseline_solutions: typing.Optional[typing.List[Task.BaselineSolution]] = None,
        known_solutions: typing.Optional[typing.List[BaseTask.KnownSolution]] = None,
        message_on_unknown_solution: typing.Optional[str] = None
    ) -> None:
        """Method generated by attrs for class TaskPatch.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    overlap: typing.Optional[int]
    infinite_overlap: typing.Optional[bool]
    baseline_solutions: typing.Optional[typing.List[Task.BaselineSolution]]
    known_solutions: typing.Optional[typing.List[BaseTask.KnownSolution]]
    message_on_unknown_solution: typing.Optional[str]
