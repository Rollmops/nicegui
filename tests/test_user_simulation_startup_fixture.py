from typing import Callable

import pytest

from nicegui import ui
from nicegui.testing import User


@pytest.fixture
def user_startup() -> Callable:
    def custom_startup():
        @ui.page('/')
        def page():
            ui.label("Hello from my custom startup :-)")

        ui.run()

    return custom_startup


async def test_user_startup_fixture(user: User):
    await user.open("/")

    await user.should_see("Hello from my custom startup :-)")
