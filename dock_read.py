import matplotlib.pyplot as plt
import pandas as pd

def visualize_template(filename='/home/atolye/dock_sablon.csv'):
    try:
        df = pd.read_csv(filename, header=None, names=['x', 'y'])

        plt.figure(figsize=(8, 8))
        plt.scatter(df['x'], df['y'], s=10, label='Selected Cluster Points')

        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)

        plt.title(f"Visualizing {filename}")
        plt.xlabel("X (Relative Meters)")
        plt.ylabel("Y (Relative Meters)")
        plt.legend()
        plt.axis('equal')
        plt.grid(True, linestyle='--', alpha=0.6)

        plt.show()
    except Exception as e:
        print(f"Could not read the file: {e}")

if __name__ == "__main__":
    visualize_template()
