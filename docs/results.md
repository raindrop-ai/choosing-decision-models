# Baseline results

These tables summarize the recorded outcomes. Recompute their underlying CSVs with `python3 baseline.py summarize`; the new files go to `.local/summaries/`.

## Overall accuracy

| Model | Correct / answered | Accuracy | Answered / selected |
| --- | ---: | ---: | ---: |
| Astra | 999 / 1005 | 99.4% | 1005 / 1005 |
| Opus 5.5 | 997 / 1003 | 99.4% | 1003 / 1005 |
| GLiDE v1.2 | 954 / 1005 | 94.9% | 1005 / 1005 |
| Decider v1.1 | 919 / 1005 | 91.4% | 1005 / 1005 |
| Jev | 892 / 1005 | 88.8% | 1005 / 1005 |
| Microsoft Decision-1 | 846 / 1004 | 84.3% | 1004 / 1005 |
| Clef | 835 / 1005 | 83.1% | 1005 / 1005 |
| Luna Decisions | 777 / 997 | 77.9% | 997 / 1005 |
| Clef Flash | 768 / 1005 | 76.4% | 1005 / 1005 |
| Strands Decider | 678 / 1005 | 67.5% | 1005 / 1005 |
| GLiNER2.5 Decide | 429 / 1005 | 42.7% | 1005 / 1005 |
| Laya | 416 / 1005 | 41.4% | 1005 / 1005 |
| CalDec v1 | 408 / 1005 | 40.6% | 1005 / 1005 |

## Errors on binary questions

The selected subset has [214 source-defined binary questions](../questions/binary-subset.md), including 15 with adapted choice representations. Each source's positive label is retained. Failed requests and refusals are excluded from confusion counts and lower answered coverage.

| Model | False alarms | Missed detections | Precision | Recall |
| --- | ---: | ---: | ---: | ---: |
| Astra | 2 | 1 | 97.8% | 98.9% |
| Opus 5.5 | 1 | 0 | 98.9% | 100.0% |
| GLiDE v1.2 | 1 | 6 | 98.8% | 93.4% |
| Decider v1.1 | 5 | 9 | 94.3% | 90.1% |
| Jev | 5 | 3 | 94.6% | 96.7% |
| Microsoft Decision-1 | 8 | 9 | 91.1% | 90.1% |
| Clef | 4 | 9 | 95.3% | 90.1% |
| Luna Decisions | 17 | 24 | 79.8% | 73.6% |
| Clef Flash | 3 | 12 | 96.3% | 86.8% |
| Strands Decider | 27 | 25 | 71.0% | 72.5% |
| GLiNER2.5 Decide | 57 | 25 | 53.7% | 72.5% |
| Laya | 43 | 45 | 51.7% | 50.5% |
| CalDec v1 | 54 | 43 | 47.1% | 52.7% |

## Costs and prediction times

### Self-hosted models

All eight models ran on the same physical NVIDIA A100 80GB PCIe, one prediction at a time. Timing summaries exclude each model's first forward with kernel startup; every answer still counts toward accuracy. See [measurement conditions and definitions](methods.md#saved-costs-and-timings).

| Model | Median prediction time | p95 prediction time |
| --- | ---: | ---: |
| GLiDE v1.2 | 137 ms | 481 ms |
| Decider v1.1 | 145 ms | 488 ms |
| Clef | 190 ms | 849 ms |
| Clef Flash | 99 ms | 292 ms |
| Strands Decider | 93 ms | 195 ms |
| GLiNER2.5 Decide | 39 ms | 165 ms |
| Laya | 26 ms | 33 ms |
| CalDec v1 | 27 ms | 35 ms |

### Hosted models

We accessed the hosted models through Vercel AI Gateway. Costs show model inference charges for the recorded inputs, excluding Vercel AI Gateway fees. API request times include network travel and routing; GPU-worker timings measure prediction after model loading.

| Model | Median request time | p95 request time | Model cost / 1,000 priced requests |
| --- | ---: | ---: | ---: |
| Astra | 3217 ms | 5801 ms | $7.319 |
| Opus 5.5 | 1753 ms | 3906 ms | $4.633 |
| Jev | 219 ms | 360 ms | $0.028 |
| Microsoft Decision-1 | 330 ms | 506 ms | $0.015 |
| Luna Decisions | 375 ms | 650 ms | $0.045 |

CSV downloads: [overall](../summaries/overall.csv), [by capability](../summaries/capabilities.csv), [binary outcomes](../summaries/native_binary.csv), [saved costs and timings](../summaries/cost_timing.csv).

[Browse individual questions and model answers](../questions/README.md).
