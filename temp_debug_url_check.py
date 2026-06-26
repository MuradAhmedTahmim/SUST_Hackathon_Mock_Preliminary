from pathlib import Path
p = Path('api/urls.py')
text = p.read_text()
print(repr(text))
print('---LINES---')
for i, line in enumerate(text.splitlines(), 1):
    print(f'{i}: {repr(line)}')
