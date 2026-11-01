#!/usr/bin/env python3
"""Suggest a YouTube title and hashtags for a music video.

Usage: python3 main.py "Song Title" "Artist Name"
"""
import sys

def suggest(title, artist):
    base = f"{title} | {artist}"
    tags = ["#Music", "#NewSong", "#Trending", "#YouTubeMusic"]
    return base, " ".join(tags)

if __name__ == "__main__":
    title = sys.argv[1] if len(sys.argv) > 1 else "My Song"
    artist = sys.argv[2] if len(sys.argv) > 2 else "Artist"
    t, h = suggest(title, artist)
    print("Title:", t)
    print("Hashtags:", h)
