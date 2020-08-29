cmake_minimum_required(VERSION 2.8.12)
project(projectq_gpu LANGUAGES CXX CUDA)
find_package( CUDA REQUIRED )
#find_package(PythonLibs)
#include_directories(${PYTHON_INCLUDE_DIRS})
add_subdirectory(pybind11)

cuda_add_library(_cppsim SHARED
  _cppsim.cpp
  _cppkernels/cudastart.cu)

target_link_libraries(_cppsim
  ${PYTHON_LIBRARIES}
  cudart)

set_target_properties(_cppsim PROPERTIES PREFIX "")

# pybind11_add_module(_cppsim _cppsim.cpp)