#!/usr/bin/env python3
## See the bottom of this file for license information
import requests


def get_top_links(subreddit: str, time: str, limit: int, headers: dict) -> list:
  r = requests.get(f'https://www.reddit.com/r/{subreddit}/top/.json?t={time}&limit={limit}', headers=headers)
  r.raise_for_status()

  # Actual list of posts is nested in response data
  top_posts = r.json()
  top_posts = top_posts['data']['children']

  vreddit_links = []

  for post in top_posts:
    post = post['data']

    if not post['domain'] == 'v.redd.it':
      continue

    vreddit_links.append(post['url'])

  return vreddit_links


if __name__ == '__main__':
  headers = {'user-agent': 'reddit-to-youtube/0.0.1'}
  links = get_top_links('tiktokcringeanarchy', 'week', 100, headers)

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
