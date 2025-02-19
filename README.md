# College Basketball - March Madness Predictive Model

## Overview
This project predicts win probabilities for college basketball games using supervised learning techniques. Additionally, it explores unsupervised learning to identify useful features that enhance prediction accuracy.

## Features
- **Win Probability Model**: Uses supervised learning to predict game outcomes.
- **Feature Discovery**: Applies unsupervised learning to identify meaningful patterns in data.
- **CSV Export**: Saves scraped data in CSV format for analysis.

## Installation
1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd <repository_name>
   ```
2. Set up a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

### Running the Prediction Model
1. Obtain Game data by visiting kenpom.com/cbbga(yy).txt
   - save file as csv, can be done by saving as a text file then changing ".txt" to ".csv" in file explorer
   - There is an xlsx reader in the file list if you just want to paste it into a cell
     
2. Run Compiler code to reformat the .csv to a clean version with proper columns for the dates/teams/scores
   - make sure to update filepaths for the input and output
     
3. Obtain Team Data:
   - I have not found a webscraping ability to automate this yet
   - To do this, visit "https://kenpom.com/archive.php?d=yyyy-mm-dd" to get the offensive and defensive ratings for each day you want to do analysis on
   - Right now the best method is to just copy and paste the table with the data and throw it into an excel. I have an example excel as "Kenpom Data"
   - Next you refill down the cells in "February Results NI" Worksheet after putting more games in, do the same for the "February Results I" sheet
   - copy the "February Results I" sheet and paste "Values", then save as a .csv. This will be the file your unsupervised and supervised learning will read.

4. Unsupervised Learning:
   - I have a few of these working right now, but for now you can use trial 1 and trial 2 to see different things. Have not organized it yet whatsoever, so bare with me
     
5. Supervised Learning:
   - Pretty straight forward, I recommend leaving the features I have in there as they are. I welcome you to mess with how many you include to just play around with it to see what happens. Again, just make sure your file path is correct to get this to work. Planning on adding shop plots and matrix to see more stuff.

## Requirements
- Python 3.x
- Pandas, NumPy, Scikit-learn

## Future Improvements

## License
This project is licensed under the MIT License.

