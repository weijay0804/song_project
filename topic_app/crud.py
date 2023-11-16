from contextlib import contextmanager

from django.db import connection


@contextmanager
def get_cursor():
    cursor = connection.cursor()

    try:
        yield cursor
    finally:
        cursor.close()


def count_user_love_singers(username: str) -> int:
    with get_cursor() as cursor:
        cursor.execute("SELECT COUNT(sn) FROM love_singer WHERE member_acc = %s", [username])

        result = cursor.fetchall()[0][0]

    return result


def get_singers(limit: int = 100) -> list:
    with get_cursor() as cursor:
        cursor.execute("SELECT DISTINCT(singer) FROM singer_relation LIMIT %s", [limit])

        result = cursor.fetchall()

    return result


def add_user_love_singer(singer_list: list, username: str) -> None:
    data = [[d, username] for d in singer_list]

    with get_cursor() as cursor:
        cursor.executemany("INSERT INTO love_singer(singer, member_acc) VALUES(%s, %s)", data)


def get_user(username: str) -> dict:
    with get_cursor() as cursor:
        cursor.execute("SELECT member_acc, password FROM member WHERE member_acc=%s", (username))

        result = cursor.fetchone()

    if result is None:
        return None

    return {"member_acc": result[0], "password": result[-1]}


def add_user(username: str, password: str, email: str, is_vip: str = "1") -> None:
    with get_cursor() as cursor:
        cursor.execute(
            "INSERT INTO member(member_acc, password, mail, isvip) VALUES(%s, %s, %s, %s)",
            [username, password, email, is_vip],
        )