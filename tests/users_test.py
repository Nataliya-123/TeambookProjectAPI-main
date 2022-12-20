import pytest
from API.api import Teambook

us = Teambook()


def test_login():
    token = us.login()
    assert token


def test_get_user():
    status = us.get_user()
    assert status == 200


def test_create_user():
    my_id = us.create_user()
    assert my_id, int


# '''Периодически падает, если много реинвайтов отправлять'''
# @pytest.mark.xpass
# def test_re_invite_user():
#     status = us.re_invite_user()
#     assert status == 201


def test_get_user_exist():
    status = us.get_user_exists()
    assert status == 200


def test_get_user_deactivate():
    status = us.get_user_deactivate()
    assert status == 200
