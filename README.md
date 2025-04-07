# Quarto-driven Research Project Repository Template


## Tools you'll need

- Quarto 
- `uv`
- R

## To get started

As this is a template repo, you'll probably want to clone it, then delete the `.git` folder, and initialize it as a new repo for your own project.

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
