#!/usr/bin/env python3
# See the bottom of this file for license information

import os
from datetime import date
import shutil
from modules import reddit_api, video_utils, youtube_upload


if __name__ == '__main__':
    print('Fetching links from Reddit API...')
    headers = {'user-agent': 'reddit-to-youtube/0.0.1'}
    subreddit = 'tiktokcringeanarchy'
    time = 'week'
    links = reddit_api.get_top_links(
        subreddit,
        time,
        30,
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
    output = os.path.join(os.getcwd(), 'test_video.mp4')
    video_utils.concat_videos(output)

    # Remove our temporary files
    shutil.rmtree('tmp')

    todays_date = date.today()
    youtube_upload.youtube_upload(
        output,                                                     # Video directory path 
        f'{subreddit} Top Posts of the {time} ({date.today()})',    # Video title
        f'This {time}\'s top posts from {subreddit}',               # Video description
        f'reddit,{subreddit}',                                      # Video tags
        'public',                                                   # Upload privacy status (accepts public, private, or unlisted)
        '23'                                                        # Youtube API video category id (region specific)
    )

    os.remove(output)   # Remove our concatenated video


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
