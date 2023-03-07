
cdef extern from "bench_tbb.h":
    void bench_tbb() nogil

def py_bench_tbb():
    bench_tbb()