# Spotify to Tidal Sync

**Description**:  
This script synchronizes your Spotify playlists and tracks with your Tidal account, allowing seamless management of your music library across both platforms.

---

## Features

- Synchronizes all Spotify playlists to Tidal.
- Option to sync specific playlists by name.
- Prevents duplicate tracks in Tidal by checking existing favorites.
- Utilizes multi-threading for faster syncing.
- Handles Spotify "Liked Songs" and playlist tracks.
- Logs progress and errors for easy troubleshooting.

---

## Table of Contents

1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Setup](#setup)
4. [Usage](#usage)
5. [Environment Variables](#environment-variables)
6. [Known Issues](#known-issues)
7. [Contributing](#contributing)
8. [License](#license)

---

## Requirements

- Python 3.8 or higher.
- Spotify and Tidal accounts.
- API credentials for Spotify.
- Required Python libraries:
  - `python-dotenv`
  - `spotipy`
  - `tidalapi`

---

## Installation

1. **Clone this repository**:
   ```bash
   git clone https://github.com/leotarafa/SpotifyTidalSync.git