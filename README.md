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

	2.	Navigate to the project directory:

cd SpotifyTidalSync


	3.	Install dependencies:

pip install -r requirements.txt

Setup

	1.	Create a Spotify Developer App:
	•	Go to the Spotify Developer Dashboard and create a new application.
	•	Note your Client ID and Client Secret.
	•	Set the redirect URI to http://localhost/.
	2.	Prepare the .env File:
	•	Create a .env file in the project directory and add the following variables:

SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
SPOTIFY_REDIRECT_URI=http://localhost/
TIDAL_USERNAME=your_tidal_username
TIDAL_PASSWORD=your_tidal_password
SYNC_PLAYLISTS=all  # Or specify playlist names (e.g., "My Playlist, Road Trip")

Usage

	1.	Run the script:

python SpotifyToTidalSync.py

	•	This will sync all playlists if SYNC_PLAYLISTS=all or specific playlists defined in the .env file.

	2.	Options:
	•	Sync only specific playlists by setting SYNC_PLAYLISTS in the .env file (comma-separated playlist names).
	•	Monitor the console for detailed logs of added or skipped tracks.

Environment Variables

Variable	Description	Example
SPOTIFY_CLIENT_ID	Spotify App Client ID	your_client_id
SPOTIFY_CLIENT_SECRET	Spotify App Client Secret	your_client_secret
SPOTIFY_REDIRECT_URI	Redirect URI for Spotify OAuth	http://localhost/
TIDAL_USERNAME	Your Tidal username	your_email@example.com
TIDAL_PASSWORD	Your Tidal password	your_password
SYNC_PLAYLISTS	Specify playlist names to sync (comma-separated) or use all	My Playlist, Chill Vibes

Known Issues

	•	Some tracks may not be found on Tidal due to differences in catalog availability or naming conventions.
	•	API rate limits may cause delays for large playlists.
	•	Multi-threading errors are logged but do not interrupt the overall sync process.

Contributing

Contributions are welcome! To contribute:
	1.	Fork the repository.
	2.	Create a new branch:

git checkout -b feature-name


	3.	Commit your changes:

git commit -m "Add new feature"


	4.	Push your branch:

git push origin feature-name


	5.	Open a pull request.

License

This project is licensed under the MIT License. See the LICENSE file for details.