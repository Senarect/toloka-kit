__all__ = [
    'BaseTask',
    'Task',
    'CreateTaskParameters',
    'CreateTaskAsyncParameters',
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
    """Base class for Task

    Attributes:
        input_values: Input data for a task. List of pairs:
            "<input field ID 1>": "<field value 1>",
            "<input field ID 1>": "<field value 2>",
            ...
            "<input field ID n>": "<field value n>"
        known_solutions: Responses and hints for control tasks and training tasks. If multiple output fields are included
            in the validation, all combinations of the correct response must be specified.
        message_on_unknown_solution: Hint for the task (for training tasks).
        id: Task ID.
        origin_task_id: ID of the task it was copied from.
    """

    class KnownSolution(toloka.client.primitives.base.BaseTolokaObject):
        """Answers and hints for control and training tasks.

        If several output fields are taken into account when checking, you must specify all combinations of the correct answer.

        Attributes:
            output_values: Correct answers in the task (for control tasks). If there are several correct answer options,
                for each option you need to define output_values and give the weight of the correct answer (key correctness_weight).
                "<output field id 1>": "<correct answer value 1>",
                "<output field id 2>": "<correct answer value 2>",
                ...
                "<output field id n>": "<correct answer value n>"
            correctness_weight: Weight of the correct answer. Allows you to set several options for correct answers and
                rank them by correctness. For example, if the weight of the correct answer is 0.5, half of the error is
                counted to the user. The more correct the answer in correctValues, the higher its weight.
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
    """The task that will be issued to the performers

    Not to be confused with TaskSuite - a set of tasks that is shown to the user at one time.
    TaskSuite may contain several Tasks.

    Attributes:
        input_values: Input data for a task. List of pairs:
            "<input field ID 1>": "<field value 1>",
            "<input field ID 1>": "<field value 2>",
            ...
            "<input field ID n>": "<field value n>"
        known_solutions: Responses and hints for control tasks and training tasks. If multiple output fields are included
            in the validation, all combinations of the correct response must be specified.
        message_on_unknown_solution: Hint for the task (for training tasks).
        id: Task ID.
        pool_id: The ID of the pool that the task is uploaded to.
        remaining_overlap: How many times will this task be issued to performers. Read Only field.
        reserved_for: IDs of users who will have access to the task.
        unavailable_for: IDs of users who shouldn't have access to the task.
        traits_all_of: 
        traits_any_of: 
        traits_none_of_any: 
        origin_task_id: ID of the task it was copied from.
        created: The UTC date and time when the task was created.
        baseline_solutions: Preliminary responses. This data simulates performer responses when calculating confidence in a response.
            It is used in dynamic overlap (also known as incremental relabeling or IRL) and aggregation of results by skill.

    Examples:
        How to create tasks.

        >>> tasks = [
        >>>     Task(input_values={'image': 'https://some.url/my_img0001.png'}, pool_id=my_pool_id),
        >>>     Task(input_values={'image': 'https://some.url/my_img0002.png'}, pool_id=my_pool_id),
        >>> ]
        >>> created_tasks = toloka_client.create_tasks(tasks, allow_defaults=True)
        >>> print(len(created_tasks.items))
        ...
    """

    class BaselineSolution(toloka.client.primitives.base.BaseTolokaObject):
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


class CreateTaskParameters(toloka.client.primitives.parameter.Parameters):
    """Parameters for Task creation controlling

    Used when creating one Task.

    Attributes:
        allow_defaults: Active overlap setting:
            * True — Use the overlap value that is set in the `defaults.default_overlap_for_new_task_suites` pool parameter.
            * False — Use the overlap value that is set in the `overlap` task suite parameter.
        open_pool: Open the pool immediately after creating a task suite, if the pool is closed.
    """

    def __init__(
        self,
        *,
        allow_defaults: typing.Optional[bool] = None,
        open_pool: typing.Optional[bool] = None
    ) -> None:
        """Method generated by attrs for class CreateTaskParameters.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    allow_defaults: typing.Optional[bool]
    open_pool: typing.Optional[bool]


class CreateTaskAsyncParameters(CreateTaskParameters):
    """Attributes:
        allow_defaults: Active overlap setting:
            * True — Use the overlap value that is set in the `defaults.default_overlap_for_new_task_suites` pool parameter.
            * False — Use the overlap value that is set in the `overlap` task suite parameter.
        open_pool: Open the pool immediately after creating a task suite, if the pool is closed.
    """

    def __init__(
        self,
        *,
        allow_defaults: typing.Optional[bool] = None,
        open_pool: typing.Optional[bool] = None,
        operation_id: typing.Optional[uuid.UUID] = None
    ) -> None:
        """Method generated by attrs for class CreateTaskAsyncParameters.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    allow_defaults: typing.Optional[bool]
    open_pool: typing.Optional[bool]
    operation_id: typing.Optional[uuid.UUID]


class CreateTasksParameters(CreateTaskParameters):
    """Parameters for Tasks creation controlling

    Used when creating many Tasks.

    Attributes:
        allow_defaults: Active overlap setting:
            * True — Use the overlap value that is set in the `defaults.default_overlap_for_new_task_suites` pool parameter.
            * False — Use the overlap value that is set in the `overlap` task suite parameter.
        open_pool: Open the pool immediately after creating a task suite, if the pool is closed.
        skip_invalid_items: Task validation option:
            * True — All valid tasks are added. If a task does not pass validation, then it is not added to Toloka. All such tasks are listed in the response.
            * False — If any task does not pass validation, then operation is cancelled and no tasks are added to Toloka.
        async_mode: Request processing mode:
            * True — Asynchronous operation is started internally and `create_tasks` waits for the completion of it. It is recommended to create no more than 10,000 tasks per request in this mode.
            * False — The request is processed synchronously. A maximum of 5000 tasks can be added in a single request in this mode.
    """

    def __init__(
        self,
        *,
        allow_defaults: typing.Optional[bool] = None,
        open_pool: typing.Optional[bool] = None,
        skip_invalid_items: typing.Optional[bool] = None,
        operation_id: typing.Optional[uuid.UUID] = None,
        async_mode: typing.Optional[bool] = True
    ) -> None:
        """Method generated by attrs for class CreateTasksParameters.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    allow_defaults: typing.Optional[bool]
    open_pool: typing.Optional[bool]
    skip_invalid_items: typing.Optional[bool]
    operation_id: typing.Optional[uuid.UUID]
    async_mode: typing.Optional[bool]


class TaskOverlapPatch(toloka.client.primitives.base.BaseTolokaObject):
    """Parameters for changing the overlap of a specific Task

    Attributes:
        overlap: Overlap value.
        infinite_overlap: Infinite overlap:
            * True — Assign the task to all users. It is useful for training tasks.
            * False — Overlap value specified for the task or for the pool is used. Default value: False.
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
    """Parameters for changing overlap or baseline_solutions of a specific Task

    Attributes:
        overlap: Overlap value.
        infinite_overlap: Infinite overlap:
            * True — Assign the task to all users. It is useful for training tasks.
            * False — Overlap value specified for the task or for the pool is used. Default value: False.
        baseline_solutions: Preliminary responses. This data simulates performer responses when calculating confidence in a response.
            It is used in dynamic overlap (also known as incremental relabeling or IRL) and aggregation of results by skill.
        known_solutions: Responses and hints for control tasks and training tasks. If multiple output fields are included
            in the validation, all combinations of the correct response must be specified.
        message_on_unknown_solution: Hint for the task (for training tasks).
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
