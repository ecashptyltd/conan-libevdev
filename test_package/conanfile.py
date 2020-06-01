import os

from conans import ConanFile, CMake, tools

class LibevdevTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def configure(self):
        del self.settings.compiler.libcxx

    def build(self):
        cmake = CMake(self)
        # Current dir is "test_package/build/<build_id>" and CMakeLists.txt is
        # in "test_package"
        cmake.configure()
        cmake.build()

    def imports(self):
        self.copy('*.so*', dst='bin', src='lib')

    def test(self):
        # We don't run any tests, since we probably don't have permissions to
        # access any evdev devices anyway.
        pass