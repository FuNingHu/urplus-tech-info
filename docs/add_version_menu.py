"""Add the version menu to builds that predate the multiversion extension."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent / "build" / "html"


def version_names(root: Path) -> list[str]:
    names = [
        path.name
        for path in root.iterdir()
        if path.is_dir() and (path / "index.html").is_file()
    ]
    def sort_key(name: str):
        if name in ("main", "master"):
            return (1,)
        numbers = []
        for part in name.lstrip("v").split("."):
            try:
                numbers.append(int(part))
            except ValueError:
                numbers.append(-1)
        return (0, *numbers)

    return sorted(names, key=sort_key, reverse=True)


def menu(current: str, names: list[str]) -> str:
    items = "\n".join(
        f'      <dd><a href="../{name}/index.html">{name}</a></dd>'
        for name in names
    )
    return f"""
<div class="rst-versions" data-toggle="rst-versions" role="note" aria-label="Versions">
  <span class="rst-current-version" data-toggle="rst-current-version">
    <span class="fa fa-book"></span>
    v: {current}
    <span class="fa fa-caret-down"></span>
  </span>
  <div class="rst-other-versions">
    <dl>
      <dt>Versions</dt>
{items}
    </dl>
  </div>
</div>
"""


def main() -> None:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT
    names = version_names(root)
    if len(names) < 2:
        return
    for name in names:
        snippet = menu(name, names)
        for page in (root / name).glob("*.html"):
            text = page.read_text(encoding="utf-8")
            if "rst-versions" in text or "</body>" not in text:
                continue
            page.write_text(text.replace("</body>", snippet + "</body>", 1), encoding="utf-8")


if __name__ == "__main__":
    main()
