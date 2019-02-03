#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.69.0@bincrafters/stable")

class BoostIntrusiveConan(base.BoostBaseConan):
    name = "boost_intrusive"
    version = "1.69.0"
    url = "https://github.com/bincrafters/conan-boost_intrusive"
    lib_short_names = ["intrusive"]
    header_only_libs = ["intrusive"]
    b2_requires = [
        "boost_assert",
        "boost_config",
        "boost_container_hash",
        "boost_core",
        "boost_move",
        "boost_static_assert"
    ]
