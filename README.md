# Travel Website

## Environement setup

First clone this repository and get the `MapsAPIKey.txt` API key from the repository owner.

To run this app first create a new conda environment by running the following on the command line.

```
conda env create -n travel_site -f environment.yml
conda activate travel_site
```

To run the app switch to the route directory and run the following.

```
flask --app app_runner run
```

