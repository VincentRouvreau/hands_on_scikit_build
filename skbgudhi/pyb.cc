#include <pybind11/pybind11.h>

#include "bench_tbb.h"

namespace py = pybind11;

PYBIND11_MODULE(pyb, m) {
      m.def("bench_tbb", &bench_tbb,
          R"pbdoc(
        Benchmark oneTBB parallel_for and a classical for loop. Just displays results.
    )pbdoc");
}
