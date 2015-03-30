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

def process_svg(target, r):
    try:
        names = r['names']
    except KeyError:
        names = [target]
    rule = names[0] + '@2x.png'
    dep  = target + '.svg'
    params = []
    try:
        params.append('-w {}'.format(r['w']))
    except KeyError:
        pass
    try:
        params.append('-h {}'.format(r['h']))
    except KeyError:
        pass
    coms = ['inkscape -f {{src}} -e {{tgt}} {}'.format(' '.join(params))]
    if r.get('fix', False):
        coms.append('python fix-antialias.py {{tgt}}'.format())
    r = make_rule(rule, dep, coms)
    yield r
    for name in names[1:]:
        name = os.path.join(TARGET_DIR, name + '@2x.png')
        com = 'cp {} {}'.format(dep, name)
        yield Rule(name, r.rule, com)

def process_png(target, r):
    try:
        names = r['names']
    except KeyError:
        names = [target]
    for name in names:
        rule = name   + '@2x.png'
        dep  = target + '.png'
        coms = ['cp {{src}} {{tgt}}'.format()]
        return make_rule(rule, dep, coms)

def process_ini(target, r):
    rule = target + '.ini'
    dep  = rule
    coms = ['cp {{src}} {{tgt}}'.format()]
    return make_rule(rule, dep, coms)

def process_py(target, r):
    target_path = os.path.join(SOURCE_DIR, target + '.py')
    deps = [os.path.join(SOURCE_DIR, s) for s in r['srcs']]
    deps.append(target_path)
    coms = 'python {}'.format(target_path)
    try:
        names = r['names']
    except KeyError:
        names = [target]
    for name in names:
        name = os.path.join(TARGET_DIR, name + '@2x.png')
        yield Rule(name, ' '.join(deps), coms)

def process_config(config):
    for target, r in config.get('svg', {}).items():
        yield from process_svg(target, r)
    for target, r in config.get('py', {}).items():
        yield from process_py(target, r)
    for target, r in config.get('png', {}).items():
        yield process_png(target, r)
    for target, r in config.get('ini', {}).items():
        yield process_ini(target, r)


config = load_config()
rules = list(process_config(config))
rules.append(Rule('all', ' '.join(r.rule for r in rules), ''))
with open('Makefile', 'w') as fd:
    for r in reversed(rules):
        fd.write('{}: {}\n\t{}'.format(r.rule, ' '.join([r.deps, '| bin/']), r.coms))
        fd.write('\n')
    fd.write('bin/:\n\tmkdir bin\n')
