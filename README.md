# Quarto-driven Research Project Repository Template


## Tools you'll need

- [Quarto](https://quarto.org/) 
    - Handles making markdown notebooks into beautiful outputs, from PDF to html (or even Word!) 
- [`uv`](https://docs.astral.sh/uv/)
    - My python project and package manager of choice, lightning fast, simple, all in one place, no more venv and pip struggles
- R and `renv`
    - Kinda self-explanatory, but `renv` makes managing R projects nice without the bloat, and it comes built in with R!

## To get started

As this is a template repo, you'll probably want to use it as a basis for your own project repo. You have a few options:

1. Clone it, then delete the `.git` folder, and initialize it as a new repo for your own project.

2. "Use this template" button on GitHub.

3. Alternatively, if you're using the GitHub CLI tool:
    ```sh
    gh repo create <new-repo-name> --template="https://github.com/agbocsardi/quarto-project-template.git"
    ```

## Intended Workflow Guidelines
- High-level workflow code (what to run, what order, etc) should live in the project root, this should mostly just call things you have defined in your `lib` modules. 
    - You can use `source('lib/foo.r')` in R, and `from lib.foo import bar` in python to access the functions you defined.
- Complimentary to the previous one, `lib` doesn't contain code that should run, it's meant for defining functions that you'll call in your main code.
- Don't rely on notebooks for the final product: they are useful in presenting your work, gathering quick feedback, experimenting, but if you want to have some code become part of the final codebase, refactor it into either the manuscript, the run-code, or the modules.




## Notes

When using `uv`, the quarto commands need a bit of love:

```{sh}
uv run quarto preview manuscript/main.qmd -t aog-article-pdf
```
