# pip install rich 가 필요합니다.

from rich import print as pprint
from rich.table import Table
from rich.panel import Panel

# 변수
name = "Alice"
age = 25
score = 95.5
data = {"name": name, "age": age, "score": score}

# 1) 컬러/스타일 출력 (f-string)
pprint(f"[bold green]Hello, [name]{name}[/]! Your score is [cyan]{score:.2f}[/].")

# 2) 패널(박스)로 멀티라인 출력
panel_text = """
[bold]Student Info[/]
- Name : [yellow]{name}[/]
- Age  : [magenta]{age}[/]
- Score: [cyan]{score:.2f}[/]
""".format(name=name, age=age, score=score)

pprint(Panel(panel_text, title="Profile", border_style="blue"))

# 3) 테이블 출력 (딕셔너리/리스트 보기 좋게)
table = Table(title="Records")
table.add_column("Key", style="bold")
table.add_column("Value")

for k, v in data.items():
    table.add_row(k, str(v))

pprint(table)

# 4) sep, end 옵션 그대로 활용 (rich.print도 동일 동작)
pprint("2025", "09", "23", sep="-", end="\n\n")