cmake_minimum_required(VERSION 2.8.12)
project(projectq_gpu)
find_package( CUDA REQUIRED )
#find_package(PythonLibs)
#include_directories(${PYTHON_INCLUDE_DIRS})
add_subdirectory(pybind11)
set_target_properties(
        projectq_gpu
        PROPERTIES
        CUDA_SEPARABLE_COMPILATION ON)
pybind11_add_module(_cppsim _cppsim.cu)