"""User-defined exceptions"""


class BkrError(Exception):
    """Base exception for bkr package"""

    pass


class NotInTreeError(BkrError):
    """Thrown when user attempts bkr operation outside of working tree."""

    pass


class ConfigNotFoundError(BkrError):
    """Thrown when config file does not exist."""

    pass


class InvalidConfigError(BkrError):
    """Thrown when config file is not valid."""

    pass


class RecordExistsError(BkrError):
    """Thrown when bkr attempts to create record that already exists"""

    pass


class InitError(BkrError):
    """Thrown when 'bkr init' command fails"""

    pass
