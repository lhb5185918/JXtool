from common import read_yaml, base_path


print(base_path("config.yaml"))

print(read_yaml(file_path=base_path("config.yaml"),key="databaseconfig",value="host"))
