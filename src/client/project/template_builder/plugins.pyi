__all__ = [
    'BasePluginV1',
    'ImageAnnotationHotkeysPluginV1',
    'TextAnnotationHotkeysPluginV1',
    'HotkeysPluginV1',
    'TriggerPluginV1',
    'TolokaPluginV1',
]
import toloka.client.project.template_builder.base
import toloka.util._extendable_enum
import typing


class BasePluginV1(toloka.client.project.template_builder.base.BaseComponent, metaclass=toloka.client.project.template_builder.base.VersionedBaseComponentMetaclass):
    """A base class for plugins.
    """

    def __init__(self, *, version: typing.Optional[str] = '1.0.0') -> None:
        """Method generated by attrs for class BasePluginV1.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    version: typing.Optional[str]


class ImageAnnotationHotkeysPluginV1(BasePluginV1):
    """Hotkeys for the [ImageAnnotationFieldV1](toloka.client.project.template_builder.fields.ImageAnnotationFieldV1.md) component.

    For more information, see [plugin.field.image-annotation.hotkeys](https://toloka.ai/docs/template-builder/reference/plugin.field.image-annotation.hotkeys).

    Attributes:
        cancel: A hotkey for canceling area creation.
        confirm: A hotkey for confirming area creation.
        labels: A list of hotkeys for choosing area labels.
        modes: Hotkeys for switching selection modes.
    """

    class Mode(toloka.client.project.template_builder.base.BaseTemplate):
        """Selection mode hotkeys.

        Attributes:
            point: A hotkey for a point selection mode.
            polygon: A hotkey for a polygon selection mode.
            rectangle: A hotkey for a rectangle selection mode.
            select: A hotkey for a mode for editing selections.
        """

        def __init__(
            self,
            *,
            point: typing.Optional[str] = None,
            polygon: typing.Optional[str] = None,
            rectangle: typing.Optional[str] = None,
            select: typing.Optional[str] = None
        ) -> None:
            """Method generated by attrs for class ImageAnnotationHotkeysPluginV1.Mode.
            """
            ...

        _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
        point: typing.Optional[str]
        polygon: typing.Optional[str]
        rectangle: typing.Optional[str]
        select: typing.Optional[str]

    @typing.overload
    def __init__(
        self,
        *,
        cancel: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, str]] = None,
        confirm: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, str]] = None,
        labels: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, typing.List[str]]] = None,
        modes: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, Mode]] = None,
        version: typing.Optional[str] = '1.0.0'
    ) -> None:
        """Method generated by attrs for class ImageAnnotationHotkeysPluginV1.
        """
        ...

    @typing.overload
    def __init__(
        self,
        *,
        cancel: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, str]] = None,
        confirm: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, str]] = None,
        labels: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, typing.List[str]]] = None,
        point: typing.Optional[str] = None,
        polygon: typing.Optional[str] = None,
        rectangle: typing.Optional[str] = None,
        select: typing.Optional[str] = None,
        version: typing.Optional[str] = '1.0.0'
    ) -> None:
        """Method generated by attrs for class ImageAnnotationHotkeysPluginV1.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    version: typing.Optional[str]
    cancel: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, str]]
    confirm: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, str]]
    labels: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, typing.List[str]]]
    modes: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, Mode]]


class TextAnnotationHotkeysPluginV1(BasePluginV1):
    """Hotkeys for the [TextAnnotationFieldV1](toloka.client.project.template_builder.fields.TextAnnotationFieldV1.md) component.

    For more information, see [plugin.field.text-annotation.hotkeys](https://toloka.ai/docs/template-builder/reference/plugin.field.text-annotation.hotkeys).

    Attributes:
        labels: A list of hotkeys for choosing labels.
        remove: A hotkey for clearing the label of the annotated text.
    """

    def __init__(
        self,
        labels: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, typing.List[str]]] = None,
        remove: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, str]] = None,
        *,
        version: typing.Optional[str] = '1.0.0'
    ) -> None:
        """Method generated by attrs for class TextAnnotationHotkeysPluginV1.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    version: typing.Optional[str]
    labels: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, typing.List[str]]]
    remove: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, str]]


class HotkeysPluginV1(BasePluginV1):
    """Hotkeys for actions.

    You can use as hotkeys:
    * Letters
    * Numbers
    * Up and down arrows

    Choose a hotkey using a named parameter of the `HotkeysPluginV1` and assign an action to it.

    Example:
        Creating hotkeys for classification buttons.

        >>> hot_keys_plugin = tb.HotkeysPluginV1(
        >>>     key_1=tb.SetActionV1(tb.OutputData('result'), 'cat'),
        >>>     key_2=tb.SetActionV1(tb.OutputData('result'), 'dog'),
        >>>     key_3=tb.SetActionV1(tb.OutputData('result'), 'other'),
        >>> )
        ...
    """

    def __init__(
        self,
        *,
        key_a: typing.Optional[typing.Any] = None,
        key_b: typing.Optional[typing.Any] = None,
        key_c: typing.Optional[typing.Any] = None,
        key_d: typing.Optional[typing.Any] = None,
        key_e: typing.Optional[typing.Any] = None,
        key_f: typing.Optional[typing.Any] = None,
        key_g: typing.Optional[typing.Any] = None,
        key_h: typing.Optional[typing.Any] = None,
        key_i: typing.Optional[typing.Any] = None,
        key_j: typing.Optional[typing.Any] = None,
        key_k: typing.Optional[typing.Any] = None,
        key_l: typing.Optional[typing.Any] = None,
        key_m: typing.Optional[typing.Any] = None,
        key_n: typing.Optional[typing.Any] = None,
        key_o: typing.Optional[typing.Any] = None,
        key_p: typing.Optional[typing.Any] = None,
        key_q: typing.Optional[typing.Any] = None,
        key_r: typing.Optional[typing.Any] = None,
        key_s: typing.Optional[typing.Any] = None,
        key_t: typing.Optional[typing.Any] = None,
        key_u: typing.Optional[typing.Any] = None,
        key_v: typing.Optional[typing.Any] = None,
        key_w: typing.Optional[typing.Any] = None,
        key_x: typing.Optional[typing.Any] = None,
        key_y: typing.Optional[typing.Any] = None,
        key_z: typing.Optional[typing.Any] = None,
        key_0: typing.Optional[typing.Any] = None,
        key_1: typing.Optional[typing.Any] = None,
        key_2: typing.Optional[typing.Any] = None,
        key_3: typing.Optional[typing.Any] = None,
        key_4: typing.Optional[typing.Any] = None,
        key_5: typing.Optional[typing.Any] = None,
        key_6: typing.Optional[typing.Any] = None,
        key_7: typing.Optional[typing.Any] = None,
        key_8: typing.Optional[typing.Any] = None,
        key_9: typing.Optional[typing.Any] = None,
        key_up: typing.Optional[typing.Any] = None,
        key_down: typing.Optional[typing.Any] = None,
        version: typing.Optional[str] = '1.0.0'
    ) -> None:
        """Method generated by attrs for class HotkeysPluginV1.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    version: typing.Optional[str]
    key_a: typing.Optional[typing.Any]
    key_b: typing.Optional[typing.Any]
    key_c: typing.Optional[typing.Any]
    key_d: typing.Optional[typing.Any]
    key_e: typing.Optional[typing.Any]
    key_f: typing.Optional[typing.Any]
    key_g: typing.Optional[typing.Any]
    key_h: typing.Optional[typing.Any]
    key_i: typing.Optional[typing.Any]
    key_j: typing.Optional[typing.Any]
    key_k: typing.Optional[typing.Any]
    key_l: typing.Optional[typing.Any]
    key_m: typing.Optional[typing.Any]
    key_n: typing.Optional[typing.Any]
    key_o: typing.Optional[typing.Any]
    key_p: typing.Optional[typing.Any]
    key_q: typing.Optional[typing.Any]
    key_r: typing.Optional[typing.Any]
    key_s: typing.Optional[typing.Any]
    key_t: typing.Optional[typing.Any]
    key_u: typing.Optional[typing.Any]
    key_v: typing.Optional[typing.Any]
    key_w: typing.Optional[typing.Any]
    key_x: typing.Optional[typing.Any]
    key_y: typing.Optional[typing.Any]
    key_z: typing.Optional[typing.Any]
    key_0: typing.Optional[typing.Any]
    key_1: typing.Optional[typing.Any]
    key_2: typing.Optional[typing.Any]
    key_3: typing.Optional[typing.Any]
    key_4: typing.Optional[typing.Any]
    key_5: typing.Optional[typing.Any]
    key_6: typing.Optional[typing.Any]
    key_7: typing.Optional[typing.Any]
    key_8: typing.Optional[typing.Any]
    key_9: typing.Optional[typing.Any]
    key_up: typing.Optional[typing.Any]
    key_down: typing.Optional[typing.Any]


class TriggerPluginV1(BasePluginV1):
    """A plugin for triggering actions when events occur.

    For more information, see [plugin.trigger](https://toloka.ai/docs/template-builder/reference/plugin.trigger).

    Attributes:
        action: An action to trigger.
        condition: A condition that must be met in order to trigger the action.
        fire_immediately: If `True` then the action is triggered immediately after the task is loaded.
        on_change_of: The data change event that triggers the action.

    Example:
        How to save Toloker's coordinates.

        >>> coordinates_save_plugin = tb.plugins.TriggerPluginV1(
        >>>     fire_immediately=True,
        >>>     action=tb.actions.SetActionV1(
        >>>         data=tb.data.OutputData(path='toloker_coordinates'),
        >>>         payload=tb.data.LocationData()
        >>>     ),
        >>> )
        ...
    """

    def __init__(
        self,
        *,
        action: typing.Optional[toloka.client.project.template_builder.base.BaseComponent] = None,
        condition: typing.Optional[toloka.client.project.template_builder.base.BaseComponent] = None,
        fire_immediately: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, bool]] = None,
        on_change_of: typing.Optional[toloka.client.project.template_builder.base.BaseComponent] = None,
        version: typing.Optional[str] = '1.0.0'
    ) -> None:
        """Method generated by attrs for class TriggerPluginV1.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    version: typing.Optional[str]
    action: typing.Optional[toloka.client.project.template_builder.base.BaseComponent]
    condition: typing.Optional[toloka.client.project.template_builder.base.BaseComponent]
    fire_immediately: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, bool]]
    on_change_of: typing.Optional[toloka.client.project.template_builder.base.BaseComponent]


class TolokaPluginV1(BasePluginV1):
    """A plugin with extra settings for tasks in Toloka.

    For more information, see [plugin.toloka](https://toloka.ai/docs/template-builder/reference/plugin.toloka).

    Attributes:
        layout: Settings for the task appearance in Toloka.
        notifications: Notifications shown at the top of the page.

    Example:
        Setting the width of the task block on a page.

        >>> task_width_plugin = tb.plugins.TolokaPluginV1(
        >>>     kind='scroll',
        >>>     task_width=400,
        >>> )
        ...
    """

    class TolokaPluginLayout(toloka.client.project.template_builder.base.BaseTemplate):
        """A task block layout.
        """

        class Kind(toloka.util._extendable_enum.ExtendableStrEnum):
            """A task block layout mode.

            Attributes:
                SCROLL: All tasks from a task suite are displayed on a page. It is the default mode.
                PAGER: A single task is displayed on a page. Buttons at the bottom of the page show other tasks from a task suite.
            """

            PAGER = 'pager'
            SCROLL = 'scroll'

        def __init__(
            self,
            kind: typing.Optional[Kind] = None,
            *,
            task_width: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, float]] = None
        ) -> None:
            """Method generated by attrs for class TolokaPluginV1.TolokaPluginLayout.
            """
            ...

        _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
        kind: typing.Optional[Kind]
        task_width: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, float]]

    @typing.overload
    def __init__(
        self,
        layout: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, TolokaPluginLayout]] = ...,
        *,
        notifications: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, typing.List[toloka.client.project.template_builder.base.BaseComponent]]] = None,
        version: typing.Optional[str] = '1.0.0'
    ) -> None:
        """Method generated by attrs for class TolokaPluginV1.
        """
        ...

    @typing.overload
    def __init__(
        self,
        kind: typing.Optional[TolokaPluginLayout.Kind] = None,
        *,
        task_width: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, float]] = None,
        notifications: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, typing.List[toloka.client.project.template_builder.base.BaseComponent]]] = None,
        version: typing.Optional[str] = '1.0.0'
    ) -> None:
        """Method generated by attrs for class TolokaPluginV1.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    version: typing.Optional[str]
    layout: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, TolokaPluginLayout]]
    notifications: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, typing.List[toloka.client.project.template_builder.base.BaseComponent]]]
