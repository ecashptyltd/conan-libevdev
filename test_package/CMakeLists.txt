cmake_minimum_required(VERSION 2.8.12)
project(PackageTest C)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(evdevDetect evdevDetect.cpp)
target_link_libraries(evdefDetect ${CONAN_LIBS})