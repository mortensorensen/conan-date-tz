from conans import ConanFile, CMake, tools
import os


class DateTzConan(ConanFile):
    name = "date-tz"
    version = "2.4.1"
    license = "MIT"
    url = "https://github.com/mortensorensen/conan-date-tz"
    homepage = "https://github.com/HowardHinnant/date"
    description = "A date and time library based on the C++11/14/17 <chrono> header"
    topics = ("conan", "date", "timezone")
    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False],
        "build_testing": [True, False],
        "system_tz_db": [True, False],
    }
    default_options = {
        "shared": False,
        "build_testing": False,
        "system_tz_db": False,
    }
    generators = "cmake"
    _source_subfolder = "source_subfolder"

    def source(self):
        tools.get("{0}/archive/v{1}.zip".format(self.homepage, self.version))
        extracted_dir = "date-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_SHARED_LIBS"] = self.options.shared
        cmake.definitions["ENABLE_DATE_TESTING"] = self.options.system_tz_db
        cmake.definitions["USE_SYSTEM_TZ_DB"] = self.options.build_testing
        cmake.definitions["BUILD_TZ_LIB"] = True
        cmake.configure()
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()
        cmake.install()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()
