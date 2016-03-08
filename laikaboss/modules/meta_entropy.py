# Copyright 2016 Josh Liburdi
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
# 
from laikaboss.si_module import SI_MODULE
import entropy

class META_ENTROPY(SI_MODULE):
    def __init__(self,):
        self.module_name = "META_ENTROPY"

    def _run(self, scanObject, result, depth, args):
        moduleResult = []

        byte_entropy = entropy.shannon_entropy(scanObject.buffer) * 8.0
        scanObject.addMetadata(self.module_name, "ENTROPY", byte_entropy)

        return moduleResult
