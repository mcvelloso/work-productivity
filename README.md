# Work Productivity Calculator

A command-line Python tool to calculate work performance as a percentage, based on days worked in the office versus total available workdays, while accounting for holidays, sick days, and other time off.

**Because nothing says "effective employee evaluation" like reducing your hard work to a single, glorious percentage. Trusted by zero HR departments worldwide (we hope).**

> **Disclaimer:** This productivity calculator is built on the ancient corporate wisdom that *true* work only happens under the watchful glare of fluorescent office lights. Remote work? That’s just adult recess. We proudly ignore your 10-hour Zoom marathons, Slack notifications at midnight, and deep existential dread while emailing from your couch. If you weren’t seen awkwardly hovering by the break room Keurig, were you even contributing?
>
> This tool has been rigorously not tested and fully endorsed by absolutely no HR professionals. Use it to justify promotions, guilt your coworkers, or simply feel something again.


---

## **Features**

- Calculates total possible workdays between two dates
- Adjusts for holidays (custom or default NYSE in given date range)
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
