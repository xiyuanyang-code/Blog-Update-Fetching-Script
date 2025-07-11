# update_readme.py
def replace_section(readme_path, prev_path):
    with open(readme_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # fins pattern BEGIN and END
    begin_idx = next(i for i, line in enumerate(lines) if "<!-- BEGIN -->" in line)
    end_idx = next(i for i, line in enumerate(lines) if "<!-- END -->" in line)

    # read file-content for prev.txt
    with open(prev_path, "r", encoding="utf-8") as f:
        prev_content = f.read().rstrip("\n")

    # contruct new content
    new_lines = (
        lines[: begin_idx + 1]
        + ["```text\n"]
        + [prev_content + "\n"]
        + ["```\n"]
        + lines[end_idx:]
    )

    # 写回 README.md
    with open(readme_path, "w", encoding="utf-8") as f:
        f.writelines(new_lines)


if __name__ == "__main__":
    replace_section("README.md", "prev.txt")
