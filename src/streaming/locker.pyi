__all__ = [
    'BaseLocker',
    'FileLocker',
    'NewerInstanceDetectedError',
    'ZooKeeperLocker',
]
import filelock._api
import kazoo.client  # type: ignore
import typing


class NewerInstanceDetectedError(Exception):
    """Exception being thrown in case of new concurrent pipeline was detected.
    Used to safely restore a process from a storage.
    """


class BaseLocker:
    def cleanup(self, lock: typing.Any) -> None: ...


class BaseSequentialIdLocker(BaseLocker):
    def __init__(self) -> None:
        """Method generated by attrs for class BaseSequentialIdLocker.
        """
        ...

    _id: typing.Optional[int]


class FileLocker(BaseSequentialIdLocker):
    """Simplest filesystem-based locker to use with a storage.

    Two locks cannot be taken simultaneously with the same key.
    If the instance detects that the lock was taken by a newer version, it throws an error.

    Attributes:
        dirname: Directory to store lock files ending with ".lock" and ".lock.content".
        timeout: Time in seconds to wait in case of lock being already acquired. Infinite by default.

    Example:
        Try to lock the same key at the same time..

        >>> locker_1 = FileLocker()
        >>> locker_2 = FileLocker(timeout=0)
        >>> with locker_1('some_key') as lock_1:
        ...     with locker_2('some_key') as lock_2:  # => raise an error: timeout
        ...         pass
        ...

        Try to lock the same key sequentially.

        >>> locker_1 = FileLocker()
        >>> locker_2 = FileLocker()
        >>> with locker_1('some_key'):
        ...     pass
        >>> with locker_2('some_key'):
        ...     pass
        >>> with locker_1('some_key'):  # raise an error: NewerInstanceDetectedError
        ...     pass
        ...
    """

    def cleanup(self, lock: filelock._api.BaseFileLock) -> None: ...

    def __init__(
        self,
        dirname: str = '/tmp',
        timeout: typing.Optional[int] = None
    ) -> None:
        """Method generated by attrs for class FileLocker.
        """
        ...

    _id: typing.Optional[int]
    dirname: str
    timeout: typing.Optional[int]


class ZooKeeperLocker(BaseSequentialIdLocker):
    """Apache ZooKeeper-based locker to use with a storage. Requires toloka-kit[zookeeper] extras.

    Two locks cannot be taken simultaneously with the same key.
    If the instance detects that the lock was taken by a newer version, it throws an error.

    Attributes:
        client: KazooClient object.
        dirname: Base node path to put locks in.
        timeout: Time in seconds to wait in case of lock being already acquired. Infinite by default.
        identifier: Optional lock identifier.

    Example:
        Create lock object.

        >>> !pip install toloka-kit[zookeeper]
        >>> from kazoo.client import KazooClient
        >>> zk = KazooClient('127.0.0.1:2181')
        >>> zk.start()
        >>> locker = ZooKeeperLocker(zk, '/my-locks')

        Try to lock the same key at the same time..

        >>> locker_1 = ZooKeeperLocker(zk, '/locks')
        >>> locker_2 = ZooKeeperLocker(zk, '/locks', timeout=0)
        >>> with locker_1('some_key') as lock_1:
        ...     with locker_2('some_key') as lock_2:  # => raise an error: timeout
        ...         pass
        ...

        Try to lock the same key sequentially.

        >>> locker_1 = ZooKeeperLocker(zk, '/locks')
        >>> locker_2 = ZooKeeperLocker(zk, '/locks')
        >>> with locker_1('some_key'):
        ...     pass
        >>> with locker_2('some_key'):
        ...     pass
        >>> with locker_1('some_key'):  # raise an error: NewerInstanceDetectedError
        ...     pass
        ...
    """

    def __init__(
        self,
        client: kazoo.client.KazooClient,
        dirname: str,
        timeout: typing.Optional[int] = None,
        identifier: str = 'lock'
    ) -> None:
        """Method generated by attrs for class ZooKeeperLocker.
        """
        ...

    _id: typing.Optional[int]
    client: kazoo.client.KazooClient
    dirname: str
    timeout: typing.Optional[int]
    identifier: str
