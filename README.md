Spotify to TIDAL Playlist Sync

This Python script securely synchronizes your saved Spotify playlists with your TIDAL favorites. It ensures no duplicate tracks are added, uses multithreading for performance, and employs secure practices to protect sensitive credentials.

Features

	•	Secure Credential Handling: Credentials are stored in a .env file, keeping sensitive information safe.
	•	Sync All Saved Playlists: Syncs all Spotify playlists you’ve saved or followed to your TIDAL favorites.
	•	Duplicate Prevention: Skips tracks that already exist in your TIDAL favorites.
	•	Multithreading: Adds tracks to TIDAL in parallel for improved performance.
	•	Detailed Logging: Outputs skipped, added, and missing tracks for easy debugging.

Requirements

	•	Python 3.8+
	•	Spotify Developer Account (to get API credentials).
	•	TIDAL account (username and password).
	•	Internet connection.

Installation

	1.	Clone this repository:

git clone https://github.com/your-username/spotify-tidal-sync.git
cd spotify-tidal-sync


	2.	Install dependencies:

pip install spotipy tidalapi python-dotenv


	3.	Set up a Spotify Developer App:
	•	Go to the Spotify Developer Dashboard.
	•	Create a new app and retrieve your:
	•	Client ID
	•	Client Secret
	•	Set the Redirect URI to: http://localhost:8888/callback.
	4.	Create a .env file:
	•	In the same directory as the script, create a .env file and add your credentials:

SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
SPOTIFY_REDIRECT_URI=http://localhost:8888/callback
TIDAL_USERNAME=your_tidal_username
TIDAL_PASSWORD=your_tidal_password

Usage

	1.	Run the script:

python3 secure_sync.py


	2.	The script will:
	•	Fetch all playlists saved to your Spotify account.
	•	Retrieve tracks from each playlist.
	•	Check for duplicates in your TIDAL favorites.
	•	Add missing tracks to TIDAL.
	3.	Example Output:

Fetching all saved Spotify playlists...
Found 3 playlists.
Processing playlist: Chill Vibes (Owner: Your Name)
Fetching existing TIDAL tracks...
Syncing playlist 'Chill Vibes' to TIDAL...
Added to TIDAL: Track Name by Artist Name
Skipping (already in TIDAL): Another Track by Another Artist

Security Best Practices

	•	Secure Credentials: All credentials are stored in a .env file. Do not hardcode sensitive information in the script.
	•	Protect Your .env File: Add .env to .gitignore to prevent accidental uploads:

.env


	•	Rotate Credentials Regularly: Change your Spotify API keys and TIDAL passwords periodically for added security.

Automation (Optional)

macOS/Linux

Use cron to run the script periodically:
	1.	Edit your cron jobs:

crontab -e


	2.	Add a line to run the script daily at 3 AM:

0 3 * * * python3 /path/to/secure_sync.py >> /path/to/sync_log.txt 2>&1



Windows

Use Task Scheduler to automate the script.

Troubleshooting

	•	Missing Environment Variables:
	•	Ensure all required variables are in your .env file.
	•	Double-check variable names and values.
	•	API Rate Limits:
	•	The script includes a small delay (time.sleep(0.1)) to avoid hitting TIDAL’s rate limits. Adjust as needed.
	•	Track Not Found:
	•	If some tracks are not found on TIDAL, it might be due to differences in metadata between Spotify and TIDAL.

License

This project is licensed under the MIT License.
