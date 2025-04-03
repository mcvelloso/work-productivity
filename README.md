# Work Productivity Calculator

A command-line Python tool to calculate work performance as a percentage, based on days worked versus total available workdays, while accounting for holidays, sick days, and other time off.

**Because nothing says "effective employee evaluation" like reducing your hard work to a single, glorious percentage. Trusted by zero HR departments worldwide (we hope).**

---

## **Features**

- Calculates total workdays between two dates
- Adjusts for holidays (custom or default NYSE)
- Accounts for sick days and personal days off
- Outputs a work performance percentage

---

## **Installation**

Clone the repo and install any dependencies (if required):

```bash
git clone https://github.com/yourusername/work-productivity.git
cd work-productivity
# (Optional) Setup virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt  # If needed
```

---

## **Usage**

Run the script from the terminal:

```bash
python work_productivity.py --days-in-office 120 --start-date 2024-01-01 --end-date 2024-06-01 --sick-days 3 --days-off 2
```

### **Arguments:**

| Argument | Type | Required | Description |
|----------|------|----------|-------------|
| `--days-in-office` | int | Yes | Number of days actually worked |
| `--start-date` | YYYY-MM-DD | Yes | Start date for the evaluation period |
| `--end-date` | YYYY-MM-DD | Yes | End date for the evaluation period |
| `--holidays` | int | No | Number of holidays (default: Number of NYSE holidays in the given date range) |
| `--sick-days` | int | No | Number of sick days (default: 0) |
| `--days-off` | int | No | Other time off (default: 0) |

---

## **Example Output**

```bash
Number of workdays: 108
Number of holidays: 5
Work Performance: 92.31%
```

---

## **License**

MIT License. See [LICENSE](LICENSE) for details.
