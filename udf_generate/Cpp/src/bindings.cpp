#include "mesh_udf.h"
#include <pybind11/eigen.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

PYBIND11_MODULE(udf_cpp, m) {
  m.doc() = "Mesh unsigned distance field via libigl";

  m.def("point_mesh_udf", &point_mesh_udf, py::arg("points"), py::arg("verts"),
        py::arg("faces"),
        "Compute unsigned distance from query points to mesh surface");
}
