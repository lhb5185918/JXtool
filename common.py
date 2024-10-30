import pymysql
from pypinyin import lazy_pinyin
import yaml
import os
import sys


def base_path(path):
    if getattr(sys, 'frozen', None):
        basedir = sys._MEIPASS
    else:
        basedir = os.path.dirname(__file__)
    return os.path.join(basedir, path)


# import yaml
# import os


def chinese_to_initials(text):
    initials = lazy_pinyin(text)
    first_letters = [word[0].upper() for word in initials]
    return ''.join(first_letters)


class CommonDatabase():
    # ... existing code ...

    def config(self, key=None, value=None, update=None):
        self.database_config = {
            'host': read_yaml(base_path('config.yaml'), 'databaseconfig', 'host'),
            'user': read_yaml(base_path('config.yaml'), 'databaseconfig', 'user'),
            'password': read_yaml(base_path('config.yaml'), 'databaseconfig', 'password'),
            'db': read_yaml(base_path('config.yaml'), 'databaseconfig', 'db'),
            'charset': read_yaml(base_path('config.yaml'), 'databaseconfig', 'charset'),
            'port': read_yaml(base_path('config.yaml'), 'databaseconfig', 'port'),
        }
        if update is None:
            return self.database_config
        else:
            self.database_config.update({key: value})
            return self.database_config
        # ... existing code ...

    def select_data(self, value, table_name, condition=None):
        self.conn = pymysql.connect(
            host=self.config()['host'],
            user=self.config()['user'],
            password=self.config()['password'],
            db=self.config()['db'],
            charset=self.config()['charset'],
            port=self.config()['port'],
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        try:
            if condition is not None:
                sql = f"select {value} from {table_name} where {condition}"
            else:
                sql = f"select {value} from {table_name}"
            self.cursor.execute(sql)
            self.conn.close()
            return self.cursor.fetchone()
        except Exception as e:
            return e


def strip_control(text):
    # 去掉前面的空格
    text = text.lstrip()

    # 去掉后面的空格
    text = text.rstrip()
    return text


def read_yaml(file_path, key=None, value=None):
    with open(file_path, 'r', encoding="utf-8") as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
        if key is None:
            return data
        else:
            if value is None:
                return data[key]
            else:
                for item in data[key]:
                    if value is None:
                        return item
                    else:
                        return item[value]


def write_yaml(file_path, moudle_name, key, value):
    # 读取YAML文件
    with open(file_path, 'r', encoding="utf-8") as file:
        data = yaml.safe_load(file)

    # 遍历数据并修改指定的字段
    for item in data[moudle_name]:
        if key in item:
            item[key] = value

    # 将修改后的内容写回到YAML文件中
    with open(file_path, 'w', encoding="utf-8") as file:
        yaml.safe_dump(data, file, default_flow_style=False, allow_unicode=True)
    return data

