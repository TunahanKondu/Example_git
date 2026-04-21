import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


def visualize_cluster(csv_path="/home/atolye/detected_cluster.csv"):
    csv_file = Path(csv_path)

    if not csv_file.exists():
        print(f"File not found: {csv_file}")
        return

    try:
        df = pd.read_csv(csv_file)

        # Expecting columns: x,y
        if "x" not in df.columns or "y" not in df.columns:
            print("CSV must contain 'x' and 'y' columns.")
            print("Found columns:", list(df.columns))
            return

        plt.figure(figsize=(8, 8))
        plt.scatter(df["x"], df["y"], s=20)

        plt.axhline(0, linewidth=0.8)
        plt.axvline(0, linewidth=0.8)

        plt.title(f"Detected Cluster Visualization\n{csv_file}")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.grid(True, linestyle="--", alpha=0.6)
        plt.axis("equal")

        # Optional: connect points in order
        plt.plot(df["x"], df["y"], alpha=0.5)

        plt.show()

    except Exception as e:
        print(f"Error reading or plotting file: {e}")


if __name__ == "__main__":
    visualize_cluster()
