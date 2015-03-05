import os
import os.path
import shutil
import yaml


SOURCE_DIR = 'src'
TARGET_DIR = '.'


def copy(source, *targets):
    for target in targets:
        shutil.copyfile(source, target)

def load_config():
    with open('config.yaml') as fd:
        return yaml.load(fd)


config = load_config()
print(config)

for k, v in config['mapping'].items():
    source = os.path.join(SOURCE_DIR, k +'.png')
    if type(v) == str:
        vs = [v]
    else:
        vs = v
    targets = [os.path.join(TARGET_DIR, target + '@2x.png') for target in vs]
    copy(source, *targets)
