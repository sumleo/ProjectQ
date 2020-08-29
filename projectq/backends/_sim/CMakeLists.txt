cmake_minimum_required(VERSION 2.8.12)
project(projectq_gpu LANGUAGES CXX CUDA)
find_package( CUDA REQUIRED )
#find_package(PythonLibs)
#include_directories(${PYTHON_INCLUDE_DIRS})
add_subdirectory(pybind11)
add_library(dummycu STATIC
    _cppkernels/cudastart.cu)

set_target_properties(dummycu PROPERTIES
    POSITION_INDEPENDENT_CODE ON
    CUDA_VISIBILITY_PRESET "hidden")

target_link_libraries(dummy PRIVATE dummycu)
target_link_libraries(dummy PRIVATE pybind11::module)
# pybind11_add_module(_cppsim _cppsim.cpp)