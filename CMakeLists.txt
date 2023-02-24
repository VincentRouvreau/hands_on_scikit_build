cmake_minimum_required(VERSION 3.15)

project(${SKBUILD_PROJECT_NAME} VERSION ${SKBUILD_PROJECT_VERSION})

# set(CMAKE_PREFIX_PATH "/home/gailuron/miniconda3/envs/scikitbuild")

find_package(pybind11 CONFIG REQUIRED)
find_package(TBB REQUIRED)

pybind11_add_module(_pyb MODULE skbgudhi/pyb.cc)
target_link_libraries(_pyb PRIVATE TBB::tbb)

install(TARGETS _pyb DESTINATION skbgudhi)