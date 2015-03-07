import os.path
import yaml


SOURCE_DIR = 'src'
TARGET_DIR = 'bin'


def load_config():
    with open('config.yaml') as fd:
        return yaml.load(fd)

def make_rule(target, dependency, commands):
    source_path = os.path.join(SOURCE_DIR, dependency)
    target_path = os.path.join(TARGET_DIR, target)
    cmd_string  = '\n\t'.join(commands).format(src=source_path, tgt=target_path)
    return '{}: {}\n\t{}'.format(target_path, source_path, cmd_string)

def process_config(config):
    print(config)
    for target, r in config['svg'].items():
        rule = target + '@2x.png'
        dep  = target + '.svg'
        coms = [
            'inkscape -f {{src}} -e {{tgt}} -w {} -h {}'.format(r['w'], r['h']),
            'python fix-antialias.py {{tgt}}'.format(),
        ]
        yield make_rule(rule, dep, coms)


config = load_config()
makefile = '\n'.join(process_config(config))
with open('Makefile', 'w') as fd:
    fd.write(makefile)
    fd.write('\n')
