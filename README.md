# Python Data Analysis Projects

A collection of data analysis projects completed during my Master of Science in Business Analytics at the University of Alabama. All projects use Python with modern data libraries.

---

## Projects

### 1. Chicago Crime Analysis (`Faith_Elrod_2025-11-04_Crime_assignment.py`)
**Course:** Business Analytics, Fall 2025

Analyzed over 20 years of Chicago crime data (2001–2025) to identify patterns in violent crime distribution across city districts.

**Key Tasks:**
- Parsed and transformed datetime columns using Polars
- Classified crime types into violent and non-violent categories
- Identified the Top 5 most violent districts in 2024
- Broke down violent crime by type per district
- Found the Top 10 beats by homicide count
- **Bonus:** Built an interactive homicide heat map using Plotly and OpenStreetMap

**Libraries:** `polars`, `plotly`, `marimo`

---

### 2. 2017 NCAA Football Analysis (`2017_NCAA_Football_assignment_v2.py`)
**Course:** Business Analytics, Fall 2025

Analyzed 2017 NCAA college football season data to uncover team and game performance trends.

**Libraries:** `polars` / `pandas`, `plotly`

---

### 3. Iowa Analysis (`Faith_Iowa.py`)
**Course:** Business Analytics, Fall 2025

Data analysis project focused on Iowa-related dataset exploration and visualization.

**Libraries:** `polars` / `pandas`, `plotly`

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.x | Core language |
| Polars | Fast DataFrame manipulation |
| Plotly Express | Interactive visualizations |
| Marimo | Reactive notebook environment |

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/python-data-analysis.git
   ```
2. Install dependencies:
   ```bash
   pip install polars plotly marimo
   ```
3. Run a script directly or open in Marimo:
   ```bash
   marimo edit Faith_Elrod_2025-11-04_Crime_assignment.py
   ```

> **Note:** The Chicago crime project requires the `chicago_crime_2001_2025.parquet` dataset, which is not included in this repo due to file size.

---

## Author
**Faith Elrod** | MS Business Analytics, University of Alabama  
[LinkedIn](https://linkedin.com/in/faithelrod) | faith.elrod03@gmail.com
