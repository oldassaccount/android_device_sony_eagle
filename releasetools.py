# Copyright (C) 2012 The Android Open Source Project
# Copyright (C) 2014 The CyanogenMod Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Custom OTA Package commands for msm8226"""

import os

TARGET_DIR = os.getenv('OUT')
TARGET_DEVICE = os.getenv('CM_BUILD')

def FullOTA_InstallEnd(self):
  if TARGET_DEVICE == "eaglei":
    self.output_zip.write(os.path.join(TARGET_DIR, "D5x22.sh"), "D5x22.sh")
    self.script.AppendExtra('package_extract_file("D5x22.sh", "/tmp/D5x22.sh");')
    self.script.AppendExtra('set_perm(0, 0, 0777, "/tmp/D5x22.sh");')
    self.script.AppendExtra('run_program("/tmp/D5x22.sh");')
