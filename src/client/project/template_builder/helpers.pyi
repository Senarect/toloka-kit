__all__ = [
    'BaseHelperV1',
    'ConcatArraysHelperV1',
    'Entries2ObjectHelperV1',
    'IfHelperV1',
    'JoinHelperV1',
    'Object2EntriesHelperV1',
    'ReplaceHelperV1',
    'SearchQueryHelperV1',
    'SwitchHelperV1',
    'TextTransformHelperV1',
    'TransformHelperV1',
    'TranslateHelperV1',
    'YandexDiskProxyHelperV1',
]
import toloka.client.project.template_builder.base
import toloka.util._extendable_enum
import typing


class BaseHelperV1(toloka.client.project.template_builder.base.BaseComponent, metaclass=toloka.client.project.template_builder.base.VersionedBaseComponentMetaclass):
    """A base class for helpers.
    """

    def __init__(self, *, version: typing.Optional[str] = '1.0.0') -> None:
        """Method generated by attrs for class BaseHelperV1.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    version: typing.Optional[str]


class ConcatArraysHelperV1(BaseHelperV1):
    """Concatenates multiple arrays into a single array.

    For more information, see [helper.concat-arrays](https://toloka.ai/docs/template-builder/reference/helper.concat-arrays).

    Attributes:
        items: Arrays to concatenate.
    """

    def __init__(
        self,
        items: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, typing.List[typing.Any]]] = None,
        *,
        version: typing.Optional[str] = '1.0.0'
    ) -> None:
        """Method generated by attrs for class ConcatArraysHelperV1.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    version: typing.Optional[str]
    items: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, typing.List[typing.Any]]]


class Entries2ObjectHelperV1(BaseHelperV1):
    """Creates an object from an array of key-value pairs.

    For example,
    `[ {"key":"foo", "value":"hello"}, {"key":"bar","value":"world"} ]`
    is converted to `{ "foo": "hello", "bar": "world" }`.

    For more information, see [helper.entries2object](https://toloka.ai/docs/template-builder/reference/helper.entries2object).

    Attributes:
        entries: A source array of key-value pairs.
    """

    class Entry(toloka.client.project.template_builder.base.BaseTemplate):
        def __init__(
            self,
            key: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, str]] = None,
            value: typing.Optional[typing.Any] = None
        ) -> None:
            """Method generated by attrs for class Entries2ObjectHelperV1.Entry.
            """
            ...

        _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
        key: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, str]]
        value: typing.Optional[typing.Any]

    def __init__(
        self,
        entries: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, typing.List[typing.Union[toloka.client.project.template_builder.base.BaseComponent, Entry]]]] = None,
        *,
        version: typing.Optional[str] = '1.0.0'
    ) -> None:
        """Method generated by attrs for class Entries2ObjectHelperV1.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    version: typing.Optional[str]
    entries: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, typing.List[typing.Union[toloka.client.project.template_builder.base.BaseComponent, Entry]]]]


class IfHelperV1(BaseHelperV1):
    """The `if then else` operator.

    For more information, see [helper.if](https://toloka.ai/docs/template-builder/reference/helper.if).

    Attributes:
        condition: A condition to check.
        then: A component that is returned if the condition is `True`.
        else_: A component that is returned if the condition is `False`.

    Example:
        How to conditionally show a part of the interface.

        >>> hidden_ui = tb.helpers.IfHelperV1(
        >>>     condition=tb.conditions.EqualsConditionV1(tb.data.OutputData('show_me'), 'show'),
        >>>     then=tb.view.ListViewV1([header, buttons, images]),
        >>> )
        ...
    """

    def __init__(
        self,
        condition: typing.Optional[toloka.client.project.template_builder.base.BaseComponent] = None,
        then: typing.Optional[typing.Any] = None,
        *,
        else_: typing.Optional[typing.Any] = None,
        version: typing.Optional[str] = '1.0.0'
    ) -> None:
        """Method generated by attrs for class IfHelperV1.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    version: typing.Optional[str]
    condition: typing.Optional[toloka.client.project.template_builder.base.BaseComponent]
    then: typing.Optional[typing.Any]
    else_: typing.Optional[typing.Any]


class JoinHelperV1(BaseHelperV1):
    """Joins strings into a single string.

    For more information, see [helper.join](https://toloka.ai/docs/template-builder/reference/helper.join).

    Attributes:
        items: A list of strings to join.
        by: A delimiter. You can use any number of characters in the delimiter.
    """

    def __init__(
        self,
        items: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, typing.List[typing.Union[toloka.client.project.template_builder.base.BaseComponent, str]]]] = None,
        by: typing.Optional[typing.Any] = None,
        *,
        version: typing.Optional[str] = '1.0.0'
    ) -> None:
        """Method generated by attrs for class JoinHelperV1.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    version: typing.Optional[str]
    items: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, typing.List[typing.Union[toloka.client.project.template_builder.base.BaseComponent, str]]]]
    by: typing.Optional[typing.Any]


class Object2EntriesHelperV1(BaseHelperV1):
    """Creates an array of key-value pairs from an object.

    For example,
    `{ "foo": "hello", "bar": "world" }` is converted to
    `[ {"key":"foo", "value":"hello"}, {"key":"bar","value":"world"} ]`.

    For more information, see [helper.object2entries](https://toloka.ai/docs/template-builder/reference/helper.object2entries).

    Attributes:
        data: An object to convert.
    """

    def __init__(
        self,
        data: typing.Optional[typing.Any] = None,
        *,
        version: typing.Optional[str] = '1.0.0'
    ) -> None:
        """Method generated by attrs for class Object2EntriesHelperV1.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    version: typing.Optional[str]
    data: typing.Optional[typing.Any]


class ReplaceHelperV1(BaseHelperV1):
    """Replaces a substring in a string.

    For more information, see [helper.replace](https://toloka.ai/docs/template-builder/reference/helper.replace).

    Attributes:
        data: An input string.
        find: A substring to look for.
        replace: A substring to replace with.
    """

    def __init__(
        self,
        data: typing.Optional[typing.Any] = None,
        find: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, str]] = None,
        replace: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, str]] = None,
        *,
        version: typing.Optional[str] = '1.0.0'
    ) -> None:
        """Method generated by attrs for class ReplaceHelperV1.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    version: typing.Optional[str]
    data: typing.Optional[typing.Any]
    find: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, str]]
    replace: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, str]]


class SearchQueryHelperV1(BaseHelperV1):
    """Creates a query for a search engine.

    For more information, see [helper.search-query](https://toloka.ai/docs/template-builder/reference/helper.search-query).

    Attributes:
        query: A query.
        engine: A search engine.
    """

    class Engine(toloka.util._extendable_enum.ExtendableStrEnum):
        """An enumeration.
        """

        YANDEX = 'yandex'
        GOOGLE = 'google'
        BING = 'bing'
        MAILRU = 'mail.ru'
        WIKIPEDIA = 'wikipedia'
        YANDEX_COLLECTIONS = 'yandex/collections'
        YANDEX_VIDEO = 'yandex/video'
        YANDEX_IMAGES = 'yandex/images'
        GOOGLE_IMAGES = 'google/images'
        YANDEX_NEWS = 'yandex/news'
        GOOGLE_NEWS = 'google/news'

    def __init__(
        self,
        query: typing.Optional[typing.Any] = None,
        engine: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, Engine]] = None,
        *,
        version: typing.Optional[str] = '1.0.0'
    ) -> None:
        """Method generated by attrs for class SearchQueryHelperV1.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    version: typing.Optional[str]
    query: typing.Optional[typing.Any]
    engine: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, Engine]]


class SwitchHelperV1(BaseHelperV1):
    """Chooses one variant from multiple cases.

    For more information, see [helper.switch](https://toloka.ai/docs/template-builder/reference/helper.switch).

    Attributes:
        cases: A list of cases.
            A case consists of a condition and a resulting component.
        default: A component that is returned if none of the conditions is `True`.
    """

    class Case(toloka.client.project.template_builder.base.BaseTemplate):
        """A case for the `SwitchHelperV1`.

        Attributes:
            condition: A case condition.
            result: A component that is returned if the condition is `True`.
        """

        def __init__(
            self,
            condition: typing.Optional[toloka.client.project.template_builder.base.BaseComponent] = None,
            result: typing.Optional[typing.Any] = None
        ) -> None:
            """Method generated by attrs for class SwitchHelperV1.Case.
            """
            ...

        _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
        condition: typing.Optional[toloka.client.project.template_builder.base.BaseComponent]
        result: typing.Optional[typing.Any]

    def __init__(
        self,
        cases: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, typing.List[typing.Union[toloka.client.project.template_builder.base.BaseComponent, Case]]]] = None,
        default: typing.Optional[typing.Any] = None,
        *,
        version: typing.Optional[str] = '1.0.0'
    ) -> None:
        """Method generated by attrs for class SwitchHelperV1.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    version: typing.Optional[str]
    cases: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, typing.List[typing.Union[toloka.client.project.template_builder.base.BaseComponent, Case]]]]
    default: typing.Optional[typing.Any]


class TextTransformHelperV1(BaseHelperV1):
    """Converts a text to uppercase, lowercase, or capitalize it.

    For more information, see [helper.text-transform](https://toloka.ai/docs/template-builder/reference/helper.text-transform).

    Attributes:
        data: A text to convert.
        transformation: A conversion mode:
            * `uppercase` — Makes all letters uppercase.
            * `lowercase` — Makes all letters lowercase.
            * `capitalize` — Capitalizes the first letter in the text, and leaves the rest lowercase. Note, that if there are several sentences, the rest of them are not capitalized.
    """

    class Transformation(toloka.util._extendable_enum.ExtendableStrEnum):
        """An enumeration.
        """

        UPPERCASE = 'uppercase'
        LOWERCASE = 'lowercase'
        CAPITALIZE = 'capitalize'

    def __init__(
        self,
        data: typing.Optional[typing.Any] = None,
        transformation: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, Transformation]] = None,
        *,
        version: typing.Optional[str] = '1.0.0'
    ) -> None:
        """Method generated by attrs for class TextTransformHelperV1.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    version: typing.Optional[str]
    data: typing.Optional[typing.Any]
    transformation: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, Transformation]]


class TransformHelperV1(BaseHelperV1):
    """Creates a new array by transforming elements of another array.

    For example, you can create an array of `view.image` components from an array of links to images.

    For more information, see [helper.transform](https://toloka.ai/docs/template-builder/reference/helper.transform).

    Attributes:
        into: The template of an element of the new array.
            To insert values from the source array use the [LocalData](toloka.client.project.template_builder.data.LocalData.md) component with the data `path` set to `item`.
        items: The source array.
    """

    def __init__(
        self,
        into: typing.Optional[typing.Any] = None,
        items: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, typing.List[typing.Any]]] = None,
        *,
        version: typing.Optional[str] = '1.0.0'
    ) -> None:
        """Method generated by attrs for class TransformHelperV1.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    version: typing.Optional[str]
    into: typing.Optional[typing.Any]
    items: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, typing.List[typing.Any]]]


class TranslateHelperV1(BaseHelperV1):
    """A component for translating interface elements to other languages.

    For more information, see [helper.translate](https://toloka.ai/docs/template-builder/reference/helper.translate).

    Attributes:
        key: The key of a phrase that has translations.
    """

    def __init__(
        self,
        key: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, str]] = None,
        *,
        version: typing.Optional[str] = '1.0.0'
    ) -> None:
        """Method generated by attrs for class TranslateHelperV1.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    version: typing.Optional[str]
    key: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, str]]


class YandexDiskProxyHelperV1(BaseHelperV1):
    """A component for downloading files from Yandex&#160;Disk.

    For more information, see [helper.proxy](https://toloka.ai/docs/template-builder/reference/helper.proxy).

    Attributes:
        path: A path to a file in the `/<Proxy name>/<File name>.<type>` format.
    """

    def __init__(
        self,
        path: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, str]] = None,
        *,
        version: typing.Optional[str] = '1.0.0'
    ) -> None:
        """Method generated by attrs for class YandexDiskProxyHelperV1.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    version: typing.Optional[str]
    path: typing.Optional[typing.Union[toloka.client.project.template_builder.base.BaseComponent, str]]
