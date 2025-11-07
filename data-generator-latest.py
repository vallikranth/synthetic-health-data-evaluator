import random, time, json
import numpy as np
import pandas as pd
from scipy import stats

# ---------- Synthetic data generation ----------
def generate_patient(i):
    return {
        "patient_id": f"P{i:04d}",
        "age": random.randint(20, 90),
        "sex": random.choice(["M", "F"]),
        "serum_creatinine": round(random.uniform(0.5, 12), 2),
        "potassium": round(random.uniform(3, 7), 2),
        "egfr": round(random.uniform(5, 90), 1),
        "systolic_bp": random.randint(90, 180),
        "diastolic_bp": random.randint(60, 110),
        "heart_rate": random.randint(50, 110),
        "ultrafiltration": round(random.uniform(1.0, 5.0), 2),
        "medications": random.sample(
            ["epoetin", "calcitriol", "heparin", "iron_sucrose",
             "amlodipine", "furosemide", "sevelamer", "vitamin_d",
             "metoprolol", "cinacalcet"], k=random.randint(1,4))
    }

patients = [generate_patient(i) for i in range(1000)]

# ---------- Simple analysis ----------
tstat, pval = stats.ttest_ind(legacy_times, fhir_times)
summary = {
    "Legacy_mean_ms": np.mean(legacy_times),
    "FHIR_mean_ms": np.mean(fhir_times),
    "Mean_diff_ms": np.mean(legacy_times) - np.mean(fhir_times),
    "p_value": pval
}
print(summary)

# ---------- Example completeness metrics ----------
mapping_coverage = 0.9  # 90% of dialysis fields mapped
validation_error_rate = 0.02  # 2% bundles rejected
data_completeness = 1 - validation_error_rate

#---generate csv file
import csv
with open("results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(summary.keys())
    writer.writerow(summary.values())