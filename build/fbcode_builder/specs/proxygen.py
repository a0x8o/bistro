#!/usr/bin/env python
# Copyright (c) Facebook, Inc. and its affiliates.
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import specs.folly as folly
import specs.fizz as fizz
import specs.mvfst as mvfst
import specs.sodium as sodium
import specs.wangle as wangle
import specs.zstd as zstd


def fbcode_builder_spec(builder):
    builder.add_option(
        'proxygen/proxygen:cmake_defines',
        {
            'BUILD_QUIC': 'ON',
        }
    )
    return {
        'depends_on': [folly, wangle, fizz, sodium, zstd, mvfst],
        'steps': [
            # CMake build with QUIC/HTTP3
            builder.fb_github_cmake_install(
                'proxygen/proxygen', '..'),
            # Legacy build with no QUIC/HTTP3
            builder.fb_github_autoconf_install('proxygen/proxygen'),
        ],
    }
