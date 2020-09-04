#!/usr/bin/env python3
## See the bottom of this file for license information

from modules import reddit_api

if __name__ == '__main__':
  headers = {'user-agent': 'reddit-to-youtube/0.0.1'}
  links = reddit_api.get_top_links('tiktokcringeanarchy', 'week', 100, headers)

  link_num = 0
  for link in links:
    link_num += 1
    print(link_num, ': ', link)


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
