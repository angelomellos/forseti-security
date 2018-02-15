# Copyright 2017 The Forseti Security Authors. All rights reserved.
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

"""Forseti installer CLI config object."""

from config import Config
from ..util.constants import TEMPLATE_TYPE_CLIENT


class ClientConfig(Config):
    """Forseti installer CLI config object."""

    def __init__(self, **kwargs):
        """Initialize.

        Args:
            kwargs (dict): The kwargs.
        """
        super(ClientConfig, self).__init__(**kwargs)
        self.template_type = TEMPLATE_TYPE_CLIENT