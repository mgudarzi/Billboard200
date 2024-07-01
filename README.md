
# Billboard Chart Analyzer

This script analyzes data from a Billboard chart HTML file to provide insights into song rankings.

## Features

- **get_top_5_pos_change**: Returns the top 5 songs with the highest positive change in position from last week to this week.
- **get_peak_at_1**: Returns a list of songs that peaked at number 1 on the chart.
- **get_songs_gt_weeks**: Returns songs that have been on the chart for more than a specified number of weeks.

## Usage

1. **Requirements**:
   - Python 3.x
   - BeautifulSoup (`pip install beautifulsoup4`)

2. **Running the Script**:
   - Ensure you have Python installed.
   - Install BeautifulSoup if not already installed (`pip install beautifulsoup4`).
   - Place your Billboard chart HTML file (`BillboardGlobal200-2021.html`) in the same directory as this script.

3. **Executing the Script**:
   - Run the script `python script_name.py`.
   - Results will be printed for each function call.

4. **Testing**:
   - Unit tests are provided in `TestAllMethods` to validate the functionality of each method.
   - Run tests using `unittest` framework: `python script_name.py -v`.

5. **Additional Notes**:
   - Modify the file name in `main()` if your HTML file has a different name.
   - Feel free to adapt and extend these functions for other analyses or data sources.
