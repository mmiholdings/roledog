import re, pathlib, datetime, textwrap
root = pathlib.Path(__file__).resolve().parents[1]
tpl  = (root/'README.tpl.md').read_text(encoding='utf-8')
docs = {p.stem.upper(): p.read_text(encoding='utf-8')
        for p in (root/'docs').glob('*.md')}
def inject(match):
    name = match.group(1).upper()
    return docs.get(name, f'> *TODO { name }*')
out = re.sub(r'{{(\w+)}}', inject, tpl)
out = out.replace('{{DATE}}', datetime.date.today().isoformat())
(root/'README.md').write_text(out, encoding='utf-8')
print('README rebuilt ✔')
