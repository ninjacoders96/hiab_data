import pandas as pd
import requests
from tqdm import tqdm
from runtime_keys_hiab import api_path, headers

# -------- CONFIG --------
INPUT_FILE = "input.xlsx"
OUTPUT_FILE = "output.xlsx"
LOOKUP_COL = "Moffett number"
RESULT_COL = "Moffett List"

df = pd.read_excel(INPUT_FILE)

if RESULT_COL not in df.columns:
    df[RESULT_COL] = None

for idx, row in tqdm(df.iterrows(), total=len(df)):
    code = str(row.get(LOOKUP_COL)).strip()

    if not code or code.lower() == "nan":
        continue

    try:
        r = requests.get(
            api_path(code),
            headers=headers(),
            timeout=30
        )

        if r.status_code == 200:
            payload = r.json()
            price = (
                payload.get("details", {})
                .get("priceInfo", {})
                .get("price")
            )
            df.at[idx, RESULT_COL] = price if price else "Not Found"
        else:
            df.at[idx, RESULT_COL] = "Not Found"

    except Exception:
        df.at[idx, RESULT_COL] = "Not Found"

df.to_excel(OUTPUT_FILE, index=False)
print(f"Updated Excel saved: {OUTPUT_FILE}")
