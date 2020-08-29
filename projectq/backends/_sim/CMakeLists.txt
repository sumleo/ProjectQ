cmake_minimum_required(VERSION 2.8.12)
project(projectq_gpu LANGUAGES CXX CUDA)
find_package( CUDA REQUIRED )

set(CMAKE_SKIP_BUILD_RPATH TRUE)
set(CMAKE_BUILD_WITH_INSTALL_RPATH TRUE)
set(CMAKE_INSTALL_RPATH "@loader_path")
set(CMAKE_INSTALL_RPATH_USE_LINK_PATH TRUE)

add_subdirectory(pybind11)
cuda_add_library(cuda_gpu SHARED _cppkernels/cudastart.cu)

pybind11_add_module(_cppsim _cppsim.cpp)
target_link_libraries(_cppsim SHARED cuda_gpu)