<br/>
<p align="center">
  <a href="https://github.com/julianpyrlik/Spotify-Playlist-Creator">
    <img src="https://cdn-icons-png.flaticon.com/512/174/174872.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Spotify Playlist Creator</h3>

  <p align="center">
    Create your playlist in seconds.
    <br/>
    <br/>
    <a href="https://github.com/julianpyrlik/Spotify-Playlist-Creator"><strong>Explore the docs »</strong></a>
    <br/>
    <br/>
    <a href="https://github.com/julianpyrlik/Spotify-Playlist-Creator">View Demo</a>
    .
    <a href="https://github.com/julianpyrlik/Spotify-Playlist-Creator/issues">Report Bug</a>
    .
    <a href="https://github.com/julianpyrlik/Spotify-Playlist-Creator/issues">Request Feature</a>
  </p>
</p>

![Downloads](https://img.shields.io/github/downloads/julianpyrlik/Spotify-Playlist-Creator/total) ![Contributors](https://img.shields.io/github/contributors/julianpyrlik/Spotify-Playlist-Creator?color=dark-green) ![Issues](https://img.shields.io/github/issues/julianpyrlik/Spotify-Playlist-Creator) ![License](https://img.shields.io/github/license/julianpyrlik/Spotify-Playlist-Creator) 

## Table Of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Installation](#installation)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Authors](#authors)
* [Acknowledgements](#acknowledgements)

## About The Project

This script helps you create a Spotify playlist of Billboard Hot 100 songs for a specific year. It retrieves song titles by webscraping Billboard's website and then searches for those songs on Spotify, adding them to a new playlist.

## Built With

Python
Spotify API

## Getting Started


### Installation

1. Install the required libraries:

2. Create a Spotify app and obtain your client_id, client_secret, and redirect_uri. You can do this by following the instructions here: https://developer.spotify.com/

3. Create a file named .env in the same directory as your script and add your Spotify credentials.

How it Works

The script asks the user for the desired year.

It constructs a URL for the Billboard Hot 100 chart for that year.

It uses the requests library to fetch the webpage content.

It uses Beautiful Soup to parse the HTML and extract the song titles.

It authenticates with the Spotify API using your credentials stored in the .env file.

It searches for each song title on Spotify and retrieves the corresponding URI.

It creates a new private playlist on your Spotify account.

Finally, it adds the retrieved song URIs to the newly created playlist.


## Roadmap

See the [open issues](https://github.com/julianpyrlik/Spotify-Playlist-Creator/issues) for a list of proposed features (and known issues).

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.
* If you have suggestions for adding or removing projects, feel free to [open an issue](https://github.com/julianpyrlik/Spotify-Playlist-Creator/issues/new) to discuss it, or directly create a pull request after you edit the *README.md* file with necessary changes.
* Please make sure you check your spelling and grammar.
* Create individual PR for each suggestion.
* Please also read through the [Code Of Conduct](https://github.com/julianpyrlik/Spotify-Playlist-Creator/blob/main/CODE_OF_CONDUCT.md) before posting your first idea as well.

## License

Distributed under the MIT License. See [LICENSE](https://github.com/julianpyrlik/Spotify-Playlist-Creator/blob/main/LICENSE.md) for more information.

## Authors

* **Julian Pyrlik** - ** - [Julian Pyrlik](https://github.com/julianpyrlik) - **

