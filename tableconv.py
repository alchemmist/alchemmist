import re
import sys
from markdownify import markdownify as md


def convert_html_tables_to_md(content: str) -> str:
    def replace_table(match):
        html_table = match.group(0)
        try:
            normalized_html = re.sub(r">\s+<", "><", html_table)
            return md(normalized_html)
        except Exception as e:
            print(f"Error whyle convert table: {e}", file=sys.stderr)
            return html_table

    pattern = re.compile(r"<table[^>]*>.*?</table>", re.DOTALL | re.IGNORECASE)
    return pattern.sub(replace_table, content)


def add_br_to_bullet_points_in_table_cells(content: str) -> str:
    lines = content.splitlines()
    processed_lines = []

    for line in lines:
        if line.strip().startswith("|") and line.strip().endswith("|"):
            parts = [p.strip() for p in line.strip().split("|")]

            if parts and parts[0] == "":
                parts = parts[1:]
            if parts and parts[-1] == "":
                parts = parts[:-1]

            for i, cell in enumerate(parts):
                if "• " in cell:
                    parts[i] = re.sub(r"(• [^•\n]+?)(?=(?: •|$))", r"\1<br>", cell)

            processed_lines.append("| " + " | ".join(parts) + " |")
        else:
            processed_lines.append(line)

    return "\n".join(processed_lines)


def main():
    try:
        with open("README.md", "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        print("Ошибка: файл README.md не найден", file=sys.stderr)
        sys.exit(1)

    converted_content = convert_html_tables_to_md(content)
    converted_content = add_br_to_bullet_points_in_table_cells(converted_content)

    with open("README.md", "w", encoding="utf-8") as file:
        file.write(converted_content)

    print("✅ Success: tables converted.")


if __name__ == "__main__":
    main()
