from . import client
from .sorting import sort_by_name

from .cache import cache


@cache
def all():
    """
    Return all person listed in database.
    """
    return sort_by_name(client.fetch_all("persons"))


@cache
def get_person_by_desktop_login(desktop_login):
    """
    Returns person corresponding to given login.
    """
    return client.fetch_first("persons?desktop_login=%s" % desktop_login)


@cache
def get_person_by_full_name(full_name):
    """
    Returns person corresponding to given name.
    """
    first_name, last_name = full_name.lower().split(" ")
    for person in all():
        is_right_first_name = first_name == person["first_name"].lower()
        is_right_last_name = last_name == person["last_name"].lower()
        if is_right_first_name and is_right_last_name:
            return person


@cache
def get_simple_person_list():
    """
    Person list with very few information, accessible without manager or admin
    rights.
    """
    return sort_by_name(client.get("auth/person-list"))
