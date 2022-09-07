import re
from pathlib import Path

prefix = ':id-:name-:class_id'
assert ':' not in prefix, '第一次使用前要先填充模板。'

for file in Path.cwd().glob('**/*.pdf'):
    if re.match('第\d+章', file.stem):
        file.rename(file.with_stem(f'{prefix}-{file.stem}作业'))
