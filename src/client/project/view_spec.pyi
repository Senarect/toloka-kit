__all__ = [
    'ViewSpec',
    'ClassicViewSpec',
    'TemplateBuilderViewSpec',
]
import toloka.client.primitives.base
import toloka.client.project.template_builder
import toloka.client.project.template_builder.base
import toloka.util._extendable_enum
import typing


class ViewSpec(toloka.client.primitives.base.BaseTolokaObject):
    """The description of a task interface.

    You can choose the type of description:
        * HTML, CSS, and JS — use [ClassicViewSpec](toloka.client.project.view_spec.ClassicViewSpec.md)
        * Template Builder components — use [TemplateBuilderViewSpec](toloka.client.project.view_spec.TemplateBuilderViewSpec.md)

    Args:
        settings: Common interface elements.
    """

    class Type(toloka.util._extendable_enum.ExtendableStrEnum):
        """A `ViewSpec` type.

        Attributes:
            CLASSIC: A task interface is defined with HTML, CSS and JS.
            TEMPLATE_BUILDER: A task interface is defined with the [TemplateBuilder](toloka.client.project.template_builder.TemplateBuilder.md) components.
        """

        CLASSIC = 'classic'
        TEMPLATE_BUILDER = 'tb'

    class Settings(toloka.client.primitives.base.BaseTolokaObject):
        """Common interface elements.

        Attributes:
            show_finish: Show the **Exit** button. The default is to show the button.
            show_fullscreen: Show the **Expand to fullscreen** button. The default is to show the button.
            show_instructions: Show the **Instructions** button. The default is to show the button.
            show_message: Show the **Message for the requester** button. The default is to show the button.
            show_reward: Show the price per task page. The default is to show the price.
            show_skip: Show the **Skip** button. The default is to show the button.
            show_submit: Show the **Submit** button. The default is to show the button.
            show_timer: Show the timer. The default is to show the timer.
            show_title: Show the project name on the top of a page. The default is to show the name.
        """

        def __init__(
            self,
            *,
            show_finish: typing.Optional[bool] = None,
            show_fullscreen: typing.Optional[bool] = None,
            show_instructions: typing.Optional[bool] = None,
            show_message: typing.Optional[bool] = None,
            show_reward: typing.Optional[bool] = None,
            show_skip: typing.Optional[bool] = None,
            show_submit: typing.Optional[bool] = None,
            show_timer: typing.Optional[bool] = None,
            show_title: typing.Optional[bool] = None
        ) -> None:
            """Method generated by attrs for class ViewSpec.Settings.
            """
            ...

        _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
        show_finish: typing.Optional[bool]
        show_fullscreen: typing.Optional[bool]
        show_instructions: typing.Optional[bool]
        show_message: typing.Optional[bool]
        show_reward: typing.Optional[bool]
        show_skip: typing.Optional[bool]
        show_submit: typing.Optional[bool]
        show_timer: typing.Optional[bool]
        show_title: typing.Optional[bool]

    def __init__(self, *, settings: typing.Optional[Settings] = None) -> None:
        """Method generated by attrs for class ViewSpec.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    settings: typing.Optional[Settings]


class ClassicViewSpec(ViewSpec):
    """A task interface defined with HTML, CSS and JS.

    For more information, see the [guide](https://toloka.ai/en/docs/guide/concepts/spec).

    Attributes:
        markup: HTML markup of the task interface.
        styles: CSS for the task interface.
        script: JavaScript code for the task interface.
        assets: Links to external files.
    """

    class Assets(toloka.client.primitives.base.BaseTolokaObject):
        """Links to external files.

        You can link:
            * CSS libraries
            * JavaScript libraries
            * Toloka assets — libraries that can be linked using the `$TOLOKA_ASSETS` path:
                * `$TOLOKA_ASSETS/js/toloka-handlebars-templates.js` — [Handlebars template engine](http://handlebarsjs.com/).
                * `$TOLOKA_ASSETS/js/image-annotation.js` — Image labeling interface. Note, that this library requires Handlebars and must be linked after it.
                    For more information, see [Image with area selection](https://toloka.ai/en/docs/guide/concepts/t-components/image-annotation).

            Add items in the order they should be linked.

        Attributes:
            style_urls: Links to CSS libraries.
            script_urls: Links to JavaScript libraries and Toloka assets.

        Examples:
            >>> from toloka.client.project.view_spec import ClassicViewSpec
            >>> view_spec = ClassicViewSpec(
            >>>     ...,
            >>>     assets = ClassicViewSpec.Assets(
            >>>         script_urls = [
            >>>             "$TOLOKA_ASSETS/js/toloka-handlebars-templates.js",
            >>>             "$TOLOKA_ASSETS/js/image-annotation.js",
            >>>         ]
            >>>     )
            >>> )
        """

        def __init__(
            self,
            *,
            style_urls: typing.Optional[typing.List[str]] = None,
            script_urls: typing.Optional[typing.List[str]] = None
        ) -> None:
            """Method generated by attrs for class ClassicViewSpec.Assets.
            """
            ...

        _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
        style_urls: typing.Optional[typing.List[str]]
        script_urls: typing.Optional[typing.List[str]]

    def __init__(
        self,
        *,
        settings: typing.Optional[ViewSpec.Settings] = None,
        script: typing.Optional[str] = None,
        markup: typing.Optional[str] = None,
        styles: typing.Optional[str] = None,
        assets: typing.Optional[Assets] = None
    ) -> None:
        """Method generated by attrs for class ClassicViewSpec.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    settings: typing.Optional[ViewSpec.Settings]
    script: typing.Optional[str]
    markup: typing.Optional[str]
    styles: typing.Optional[str]
    assets: typing.Optional[Assets]


class TemplateBuilderViewSpec(ViewSpec):
    """A task interface defined with the [TemplateBuilder](toloka.client.project.template_builder.TemplateBuilder.md).

    See also [Template Builder](https://toloka.ai/en/docs/template-builder/) in the guide.

    Attributes:
        view: A top level component like [SideBySideLayoutV1](toloka.client.project.template_builder.layouts.SideBySideLayoutV1.md).
        plugins: An array of plugins.
        vars: Reusable data. It is referenced with the [RefComponent](toloka.client.project.template_builder.base.RefComponent.md).
        core_version: The default template components version. Most likely, you do not need to change this parameter.
        infer_data_spec:
            * `True` – The specifications of input and output data are generated automatically depending on the task interface settings.
            * `False` – You configure the specifications manually, if:
                * You don't want the specification to be affected by changes in instructions or other project parameters.
                * You have to change automatically generated specifications to suite your needs.

    Example:
        Creating a simple interface based on [ListViewV1](toloka.client.project.template_builder.view.ListViewV1.md):

        >>> import toloka.client.project.template_builder as tb
        >>> project_interface = toloka.client.project.view_spec.TemplateBuilderViewSpec(
        >>>     view=tb.view.ListViewV1(
        >>>         items=[header, output_field, radiobuttons],
        >>>         validation=some_validation,
        >>>     ),
        >>>     plugins=[plugin1, plugin2]
        >>> )
        >>> # add 'project_interface' to 'toloka.project.Project' instance
        ...
    """

    def unstructure(self): ...

    @classmethod
    def structure(cls, data: dict): ...

    @typing.overload
    def __init__(
        self,
        *,
        settings: typing.Optional[ViewSpec.Settings] = None,
        config: typing.Optional[toloka.client.project.template_builder.TemplateBuilder] = None,
        core_version: typing.Optional[str] = '1.0.0',
        infer_data_spec: typing.Optional[bool] = False
    ) -> None:
        """Method generated by attrs for class TemplateBuilderViewSpec.
        """
        ...

    @typing.overload
    def __init__(
        self,
        *,
        settings: typing.Optional[ViewSpec.Settings] = None,
        view: typing.Optional[toloka.client.project.template_builder.base.BaseComponent] = None,
        plugins: typing.Optional[typing.List[toloka.client.project.template_builder.base.BaseComponent]] = None,
        vars: typing.Optional[typing.Dict[str, typing.Any]] = None,
        core_version: typing.Optional[str] = '1.0.0',
        infer_data_spec: typing.Optional[bool] = False
    ) -> None:
        """Method generated by attrs for class TemplateBuilderViewSpec.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    settings: typing.Optional[ViewSpec.Settings]
    config: typing.Optional[toloka.client.project.template_builder.TemplateBuilder]
    core_version: typing.Optional[str]
    infer_data_spec: typing.Optional[bool]
