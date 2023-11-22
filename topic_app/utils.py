from datetime import datetime
import shutil
import os

from topic import settings


def get_user_data_root() -> str:
    """取得 static/user_data folder path"""

    return os.path.join(settings.STATICFILES_DIRS[0], "user_data")


def get_user_data_folder(username: str) -> str:
    """取得使用者的 user_data folder"""

    user_data_root = get_user_data_root()

    return os.path.join(user_data_root, username)


def create_user_data_folder(username: str) -> None:
    """建立以 username 為名的 user_data folder"""

    if os.path.exists(get_user_data_folder(username)):
        return

    os.mkdir(get_user_data_folder(username))


def copy_auido_file(username: str, file_name: str) -> None:
    """將示範用的音檔 copy 到指定的 username 的 user_data folder 中"""

    auido_path = os.path.join(settings.BASE_DIR, "test_audio.mp3")
    user_folder_path = os.path.join(get_user_data_folder(username), file_name)

    if os.path.exists(user_folder_path):
        return

    shutil.copyfile(auido_path, user_folder_path)


def get_current_time() -> str:
    """取得格式為 YYYYMMDDHHMMSS 格式的目前時間"""

    return datetime.now().strftime("%Y%m%d%H%M%S")
