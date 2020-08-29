cmake_minimum_required(VERSION 2.8.12)
project(projectq_gpu LANGUAGES CXX CUDA)
find_package( CUDA REQUIRED )
#find_package(PythonLibs)
#include_directories(${PYTHON_INCLUDE_DIRS})
add_subdirectory(pybind11)
add_library(_cppsimcu STATIC
    _cppkernels/cudastart.cu)

set_target_properties(_cppsimcu PROPERTIES
    POSITION_INDEPENDENT_CODE ON)

add_library(_cppsim MODULE
    _cppsim.cpp
)

set_target_properties(_cppsim PROPERTIES
    CXX_VISIBILITY_PRESET "hidden"
    INTERPROCEDURAL_OPTIMIZATION TRUE
    PREFIX ""
    SUFFIX ""
)

target_link_libraries(_cppsim PRIVATE _cppsimcu)
pybind11_add_module(_cppsim _cppsim.cpp)