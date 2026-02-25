# 📐 Area Finder

Area Finder is a specialized tool designed to calculate the area of any polygon using the **Shoelace Formula** (also known as Gauss's Area Formula). It provides both a convenient Command Line Interface (CLI) and a modern, intuitive Web Interface built with Flask.

## ✨ Features

- **Shoelace Algorithm**: High-precision area calculation for simple polygons.
- **Dual Interface**: Use it directly in your terminal or via a browser.
- **Vertex Ordering**: 
  - Supports standard ordered vertices (Clockwise or Counter-Clockwise).
  - Includes an experimental feature to automatically order unordered vertices using centroid sorting (recommended for convex polygons).
- **Web App**: Responsive design with real-time coordinate plotting and calculation.
- **Vercel Ready**: Pre-configured for easy deployment to Vercel.

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- `pip` (Python package installer)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ByteBard58/area-finder.git
   cd "Area Finder"
   ```

2. **Create a virtual environment (optional but recommended)**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 🛠 Usage

### Command Line Interface (CLI)

Run the core script to use the interactive CLI mode:

```bash
python area_finder.py
```

Follow the prompts to:
1. Enter the number of vertices.
2. Input each coordinate in `x,y` format.

### Web Application

Launch the Flask server to access the GUI:

```bash
python app.py
```

Once running, navigate to `http://127.0.0.1:5000` in your web browser.

## 🧪 How it Works

The tool uses the **Shoelace Formula**:

$$\text{Area} = \frac{1}{2} | \sum_{i=1}^{n-1} (x_i y_{i+1} - x_{i+1} y_i) + (x_n y_1 - x_1 y_n) |$$

Where $(x_n, y_n)$ are the coordinates of the vertices.

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page if you want to contribute.

---
## 📝 Note
This project is a part of my [Curiosity Code](https://github.com/ByteBard58/Curiosity-Code) repository, where I work on various mathematical analyses and academic tools, which I do as a hobby. Feel free to check those out if you're interested.

Have a great day! 😀
