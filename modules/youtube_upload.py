#!/usr/bin/env python3
# See the bottom of this file for license information
import os

def youtube_upload(output: str, title: str, description: str, keywords: str, category: int, privacyStatus: str):
    os.system(f"python3 upload_video.py --file=\"{output}\" --title=\"{title}\" --description=\"{description}\" --keywords=\"{keywords}\" --category=\"{category}\" --privacy=\"{privacyStatus}\"")

#  Reddit-To-YouTube combines vreddit posts into one YouTube video.
#  Copyright (C) 2020  Calvin Barrett, Ralph Drake
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
