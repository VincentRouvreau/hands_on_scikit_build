# https://github.com/scikit-build/scikit-build/pull/611
set(SKBUILD_LINK_LIBRARIES_KEYWORD "PRIVATE")

# PyBind11 interface compilation and dependency
pybind11_add_module(pyb MODULE pyb.cc)
target_link_libraries(pyb ${SKBUILD_LINK_LIBRARIES_KEYWORD} TBB::tbb)

# Cython interface compilation and dependency
add_cython_target(cyt CXX)
add_library(cyt MODULE ${cyt})
python_extension_module(cyt)
target_include_directories(cyt PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
target_link_libraries(cyt ${SKBUILD_LINK_LIBRARIES_KEYWORD} TBB::tbb)
