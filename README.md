# DiscreteFrenetSolver

[![PyPI version](https://badge.fury.io/py/discrete-frenet-solver.svg)](https://badge.fury.io/py/discrete-frenet-solver)
![CI](https://github.com/ShixuanGu/DiscreteFrenetSolver/workflows/CI/badge.svg)

[![codecov](https://codecov.io/gh/ShixuanGu/DiscreteFrenetSolver/branch/main/graph/badge.svg)](https://codecov.io/gh/ShixuanGu/DiscreteFrenetSolver)
![Python Versions](https://img.shields.io/pypi/pyversions/discrete-frenet-solver.svg)

DiscreteFrenetSolver is a Python package for computing the discrete Frenet frame (TNB frame) of a curve with numerical corrections. It handles edge cases such as straight segments and ensures orthogonality of the resulting frame for discrete curve data.

While the current version provides core functionality, we are actively working on expanding and refining the package. Future updates will include additional features, performance optimizations, and expanded documentation. 

## Installation

You can install DiscreteFrenetSolver using pip:

```bash
pip install discrete-frenet-solver
```

## Usage

Here's a simple example of how to use DiscreteFrenetSolver:

```python
import numpy as np
from discrete_frenet_solver import solve_frenet_frame

# Define your discrete curve
t = np.linspace(0, 10*np.pi, 500)
x = t * np.cos(t)
y = t * np.sin(t)
z = t
curve = np.column_stack((x, y, z))

# Solve for the Frenet frame
T, N, B = solve_frenet_frame(curve)

print("Tangent vectors:", T)
print("Normal vectors:", N)
print("Binormal vectors:", B)
```

## Features

- Handles straight segments in curves
- Ensures orthogonality of the resulting frame
- Efficient computation for large datasets

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Citation

If you use DiscreteFrenetSolver in your research, please cite our paper:

```bibtex
@article{Gu2024FreSegFP,
  title={FreSeg: Frenet-Frame-based Part Segmentation for 3D Curvilinear Structures},
  author={Shixuan Gu and Jason Adhinarta and Mikhail Bessmeltsev and Jiancheng Yang and Jessica Zhang and Daniel R. Berger and Jeff William Lichtman and Hanspeter Pfister and D. Wei},
  journal={ArXiv},
  year={2024},
  volume={abs/2404.14435},
  url={https://api.semanticscholar.org/CorpusID:269302991}
}
```