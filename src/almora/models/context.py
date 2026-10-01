from dataclasses import dataclass
from almora.infrastructure.filesystem import AppFileSystem, get_root_path
from rich.console import Console
from pathlib import Path


class SessionContext:
    def __init__(self):
        self.root_path: Path = get_root_path()
        self.app_path: AppFileSystem = AppFileSystem()
        self.console: Console | None = None
        self.log = None
        self.cli_args = None
        self.cwd = None
        self.current_process = None
        self.log_debug: bool = False
        self.yes: bool = False
        self.start_time = None
        self.user_context: UserContext | None = None


@dataclass
class UserContext:
    _is_logged_in: bool = False
    _user_id: str | None = None
    _username: str | None = None

    @property
    def is_logged_in(self) -> bool:
        return self._is_logged_in

    @is_logged_in.setter
    def is_logged_in(self, value: bool):
        if type(value) is not bool:
            raise TypeError(f"is_logged_in must be bool")

        if value:
            self._is_logged_in = True
        else:
            self._is_logged_in = False
            self._user_id = None
            self._username = None

    @property
    def user_id(self) -> str:
        return self._user_id

    @user_id.setter
    def user_id(self, value: str):
        if self._user_id is not None:
            raise AttributeError(f"user_id is already set. It cannot be changed.")
        if type(value) is not str:
            raise TypeError(f"user_id must be str")
        if not self._is_logged_in:
            raise AttributeError(f"Not is_logged_in. user_id cannot be set")
        self._user_id = value

    @property
    def username(self) -> str:
        return self._username

    @username.setter
    def username(self, value: str):
        if self._username is not None:
            raise AttributeError(f"username is already set. It cannot be changed.")
        if type(value) is not str:
            raise TypeError(f"username must be str")
        if not self._is_logged_in:
            raise AttributeError(f"Not is_logged_in. user_id cannot be set")
        self._username = value