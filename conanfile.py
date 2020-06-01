from conans import ConanFile, AutoToolsBuildEnvironment, tools
import os

class LibevdevConan(ConanFile):
    name = "libevdev"
    version = "1.9.0"
    license = "X11"
    description = "Wrapper library for Linux evdev devices."
    homepage = "https://www.freedesktop.org/wiki/Software/libevdev"
    url = "https://github.com/ecashptyltd/conan-libevdev.git"
    topics = ("evdev")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    _source_subfolder = "source_subfolder"

    def configure(self):
        del self.settings.compiler.libcxx

    def source(self):
        git = tools.Git(folder=self._source_subfolder)
        git.clone("https://gitlab.freedesktop.org/libevdev/libevdev", "libevdev-" + self.version)

    def build(self):
        self.run("autoreconf -fvi", cwd=self._source_subfolder)
        autotools = AutoToolsBuildEnvironment(self)
        autotools.configure(configure_dir=self._source_subfolder)
        autotools.make()

    def package(self):
        self.copy("*/libevdev.h", src=self._source_subfolder, dst="include")
        self.copy("*/libevdev-uinput.h", src=self._source_subfolder, dst="include")
        self.copy("*/libevdev.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["evdev"]
