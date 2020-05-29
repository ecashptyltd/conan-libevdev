from conans import ConanFile, AutoToolsBuildEnvironment, tools
import os

class LibevdevConan(ConanFile):
    name = "libevdev"
    version = "1.8.0"
    license = "X11"
    description = "Wrapper library for Linux evdev devices."
    homepage = "https://www.freedesktop.org/wiki/Software/libevdev"
    url = "https://github.com/ecashptyltd/conan-libevdev.git"
    topics = ("evdev")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    def configure(self):
        del self.settings.compiler.libcxx

    def source(self):
        tools.get("https://www.freedesktop.org/software/libevdev/libevdev-{0}.tar.xz".format(self.version))
        os.rename("libevdev-{0}".format(self.version), "libevdev")

    def build(self):
        autotools = AutoToolsBuildEnvironment(self)
        autotools.configure(configure_dir=os.path.join(self.source_folder, "libevdev"))
        autotools.make()
        autotools.install()

    def package(self):
        self.copy(pattern="COPYING", src="libevdev", keep_path=False)
        self.copy("*.h", dst="include", src="libevdev/include")
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["evdev"]
