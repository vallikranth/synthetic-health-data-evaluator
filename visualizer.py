import matplotlib.pyplot as plt
import numpy as np

# Simulated data (you can replace these with real latency values)
legacy_times = np.random.normal(182, 29, 100)
fhir_times = np.random.normal(94, 19, 100)

plt.boxplot([legacy_times, fhir_times], labels=['Legacy API', 'FHIR API'])
plt.ylabel("Response Time (ms)")
plt.title("Latency Comparison: Legacy vs FHIR")
plt.show()
