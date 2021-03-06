#!/usr/bin/env python3
# See the bottom of this file for license information
import os
import subprocess
import youtube_dl


def download_vreddit_videos(links: list, ytdl_opts: dict, download_dir='tmp',
                            timescale=90000):
    # youtube-dl doesn't support specifying an output directory for downloaded
    # files, so we need to change which directory we're in before downloading.
    original_cwd = os.getcwd()
    download_dir = os.path.join(os.getcwd(), download_dir)
    if not os.path.exists(download_dir):
        os.mkdir(download_dir)
    os.chdir(download_dir)

    with youtube_dl.YoutubeDL(ytdl_opts) as ytdl:
        ytdl.download(links)

    videos_to_reencode = (
        f for f in os.listdir(os.getcwd()) if f.endswith('.mp4')
    )

    # re-encode all videos to a uniform timescale so we don't encounter
    # undefined behavior when concatenating them later
    for pos, videos_to_reencode in enumerate(videos_to_reencode):
        subprocess.run([
            'ffmpeg', '-y', '-hide_banner',
            '-i', videos_to_reencode, '-video_track_timescale', str(timescale),
            f'{pos}.mp4'
        ])
        os.remove(videos_to_reencode)

    os.chdir(original_cwd)


def move_video_files(folder='tmp', ext='.mp4'):
    # Might want to consider using tempfile.TemporaryDirectory() instead of
    # os.mkdir(), but I'm not sure if we can pass that around to other modules
    if not os.path.exists(os.path.join(os.getcwd(), folder)):
        os.mkdir(os.path.join(os.getcwd(), folder))

    for file in os.listdir('.'):
        if not file.endswith(ext):
            continue

        os.rename(file, os.path.join(folder, file))


def concat_videos(output: str, ext='.mp4', input_folder='tmp'):
    video_files = []
    for file in os.listdir(input_folder):
        if not file.endswith(ext):
            continue

        # ffmpeg concat supports parsing a list of filenames from a text
        # document, which we generate here.
        # See https://trac.ffmpeg.org/wiki/Concatenate
        f = os.path.join(os.getcwd(), input_folder, file)
        video_files.append(f'file \'{f}\'\n')

    videos_txt = os.path.join(os.getcwd(), input_folder, 'videos.txt')
    with open(videos_txt, 'w') as v:
        v.writelines(video_files)

    # FIXME: Each video needs to be individually re-encoded at a specific
    #        timebase before they are all concatenated, otherwise ffmpeg
    #        will not produce a usable video. (-vsync 0 does not fix this)
    #        See: https://stackoverflow.com/a/56002050
    subprocess.run([
        'ffmpeg', '-y', '-hide_banner',
        '-f', 'concat', '-safe', '0', '-i', videos_txt,
        '-c:v', 'libx264', '-crf', '23', '-preset', 'slow',
        '-c:a', 'aac', output
    ])

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
