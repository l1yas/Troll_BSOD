# Troll_BSOD

## Description
Fake calculator that tricks the user.  
After entering numbers and “calculating”, it prints a fake result (`Hello World`) and shows a scary pop-up warning **“Deleting System 32”**.  
Finally, it displays a **full-screen BSOD image**.  

**Just for fun** | it does **not delete any files**. It’s safe to run.

---

## Files
- `Troll.py` → main Python script  
- `bsod.png` → BSOD image to display  
- `requirements.txt` → Python dependencies  

---

## Dependencies
Only external dependency is **Pillow**. Tkinter is included with Python.  

Install dependencies with:

```bash
pip install -r requirements.txt
```
---

## Usage

### Clone the repository:

```bash
git clone https://github.com/YourUsername/Troll_BSOD.git
cd Troll_BSOD
```

Make sure bsod.png is in the same folder as Troll.py.

### Run the script:

```bash
python Troll.py
```
Enter numbers in the fake calculator, click OK on the warning, and watch the BSOD appear.

Press Escape to close the BSOD.

### Notes
Keep bsod.png in the same folder as Troll.py for the script to work.

The BSOD is purely visual; it does not harm your system.

License
No license or MIT (if you want to allow others to reuse).
