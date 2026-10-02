"""
D3.1-2, D3.1-3, D3.1-4 — constraint and objective line figures.
Run from repo root: .venv\\Scripts\\python.exe chapter3\\D3_1\\plot_exercises.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# Chinese labels in plots
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

OUT = Path(__file__).resolve().parent / "figures"
OUT.mkdir(parents=True, exist_ok=True)

X = np.linspace(0, 10, 400)


def plot_halfplane(
    ax,
    title: str,
    boundary_fn,
    feasible_fn,
    xlim=(0, 7),
    ylim=(0, 9),
    strict: bool = False,
    label: str = "",
):
    x1g, x2g = np.meshgrid(np.linspace(xlim[0], xlim[1], 500), np.linspace(ylim[0], ylim[1], 500))
    mask = feasible_fn(x1g, x2g) & (x1g >= 0) & (x2g >= 0)
    ax.contourf(x1g, x2g, mask.astype(float), levels=[0.5, 1.5], colors=["#a8d5ff"], alpha=0.85)

    x2_line = boundary_fn(X)
    ls = "--" if strict else "-"
    ax.plot(X, x2_line, "k", lw=2, ls=ls, label=label or title)
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.set_aspect("equal", adjustable="box")
    ax.axhline(0, color="gray", lw=0.8)
    ax.axvline(0, color="gray", lw=0.8)
    ax.grid(True, alpha=0.3)
    ax.set_xlabel(r"$x_1$")
    ax.set_ylabel(r"$x_2$")
    ax.set_title(title)


def d3_1_2():
    # (a) x1 + 3*x2 < 6
    fig, ax = plt.subplots(figsize=(5, 5))
    plot_halfplane(
        ax,
        r"(a) $x_1+3x_2<6$（及 $x_1,x_2\geq0$）",
        lambda x: (6 - x) / 3,
        lambda a, b: a + 3 * b < 6,
        strict=True,
    )
    fig.tight_layout()
    fig.savefig(OUT / "D3_1_2_a.png", dpi=150)
    plt.close(fig)

    # (b) 4*x1 + 3*x2 <= 12
    fig, ax = plt.subplots(figsize=(5, 5))
    plot_halfplane(
        ax,
        r"(b) $4x_1+3x_2\leq12$（及 $x_1,x_2\geq0$）",
        lambda x: (12 - 4 * x) / 3,
        lambda a, b: 4 * a + 3 * b <= 12,
        strict=False,
    )
    fig.tight_layout()
    fig.savefig(OUT / "D3_1_2_b.png", dpi=150)
    plt.close(fig)

    # (c) 4*x1 + x2 < 8
    fig, ax = plt.subplots(figsize=(5, 5))
    plot_halfplane(
        ax,
        r"(c) $4x_1+x_2<8$（及 $x_1,x_2\geq0$）",
        lambda x: 8 - 4 * x,
        lambda a, b: 4 * a + b < 8,
        xlim=(0, 3),
        ylim=(0, 9),
        strict=True,
    )
    fig.tight_layout()
    fig.savefig(OUT / "D3_1_2_c.png", dpi=150)
    plt.close(fig)

    # (d) combined
    fig, ax = plt.subplots(figsize=(6, 6))
    xlim, ylim = (0, 3.5), (0, 3)
    x1g, x2g = np.meshgrid(
        np.linspace(xlim[0], xlim[1], 600),
        np.linspace(ylim[0], ylim[1], 600),
    )
    mask = (
        (x1g >= 0)
        & (x2g >= 0)
        & (x1g + 3 * x2g < 6)
        & (4 * x1g + 3 * x2g <= 12)
        & (4 * x1g + x2g < 8)
    )
    ax.contourf(x1g, x2g, mask.astype(float), levels=[0.5, 1.5], colors=["#7ec8a3"], alpha=0.9)

    ax.plot(X[X <= 6], (6 - X[X <= 6]) / 3, "b--", lw=2, label=r"$x_1+3x_2=6$")
    ax.plot(X[X <= 3], (12 - 4 * X[X <= 3]) / 3, "r-", lw=1.5, alpha=0.5, label=r"$4x_1+3x_2=12$（松弛）")
    ax.plot(X[X <= 2], 8 - 4 * X[X <= 2], "m--", lw=2, label=r"$4x_1+x_2=8$")

    v = np.array([[0, 0], [0, 2], [18 / 11, 16 / 11], [2, 0], [0, 0]])
    ax.plot(v[:, 0], v[:, 1], "ko", ms=5)
    ax.annotate("(0,0)", (0, 0), textcoords="offset points", xytext=(6, 4), fontsize=9)
    ax.annotate("(0,2)", (0, 2), textcoords="offset points", xytext=(6, -12), fontsize=9)
    ax.annotate(r"$(\frac{18}{11},\frac{16}{11})$", (18 / 11, 16 / 11), textcoords="offset points", xytext=(8, 4), fontsize=8)
    ax.annotate("(2,0)", (2, 0), textcoords="offset points", xytext=(-28, 8), fontsize=9)

    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.set_aspect("equal", adjustable="box")
    ax.axhline(0, color="gray", lw=0.8)
    ax.axvline(0, color="gray", lw=0.8)
    ax.grid(True, alpha=0.3)
    ax.set_xlabel(r"$x_1$")
    ax.set_ylabel(r"$x_2$")
    ax.set_title(r"(d) 全部约束 + 非负 — 可行域")
    ax.legend(loc="upper right", fontsize=8)
    fig.tight_layout()
    fig.savefig(OUT / "D3_1_2_d_combined.png", dpi=150)
    plt.close(fig)


def d3_1_3():
    fig, ax = plt.subplots(figsize=(6, 6))
    x = np.linspace(0, 9, 200)
    levels = [(6, "Z=6"), (12, "Z=12"), (18, "Z=18")]
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c"]
    for (z, name), c in zip(levels, colors):
        ax.plot(x, z / 3 - (2 / 3) * x, color=c, lw=2, label=rf"${name}$: $x_2={z/3:.0f}-\frac{{2}}{{3}}x_1$")
        ax.scatter([0], [z / 3], color=c, s=40, zorder=5)
        ax.annotate(f"$x_2={z/3:.0f}$", (0, z / 3), textcoords="offset points", xytext=(8, 0), fontsize=9)

    ax.set_xlim(0, 9)
    ax.set_ylim(0, 7)
    ax.set_aspect("equal", adjustable="box")
    ax.axhline(0, color="gray", lw=0.8)
    ax.axvline(0, color="gray", lw=0.8)
    ax.grid(True, alpha=0.3)
    ax.set_xlabel(r"$x_1$")
    ax.set_ylabel(r"$x_2$")
    ax.set_title(r"D3.1-3 目标函数等值线 $\max Z=2x_1+3x_2$")
    ax.legend(loc="upper right")
    fig.tight_layout()
    fig.savefig(OUT / "D3_1_3_objective_lines.png", dpi=150)
    plt.close(fig)


def d3_1_4():
    fig, ax = plt.subplots(figsize=(6, 6))
    x = np.linspace(0, 22, 200)
    ax.plot(x, 10 - 0.5 * x, "b", lw=2, label=r"$x_2=10-\frac{1}{2}x_1$")
    ax.scatter([0, 20], [10, 0], color="k", zorder=5)
    ax.annotate("(0,10)", (0, 10), textcoords="offset points", xytext=(8, -4), fontsize=10)
    ax.annotate("(20,0)", (20, 0), textcoords="offset points", xytext=(-40, 8), fontsize=10)
    ax.set_xlim(0, 22)
    ax.set_ylim(0, 12)
    ax.set_aspect("equal", adjustable="box")
    ax.axhline(0, color="gray", lw=0.8)
    ax.axvline(0, color="gray", lw=0.8)
    ax.grid(True, alpha=0.3)
    ax.set_xlabel(r"$x_1$")
    ax.set_ylabel(r"$x_2$")
    ax.set_title(r"D3.1-4 $20x_1+40x_2=400$")
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUT / "D3_1_4_line.png", dpi=150)
    plt.close(fig)


def main():
    d3_1_2()
    d3_1_3()
    d3_1_4()
    print(f"Figures saved to: {OUT}")


if __name__ == "__main__":
    main()
