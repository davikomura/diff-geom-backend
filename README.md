# Differential Geometry Simulator

This repository contains the backend of the Differential Geometry Simulator, a service that computes and returns parametrized curves and surfaces in 3D, as well as various curvature measures (Gaussian, Mean, Principal, and Normal) in a modular and extensible fashion.

## Features

* Parametrization of multiple curves and surface.
* Computation of curvature measures:

  * Gaussian curvature (K)
  * Mean curvature (H)
  * Principal curvatures (k₁, k₂)
  * Normal curvature (in arbitrary direction)
* JSON responses with coordinates and curvature values ready for front-end consumption.
* Single `/curve/` endpoint configurable via query parameters to select the curve/surface and curvature type.

## Project Structure

```
app/
├── api/
│   └── curve.py               
├── core/
│   ├── geometry_curve.py      
│   ├── curves/               
│   │   ├── sphere.py
│   │   ├── torus.py
│   │   ├── hyperbolic_paraboloid.py
│   │   ├── registry.py
│   │   ├── helicoid.py
│   │   ├── enneper.py
│   │   └── elliptic_paraboloid.py
│   ├── partials.py            
│   ├── normals.py             
│   ├── first_fundamental_form.py
│   ├── second_fundamental_form.py
│   └── curvatures.py          
├── utils/
│   ├── response_builder.py    
│   └── response_handler.py    
├── main.py                    
└── requirements.txt
```

## Requirements

* Python 3.8 or higher
* FastAPI
* Uvicorn
* NumPy

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Server

Start the development server:

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## API Usage

### Endpoint: `/curve/`

* **Method:** GET
* **Query Parameters:**

  * `curve` (string, required): Name of the curve or surface to compute. Examples: `sphere`, `torus`, `helicoid`, `enneper`.
  * `curvature` (string, optional, default `gaussian`): Type of curvature measure. Valid values: `gaussian`, `mean`, `principal`, `normal`.
  * `a`, `b` (float, optional): Coefficients used for normal curvature calculation.

## Code Organization

* **Parametrizations:** Each curve or surface is implemented in a module under `app/core/curves/`, returning NumPy arrays for coordinates and parameters.
* **Computation Modules:** Partial derivatives, normals, fundamental forms, and curvature calculations reside in `core/partials.py`, `core/normals.py`, `core/first_fundamental_form.py`, `core/second_fundamental_form.py`, and `core/curvatures.py`.
* **Request Handler:** `utils/response_handler.py` encapsulates the logic for invoking parametrizations, computing curvatures, and formatting results.
* **Serialization:** `utils/response_builder.py` provides functions to convert NumPy objects into JSON-serializable structures.

## Future Development Guidelines

* Add more parametrized curves and surfaces.
* Support custom user-defined parametrizations via API input.
* Integrate with a React-based front end for interactive 3D visualization.
* Implement result caching to optimize performance.

---

This document is intended for developers maintaining and extending the backend of the Differential Geometry Simulator.