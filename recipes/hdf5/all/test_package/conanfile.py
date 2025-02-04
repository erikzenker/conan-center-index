import os.path

from conans import ConanFile, CMake


class Hdf5TestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.definitions.update({
            "HDF5_CXX": self.options["hdf5"].enable_cxx,
            "HDF5_PARALLEL": self.options["hdf5"].parallel
        })
        cmake.configure()
        cmake.build()

    def test(self):
        bin_path = os.path.join("bin", "test_package")
        self.run(bin_path, run_environment=True)
