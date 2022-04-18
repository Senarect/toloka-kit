__all__ = [
    'RuleType',
    'RuleAction',
    'Restriction',
    'RestrictionV2',
    'SetSkillFromOutputField',
    'ChangeOverlap',
    'SetSkill',
    'RejectAllAssignments',
    'ApproveAllAssignments'
]
from enum import unique

from .conditions import RuleConditionKey
from .primitives.base import BaseParameters
from .user_restriction import DurationUnit, UserRestriction
from ..util._codegen import attribute
from ..util._extendable_enum import ExtendableStrEnum


@unique
class RuleType(ExtendableStrEnum):
    RESTRICTION = 'RESTRICTION'
    RESTRICTION_V2 = 'RESTRICTION_V2'
    SET_SKILL_FROM_OUTPUT_FIELD = 'SET_SKILL_FROM_OUTPUT_FIELD'
    CHANGE_OVERLAP = 'CHANGE_OVERLAP'
    SET_SKILL = 'SET_SKILL'
    REJECT_ALL_ASSIGNMENTS = 'REJECT_ALL_ASSIGNMENTS'
    APPROVE_ALL_ASSIGNMENTS = 'APPROVE_ALL_ASSIGNMENTS'


class RuleAction(BaseParameters, spec_enum=RuleType, spec_field='type'):
    """Base class for all actions in quality controls configurations
    """

    pass


class Restriction(RuleAction, spec_value=RuleType.RESTRICTION):
    """Restricts performer's access to projects or pools.

    To have better control over restriction period use `RestrictionV2`.

    Attributes:
        parameters.scope:
            * `POOL` - A performer can not access the pool if the action is applied. In this case the performer's rating is not affected.
            * `PROJECT` - A performer can not access the entire project containing the pool. The performer's rating is affected.
            * `ALL_PROJECTS` - A performer can not access any customer's project.
        parameters.duration_days: Blocking period in days. By default, the block is permanent.
        parameters.private_comment: A private comment. It is visible only for the customer.
    """

    class Parameters(RuleAction.Parameters):
        scope: UserRestriction.Scope = attribute(autocast=True)
        duration_days: int
        private_comment: str


class RestrictionV2(RuleAction, spec_value=RuleType.RESTRICTION_V2):
    """Restricts performer's access to projects or pools.

    Attributes:
        parameters.scope:
            * `POOL` - A performer can not access the pool if the action is applied. In this case the performer's rating is not affected.
            * `PROJECT` - A performer can not access the entire project containing the pool. The performer's rating is affected.
            * `ALL_PROJECTS` - A performer can not access any customer's project.
        parameters.duration: The duration of the block period measured in `duration_unit`.
        parameters.duration_unit: 
            * `MINUTES`;
            * `HOURS`;
            * `DAYS`;
            * `PERMANENT`.
            `PERMANENT` means that block is is permanent.
        parameters.private_comment: A private comment. It is visible only for the customer.

    Example:
        The following quality control rule disallows access to the project for 10 days, if a performer answers too fast.

        >>> new_pool = toloka.pool.Pool(....)
        >>> new_pool.quality_control.add_action(
        >>>     collector=toloka.collectors.AssignmentSubmitTime(history_size=5, fast_submit_threshold_seconds=20),
        >>>     conditions=[toloka.conditions.FastSubmittedCount > 1],
        >>>     action=toloka.actions.RestrictionV2(
        >>>         scope='PROJECT',
        >>>         duration=10,
        >>>         duration_unit='DAYS',
        >>>         private_comment='Fast responses',
        >>>     )
        >>> )
        ...
    """

    class Parameters(RuleAction.Parameters):
        scope: UserRestriction.Scope = attribute(autocast=True)
        duration: int
        duration_unit: DurationUnit = attribute(autocast=True)
        private_comment: str


class SetSkillFromOutputField(RuleAction, spec_value=RuleType.SET_SKILL_FROM_OUTPUT_FIELD):
    """Sets performer's skill value to the percentage of correct or incorrect answers.

    This action can be used with [collectors.MajorityVote](https://toloka.ai/en/docs/toloka-kit/reference/toloka.client.collectors.MajorityVote) and [collectors.GoldenSet](https://toloka.ai/en/docs/toloka-kit/reference/toloka.client.collectors.GoldenSet).

    Attributes:
        parameters.skill_id: ID of the skill to update.
        parameters.from_field: The value to assign to the skill:
            * `correct_answers_rate` - Percentage of correct answers.
            * `incorrect_answers_rate` - Percentage of incorrect answers.

    Example:
        In the following example `MajorityVote` is used to update a skill value.

        >>> new_pool = toloka.pool.Pool(....)
        >>> new_pool.quality_control.add_action(
        >>>     collector=toloka.collectors.MajorityVote(answer_threshold=2, history_size=10),
        >>>     conditions=[
        >>>         toloka.conditions.TotalAnswersCount > 2,
        >>>     ],
        >>>     action=toloka.actions.SetSkillFromOutputField(
        >>>         skill_id=some_skill_id,
        >>>         from_field='correct_answers_rate',
        >>>     ),
        >>> )
        ...
    """

    class Parameters(RuleAction.Parameters):
        skill_id: str
        from_field: RuleConditionKey = attribute(autocast=True)


class ChangeOverlap(RuleAction, spec_value=RuleType.CHANGE_OVERLAP):
    """Increases the overlap of a task.

    You can use this rule only with [collectors.UsersAssessment](https://toloka.ai/en/docs/toloka-kit/reference/toloka.client.collectors.UsersAssessment) and [collectors.AssignmentsAssessment](https://toloka.ai/en/docs/toloka-kit/reference/toloka.client.collectors.AssignmentsAssessment).

    Attributes:
        parameters.delta: An overlap increment.
        parameters.open_pool:
            * True — Open the pool after changing the overlap value.
            * False — Do not open the pool if it is already closed.

    Example:
        The example shows, how to increase task overlap when you reject assignments manually.

        >>> new_pool = toloka.pool.Pool(....)
        >>> new_pool.quality_control.add_action(
        >>>     collector=toloka.collectors.AssignmentsAssessment(),
        >>>     conditions=[toloka.conditions.AssessmentEvent == toloka.conditions.AssessmentEvent.REJECT],
        >>>     action=toloka.actions.ChangeOverlap(delta=1, open_pool=True),
        >>> )
        ...
    """

    class Parameters(RuleAction.Parameters):
        delta: int
        open_pool: bool


class SetSkill(RuleAction, spec_value=RuleType.SET_SKILL):
    """Sets performer's skill value.

    Attributes:
        parameters.skill_id: The ID of the skill.
        parameters.skill_value: The new value of the skill.

    Example:
        When an answer is accepted, assign a skill to the performer. Later you can filter performers by that skill.

        >>> new_pool = toloka.pool.Pool(....)
        >>> new_pool.quality_control.add_action(
        >>>     collector=toloka.collectors.AnswerCount(),
        >>>     conditions=[toloka.conditions.AssignmentsAcceptedCount > 0],
        >>>     action=toloka.actions.SetSkill(skill_id=some_skill_id, skill_value=1),
        >>> )
        ...
    """

    class Parameters(RuleAction.Parameters):
        skill_id: str
        skill_value: int


class RejectAllAssignments(RuleAction, spec_value=RuleType.REJECT_ALL_ASSIGNMENTS):
    """Rejects all performer's assignments in the pool. This action is available for pools with non-automatic acceptance.

    The performer is not explicitly installed, the rejection occurs on the performer on which the rule will be triggered.

    Attributes:
        parameters.public_comment: The reason of the rejection. It is visible to the customer and to the performer.

    Example:
        Reject all assignments if a performer sends responses too fast. Note, that the pool must be configured with non-automatic response acceptance.

        >>> new_pool = toloka.pool.Pool(....)
        >>> new_pool.quality_control.add_action(
        >>>     collector=toloka.collectors.AssignmentSubmitTime(history_size=5, fast_submit_threshold_seconds=20),
        >>>     conditions=[toloka.conditions.FastSubmittedCount > 3],
        >>>     action=toloka.actions.RejectAllAssignments(public_comment='Too fast responses.')
        >>> )
        ...
    """

    class Parameters(RuleAction.Parameters):
        public_comment: str


class ApproveAllAssignments(RuleAction, spec_value=RuleType.APPROVE_ALL_ASSIGNMENTS):
    """Accepts all performer's assignments in the pool.

    The performer is not explicitly installed, the approval occurs on the performer on which the rule will be triggered.

    Example:
        Accept all assignments if a performer gives correct responses for golden tasks. Note, that the pool must be configured with non-automatic response acceptance.

        >>> new_pool = toloka.pool.Pool(....)
        >>> new_pool.quality_control.add_action(
        >>>     collector=toloka.collectors.GoldenSet(history_size=5),
        >>>     conditions=[toloka.conditions.GoldenSetCorrectAnswersRate > 90],
        >>>     action=toloka.actions.ApproveAllAssignments()
        >>> )
        ...
    """

    pass
