#!/usr/bin/env python3
# See the bottom of this file for license information

import os
from modules import reddit_api, video_utils

if __name__ == '__main__':
    print('Fetching links from Reddit API...')
    headers = {'user-agent': 'reddit-to-youtube/0.0.1'}
    links = reddit_api.get_top_links(
        'tiktokcringeanarchy',
        'week',
        100,
        headers
    )

    # test_links = links[0:2]
    test_links = links
    print('Test links:', test_links)
    print('Downloading test links with youtube_dl...')
    ytdl_opts = {
        'format': 'bestvideo+bestaudio',
        'quiet': True,
        'forcefilename': True
    }
    video_utils.download_vreddit_videos(test_links, ytdl_opts)

    print('Combining video files')
    video_utils.concat_videos(os.path.join(os.getcwd(), 'test_video.mp4'))


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
