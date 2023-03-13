cmake_minimum_required(VERSION 3.15)

project(skbgudhi VERSION 0.0.0)

add_definitions(-DDEBUG_TRACES)

# C++ requirements
find_package(TBB REQUIRED)
# Python modules requirements
find_package(pybind11 CONFIG REQUIRED)
find_package(PythonExtensions REQUIRED)
find_package(Cython REQUIRED)

add_executable(bench_tbb bench_tbb.cpp)
target_link_libraries(bench_tbb TBB::tbb)
install(TARGETS bench_tbb LIBRARY DESTINATION skbgudhi)

add_subdirectory(skbgudhi)