# Research Project Template

A template for reproducible academic research projects combining LaTeX manuscripts, Python analysis scripts, and Quarto notebooks.

## Tools you'll need

- **LaTeX** (XeLaTeX or LuaLaTeX) for compiling the manuscript
- **[Quarto](https://quarto.org/)** for rendering exploratory notebooks and optional DOCX export
- **[`uv`](https://docs.astral.sh/uv/)** for Python project and package management
- **R** and **`renv`** for R-based analysis (optional)

## To get started

1. Clone or use as template:
    ```sh
    gh repo create <new-repo-name> --template="https://github.com/agbocsardi/quarto-project-template.git"
    ```

2. Install Python dependencies:
    ```sh
    uv sync
    ```

3. (Optional) Activate R environment:
    ```r
    renv::restore()
    ```

## Architecture

```
project/
├── data/              # Raw data (gitignored)
├── notebooks/         # Exploratory Quarto notebooks
├── scripts/           # Production Python analysis pipeline
├── manuscript/        # LaTeX source (main.tex + section files)
├── output/            # Git-tracked generated artifacts
│   ├── figures/       # PDF figures from scripts
│   └── tables/        # LaTeX table fragments from scripts
└── _output/           # Quarto render output (gitignored)
```

### Key workflow

1. **Explore** in `notebooks/` — quick POCs, data exploration
2. **Formalize** in `scripts/` — production analysis that writes to `output/`
3. **Write** in `manuscript/` — LaTeX imports figures/tables from `output/`
4. **Export** via `manuscript/submission.qmd` — DOCX when a conference requires it

### Commands

| Task                        | Command                                           |
|-----------------------------|---------------------------------------------------|
| Run analysis                | `uv run python scripts/run_analysis.py`           |
| Compile manuscript (PDF)    | `cd manuscript && latexmk -xelatex main.tex`      |
| Export DOCX                 | `uv run quarto render manuscript/submission.qmd`  |
| Render a notebook           | `uv run quarto render notebooks/<name>.qmd`       |

See `AGENTS.md` for full project conventions.
