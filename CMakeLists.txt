cmake_minimum_required(VERSION 2.8.12)
project(cmake_wrapper)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

add_subdirectory(${CMAKE_BINARY_DIR}/source_subfolder)
