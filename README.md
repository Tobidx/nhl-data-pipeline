# NHL Data Pipeline

This project implements a data pipeline for processing NHL game and player data using the NHL API.

---

## **Features**
- **Data Cleaning**: Load, clean, and validate data from CSV files.
- **API Integration**: Fetch updated game and player data from the NHL API.
- **Data Updates**: Append or update data in existing CSV files based on input parameters.
- **DAG Implementation**: Organize processes using a Directed Acyclic Graph (DAG) structure.
- **Exception Handling**: Retry mechanisms and error logging for robust execution.

---

## **Setup Instructions**

1. Clone the Repository:
   ```bash
   git clone https://github.com/your-username/nhl-data-pipeline.git
   cd nhl-data-pipeline

2. Install Dependencies:

  Install the required Python packages using the requirements.txt file:
  ```bash
  pip install -r requirements.txt
---

## **Running the pipeline**

To process a list of game IDs and update the dataset:
 ```bash
   python src/dag_pipeline.py

***Example***
1. Modify the dag_pipeline.py script to include game IDs to process:
```python
  game_ids = ["2023020001", "2023020002"]

2. Run the pipeline:
```bash
   python src/dag_pipeline.py

3. Check the output:

The pipeline updates the CSV files in the data/ folder with new data fetched from the NHL API.
---

**Demonstration**
Below is a demonstration of how the pipeline works:

***Input***
-Sample game IDs: ["2023020001", "2023020002"]
-Original CSV files in the data/ folder.

***Execution***

-Run the command:
```bash
   python src/dag_pipeline.py

***Process***

1. The pipeline:

-Loads existing data from data/ files.
-Fetches updated game data for the specified game IDs from the NHL API.
-Cleans and validates the data.
-Appends or updates the datasets.
-Outputs the updated files back into the data/ folder.

---
***Output***

-Updated data/game_overview.csv and other relevant files.
-New records are added, and existing records are updated based on the input game IDs.

***Example Output***

-Before: data/game_overview.csv:
```
gameID,team,score
2023020001,TOR,2

-After: data/game_overview.csv:
```
gameID,team,score
2023020001,TOR,2
2023020002,BOS,4

---
**Future Improvements**

- Enhanced Validation:
Integrate schema validation for stricter data quality checks.

- Containerization:
Package the pipeline in a Docker container for portability.

-Scalability:
Use distributed processing for larger datasets or higher workloads.

