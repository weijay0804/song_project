from contextlib import contextmanager
from datetime import datetime

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


def add_user(username: str, password: str, email: str, phone: str, is_vip: str = "0") -> None:
    with get_cursor() as cursor:
        cursor.execute(
            "INSERT INTO member(member_acc, password, mail, phone, isvip) VALUES(%s, %s, %s, %s, %s)",
            [username, password, email, phone, is_vip],
        )


def get_relation_singer(username: str, limit=7) -> list:
    """根據使用者的 love singer 取得曲風最多的歌手"""

    command = """
    SELECT s.singer, COUNT(s.singer) AS count_singer
    FROM love_singer AS l
    JOIN singer_relation AS s
    ON l.singer = s.singer
    WHERE l.member_acc = %s
    GROUP BY s.singer
    ORDER BY count_singer DESC
    LIMIT %s
    """

    with get_cursor() as cursor:
        cursor.execute(command, [username, limit])

        result = cursor.fetchall()

    return [s[0] for s in result]


def get_song_list(username: str, limit: int = 5) -> list:
    """取得使用者的歌曲清單"""

    command = """
    SELECT list_name, COUNT(song)
    FROM song_list
    WHERE member_acc = %s
    GROUP BY list_name
    LIMIT %s
    """

    with get_cursor() as cursor:
        cursor.execute(command, [username, limit])

        result = cursor.fetchall()

    if not result:
        return None

    data = [{"list_name": d[0], "count": d[1]} for d in result]

    return data


def get_user_sound(username: str, limit: int = 100) -> dict:
    """取得使用者的人聲資料"""

    command = """
    SELECT name, sound_name, time
    FROM sound
    WHERE member_acc = %s
    LIMIT %s
    """

    with get_cursor() as cursor:
        cursor.execute(command, [username, limit])

        result = cursor.fetchall()

    if not result:
        return None

    data = {}

    for r in result:
        if data.get(r[0]) is None:
            data[r[0]] = []

        data[r[0]].append({"sound_name": r[1], "time": r[2]})

    return data


def add_creation_song(username: str, song_name: str, data_name: str = None) -> None:
    """新增資料至 creation song table，如果沒有 `data_name` 參數，默認會是目前時間"""

    command = """
    INSERT INTO creation_song(song_name, member_acc, data_name, time)
    VALUES(%s, %s, %s, %s)
    """

    if data_name is None:
        data_name = datetime.now().strftime("%Y%m%d%H%M%S")

    with get_cursor() as cursor:
        cursor.execute(command, [song_name, username, data_name, datetime.now()])


def get_user_song_list_and_song(username: str) -> dict:
    """取得使用者收藏的歌曲清單和歌曲清單中的歌曲"""

    command = """
    SELECT
    list.song, list.list_name, song.singer, song.long
    FROM song_list AS list
    JOIN song ON list.song = song.name
    WHERE list.member_acc = %s
    """

    with get_cursor() as cursor:
        cursor.execute(command, [username])

        result = cursor.fetchall()

    if not result:
        return None

    data = {}

    for r in result:
        if data.get(r[1]) is None:
            data[r[1]] = []

        data[r[1]].append({"song_name": r[0], "singer": r[2], "song_time": r[3]})

    return data
