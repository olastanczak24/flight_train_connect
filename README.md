# Train-Flight Scheduler

## Description

The **Train-Flight Scheduler** is a Python-based tool designed to visualize travel connections between cities, including both **train** and **flight** routes. The tool stores connections in a `connections.json` file and can visualize them as a graph, using libraries such as `networkx` and `matplotlib`. The goal is to provide a useful tool for analyzing travel routes, scheduling trips, and understanding connections between multiple destinations.

## Features

- Stores and visualizes travel connections in a **JSON** format.
- Generates a **graphical visualization** of cities and their connections, including flight and train routes.
- Uses **Python** libraries like `networkx` and `matplotlib` for graph representation and visualization.
- Easy to extend with additional travel connection data.

## Table of Contents

- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

Follow these instructions to set up the project locally and run it.

### Prerequisites

To run this project, you'll need:

- **Python 3.x**: The project is developed using Python 3.
- **pip**: Python package installer for managing dependencies.

### Installation

1. **Clone the repository** to your local machine:

    ```bash
    git clone https://github.com/your-username/train-flight-scheduler.git
    cd train-flight-scheduler
    ```

2. **Create a virtual environment**:

    - On Linux/macOS:

        ```bash
        python3 -m venv venv
        ```

    - On Windows:

        ```bash
        python -m venv venv
        ```

3. **Activate the virtual environment**:

    - On Linux/macOS:

        ```bash
        source venv/bin/activate
        ```

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

4. **Install the required dependencies**:

## Requirements
- Python 3.8 or higher
- networkx==3.1
- matplotlib==3.7.1


### Usage

1. **Run the main script** to generate the `connections.json` file and visualize the routes:

    ```bash
    python train_flight_connections.py
    ```

    This will:
    - Generate a `connections.json` file containing your travel connections data.
    - Display a graph showing the nodes (cities) and edges (connections).

2. **Modify the `connections.json`** file as needed to update the connections or add new routes. Then re-run the script to see changes reflected in the visualization.

### Example Output

After running the script, you will see a graphical representation of cities connected by edges representing train or flight routes. Nodes represent cities (e.g., Napoli, Rome, London) and edges represent connections (e.g., train or flight routes with details like labels and travel times).

### Customizing the Data

You can update the `connections.json` file with your own travel routes. Each entry contains:

- `from`: The starting city.
- `to`: The destination city.
- `label`: The travel route (flight or train code).
- `time`: The travel time.

Example:

```json
{
  "from": "Napoli",
  "to": "Rome",
  "label": "IC552 -> AZ1270",
  "time": "13:05 -> 15:15"
}
```


