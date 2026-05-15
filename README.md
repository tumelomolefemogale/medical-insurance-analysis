# U.S. Medical Insurance Cost Analysis
 
A data analysis project exploring a U.S. medical insurance dataset using Python's built-in `csv` module — no external libraries.
 
## Dataset
 
`insurance.csv` — 1,338 patient records with the following fields:
 
| Column | Description |
|---|---|
| `age` | Patient's age |
| `sex` | Patient's sex (`male` / `female`) |
| `bmi` | Body Mass Index |
| `children` | Number of dependents |
| `smoker` | Smoking status (`yes` / `no`) |
| `region` | U.S. region (`southwest`, `southeast`, `northwest`, `northeast`) |
| `charges` | Annual insurance charges (USD) |
 
## Analysis
 
The project answers the following questions:
 
1. What is the average insurance charge across all patients?
2. How many unique regions are there, and how many patients are in each?
3. What are the ages of the oldest and youngest patients?
4. What is the average charge for smokers vs. non-smokers?
5. Which patient pays the most, and what is their profile?
6. What is the average BMI per region?
7. What percentage of patients are smokers?
8. What are the average charges by age group (18–30, 31–45, 46–59, 60+)?
9. Who pays more on average — males or females? Does that change when controlling for smoking status?
## Usage
 
1. Clone the repository and ensure `insurance.csv` is in the same directory as the script.
2. Run the script:
```bash
python analysis.py
```
 
## Requirements
 
- Python 3.x
- No external dependencies
## Project Structure
 
```
.
├── analysis.py       # Main analysis script
├── insurance.csv     # Dataset
└── README.md         # Project documentation
```
