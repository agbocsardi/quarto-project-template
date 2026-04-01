"""
Main analysis entry point.

Run with: uv run python scripts/run_analysis.py

This script reads from data/, performs analysis, and writes outputs to
output/figures/ and output/tables/.
"""

import pandas as pd
import matplotlib.pyplot as plt
from pyprojroot import here

DATA_DIR = here("data")
FIGURE_DIR = here("output/figures")
TABLE_DIR = here("output/tables")


def main():
    # --- Load data ---
    # df = pd.read_csv(DATA_DIR / "your-data.csv")

    # --- Analysis ---
    # ...

    # --- Save figures (always PDF for manuscript, PNG for DOCX/presentations) ---
    # fig, ax = plt.subplots()
    # ax.plot(...)
    # fig.savefig(FIGURE_DIR / "fig-example.pdf", bbox_inches="tight")
    # fig.savefig(FIGURE_DIR / "fig-example.png", bbox_inches="tight", dpi=300)
    # plt.close(fig)

    # --- Save tables (LaTeX fragments for manuscript, CSV for DOCX wrapper) ---
    # df.to_latex(
    #     TABLE_DIR / "tab-descriptive-stats.tex",
    #     index=False,
    #     booktabs=True,
    #     caption="Descriptive statistics",
    #     label="tab:descriptive-stats",
    #     position="H",
    # )
    # df.to_csv(TABLE_DIR / "tab-descriptive-stats.csv", index=False)

    print("Analysis complete.")


if __name__ == "__main__":
    main()
