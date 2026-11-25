# Funniest One-Line Out-of-Office Reply

[![bounty](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)
[![rank](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/konzlodon74-dot/oooreply/rank.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)
[![reward](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/konzlodon74-dot/oooreply/reward.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)

Entry for the [make.fun bounty "Funniest One-Line Out-of-Office Reply"](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8).

## What it does

`main.py` writes a single-line out-of-office auto-reply to `/output/entry.txt`. The program uses only the Python standard library, makes no network calls, and is fully deterministic — every run produces byte-identical output. It validates that the line is non-empty, single-line, and at most 160 characters before writing.

The entry line is:

> Out of office until Monday — laptop closed, brain on airplane mode, inbox officially your problem now.

## Run

```bash
python3 main.py
cat /output/entry.txt
```
