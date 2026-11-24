import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

os.makedirs("report_assets", exist_ok=True)
logo_path = os.path.join("report_assets", "mnr_logo.png")

fig, ax = plt.subplots(figsize=(4, 4), dpi=300)
fig.patch.set_facecolor("#ffffff")
ax.set_facecolor("#ffffff")

# Concentric rings
circle_outer = plt.Circle((0.5, 0.5), 0.47, color="#0b2545", fill=False, linewidth=3)
circle_gold = plt.Circle((0.5, 0.5), 0.44, color="#d97706", fill=False, linewidth=1.2)
circle_inner_bg = plt.Circle((0.5, 0.5), 0.42, color="#f8fafc", fill=True)
circle_center = plt.Circle((0.5, 0.5), 0.30, color="#0b2545", fill=True)
circle_gold_inner = plt.Circle((0.5, 0.5), 0.28, color="#d97706", fill=False, linewidth=1.2)

ax.add_patch(circle_outer)
ax.add_patch(circle_gold)
ax.add_patch(circle_inner_bg)
ax.add_patch(circle_center)
ax.add_patch(circle_gold_inner)

# Monogram "MNR" in center
ax.text(0.5, 0.59, "MNR", color="#fbbf24", fontsize=27, fontweight="bold", 
        fontfamily="serif", ha="center", va="center")

# Central Open Book motif
book_l = patches.Polygon([[0.37, 0.42], [0.48, 0.44], [0.48, 0.33], [0.37, 0.31]], 
                         closed=True, facecolor="#ffffff", edgecolor="#fbbf24", linewidth=1.2)
book_r = patches.Polygon([[0.52, 0.44], [0.63, 0.42], [0.63, 0.31], [0.52, 0.33]], 
                         closed=True, facecolor="#ffffff", edgecolor="#fbbf24", linewidth=1.2)
ax.add_patch(book_l)
ax.add_patch(book_r)
ax.plot([0.5, 0.5], [0.32, 0.44], color="#fbbf24", linewidth=2)

# Small torch flame above book
ax.scatter([0.5], [0.465], color="#f59e0b", s=55, marker="^", zorder=5)

# Text in circular band (perfectly centered between 0.30 and 0.42 radius)
ax.text(0.5, 0.86, "MNR UNIVERSITY", color="#0b2545", fontsize=9.5, 
        fontweight="bold", fontfamily="serif", ha="center", va="center")
ax.text(0.5, 0.14, "ESTD. 1974  •  SOET", color="#0b2545", fontsize=8.5, 
        fontweight="bold", fontfamily="serif", ha="center", va="center")

# Golden star accents
ax.scatter([0.14, 0.86], [0.5, 0.5], color="#d97706", s=35, marker="*")

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")
plt.tight_layout()
plt.savefig(logo_path, dpi=300, bbox_inches="tight", transparent=False)
plt.close(fig)
print("Updated vector emblem generated:", logo_path)
