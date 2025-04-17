
# 🎬 Movie Ratings ETL Project

## 📌 Project Goal
This project was built to **practice Python basics** by developing a complete ETL (Extract, Transform, Load) pipeline using messy, semi-realistic movie ratings data. The project simulates real-world data engineering tasks: data cleaning, joining multiple data sources, transformation, validation, and finally loading into a MySQL database.

---

## 📂 Data Sources

### 1. `movies_raw.json`
- Contains movie metadata such as `id`, `title`, `genre`, `release_year`
- Includes messy records (e.g. typos, inconsistent genres, wrong year formats)

### 2. `users_raw.csv`
- Includes user details: `user_id`, `name`, `age`, `country`
- Contains duplicates, missing ages, inconsistent country naming

### 3. `ratings_raw.csv`
- Movie ratings with `rating_id`, `user_id`, `movie_id`, `rating`, `timestamp`
- Problems include invalid user/movie IDs, bad timestamp formats, invalid rating values

---

## 🔄 ETL Pipeline

### ✅ Extract
- Loaded all three datasets from local files
- Parsed JSON and CSV data into Python data structures

### ✅ Transform
- Cleaned missing or malformed data
- Standardized values (e.g., country names, genres)
- Parsed rating timestamps into `date_of_rate` and `time_of_rate`
- Validated relationships between datasets (e.g. rating’s `user_id` exists in users)
- Joined `ratings`, `users`, and `movies` to form a final enriched dataset

### ✅ Load
- Final denormalized table created with the following columns:
  - `user_name`, `user_age`, `user_country`
  - `movie_title`, `movie_genre`
  - `rating`, `date_of_rate`, `time_of_rate`
- Loaded the clean data into a **MySQL database** using Python

---

## 🧠 Skills Practiced
- Python basics (functions, conditionals, loops, file handling)
- Data exploration and cleaning (custom scripts and logic)
- Working with structured and semi-structured data (CSV & JSON)
- Joining datasets, validating data integrity
- Using `pandas`, `datetime`, and basic SQL
- Connecting Python to MySQL and inserting data programmatically

---

## 📌 Next Steps
- Automate the pipeline (via schedule or Airflow)
- Add unit tests for transformations and validations
- Create a dashboard to visualize the loaded data

---

## 📁 Folder Structure (Example)
```
.
├── data/
│   ├── movies_raw.json
│   ├── ratings_raw.csv
│   └── users_raw.csv
├── etl_script.ipynb
├── data_exploring.py
└── README.md
```

---

## 👏 Author
This project was created as a foundational step toward becoming a **Data Engineer** by practicing and mastering Python basics in real-world scenarios.
