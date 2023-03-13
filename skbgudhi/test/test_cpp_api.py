from skbgudhi import cyt
from skbgudhi import pyb

# ~/workspace/formations/hands_on_scikit_build/_skbuild/linux-x86_64-3.7/cmake-build$ python -m pytest ../../../skbgudhi/test/test_cpp_api.py -s
def test_cpp_interfaces():
    for method in [pyb.bench_tbb, cyt.py_bench_tbb]:
        method()

