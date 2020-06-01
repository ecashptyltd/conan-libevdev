cmake_minimum_required(VERSION 2.8.12)
project(PackageTest C)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(evdevDetect evdevDetect.c)
target_link_libraries(evdevDetect ${CONAN_LIBS})