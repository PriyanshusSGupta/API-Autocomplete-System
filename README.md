# Autocomplete API Extraction (v1, v2, v3)

## Overview

This project involves extracting all possible names from an autocomplete API across three versions: `v1`, `v2`, and `v3`. The API endpoint structure is as follows:

```
http://35.200.185.69:8000/{version}/autocomplete?query=<string>
```

The task includes systematically querying the API to discover all possible names while respecting any constraints or limitations.

---

## Approach

### 1. **Exploration**

- The `/v1/autocomplete`, `/v2/autocomplete`, and `/v3/autocomplete` endpoints were tested using prefix-based queries.
- Each query returns a JSON response with a `results` array containing matching names.
- Empty responses indicate terminal nodes for a given prefix.


### 2. **Algorithm**

- A **Breadth-First Search (BFS)** approach was used to explore all prefixes systematically:
    - Start with all lowercase letters (`a-z`) as initial prefixes.
    - Query the API for each prefix and collect results.
    - Extend prefixes by adding one character at a time until no new results are found.
- Track visited prefixes to avoid redundant queries.


### 3. **Optimizations**

- Introduced a delay of 100ms between requests to prevent overloading the server.
- Used Python sets for O(1) lookups of visited prefixes and discovered names.

---

## Findings

### Results Summary

| Version | Total API Requests | Unique Names Found |
| :-- | :-- | :-- |
| v1 | **52** | **260** |
| v2 | **104** | **329** |
| v3 | **134** | **411** |

### Observations

1. **Prefix-based Completion**: Names are discovered by incrementally building valid prefixes.
2. **Rate Limiting**: No explicit rate limiting was encountered during testing, but a delay was added as a precaution.

---

## How to Run

### Prerequisites

1. Install Python 3.x on your system.
2. Install the required library:

```
pip install requests
```


### Steps

1. Save the script in a file named `autocomplete_extractor_v123.py`.
2. Run the script:

```
python autocomplete_extractor_v123.py
```


The script will extract names from all three versions (`v1`, `v2`, and `v3`) and display the results.

---

## Results

After running the script, you will obtain:

- Total API requests made for each version (`v1`, `v2`, `v3`).
- Total unique names extracted for each version.

---

## File Structure

```
autocomplete_extractor_v123.py   # Python script for extracting names from v1, v2, and v3
README.md                        # Documentation explaining the approach and findings
```

---

## Metrics

| Metric | v1 | v2 | v3 |
| :-- | :-- | :-- | :-- |
| Total API Requests | 52 | 104 | 134 |
| Unique Names Extracted | 260 | 329 | 411 |

---

## Notes

- The script can be extended to handle additional versions if required.
- Ensure a stable internet connection while running the script, as it makes multiple API requests.

