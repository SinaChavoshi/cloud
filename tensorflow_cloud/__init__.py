# Copyright 2020 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Import version string.
from .version import __version__

from .python.core.machine_config import AcceleratorType
from .python.core.machine_config import COMMON_MACHINE_CONFIGS
from .python.core.machine_config import MachineConfig
from .python.core.run import run
from .python.core.run import remote

# Provides direct access to Tuner and CloudOracle classes,
# which is the primary user-facing APIs.
from .python.tuner.tuner import CloudOracle
from .python.tuner.tuner import Tuner

# Provides direct access to cloud_fit,
from .python.cloud_fit.client import cloud_fit
