import collections
import os.path
import yaml


SOURCE_DIR = 'src'
TARGET_DIR = 'bin'


Rule = collections.namedtuple('Rule', ['rule', 'deps', 'coms'])


def load_config():
    with open('config.yaml') as fd:
        return yaml.load(fd)

def make_rule(target, dependency, commands):
    source_path = os.path.join(SOURCE_DIR, dependency)
    target_path = os.path.join(TARGET_DIR, target)
    cmd_string  = '\n\t'.join(commands).format(src=source_path, tgt=target_path)
    return Rule(target_path, source_path, cmd_string)

def process_config(config):
    print(config)
    for target, r in config['svg'].items():
        try:
            names = r['names']
        except KeyError:
            names = [target]
        for name in names:
            rule = name + '@2x.png'
            dep  = target + '.svg'
            coms = [
                'inkscape -f {{src}} -e {{tgt}} -w {} -h {}'.format(r['w'], r['h']),
            ]
            if r.get('fix', False):
                coms.append('python fix-antialias.py {{tgt}}'.format())
            yield make_rule(rule, dep, coms)
    for target, r in config['png'].items():
        try:
            names = r['names']
        except KeyError:
            names = [target]
        for name in names:
            rule = name   + '@2x.png'
            dep  = target + '.png'
            coms = ['cp {{src}} {{tgt}}'.format()]
            yield make_rule(rule, dep, coms)
    for target, r in config['ini'].items():
        rule = target + '.ini'
        dep  = rule
        coms = ['cp {{src}} {{tgt}}'.format()]
        yield make_rule(rule, dep, coms)


config = load_config()
rules = list(process_config(config))
rules.append(Rule('all', ' '.join(r.rule for r in rules), ''))
with open('Makefile', 'w') as fd:
    for r in reversed(rules):
        fd.write('{}: {}\n\t{}'.format(r.rule, r.deps, r.coms))
        fd.write('\n')
