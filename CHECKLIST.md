# PullPatrol test checklist

## Setup
1. Create a NEW test repository on GitHub (personal account, not an org).
2. Install the PullPatrol GitHub App on it and connect it in the dashboard.
3. Commit a starting file (e.g. README.md) to `main`.
4. Create a branch, add ALL files from this folder, push, open a Pull Request.
   (GitHub "push protection" may block the fake secrets. If it does, allow
   them for this test repo, since they are fake.)

## Expected results

| Check | Expected |
|---|---|
| Webhook received | A run appears on the dashboard as Pending, then Running |
| Run finishes | Status becomes Completed (not Failed) within about 5 min |
| `bandit_issues.py` | About 9-10 Bandit findings (password, shell=True, eval, pickle, md5, yaml.load, verify=False, SQL string, 0.0.0.0/debug) |
| `pylint_issues.py` | Pylint findings: unused imports/variables, naming, docstrings, too many arguments, undefined name, comparison to None |
| `eslint_issues.js` | ESLint findings: no-var, no-unused-vars, eqeqeq, no-eval, no-undef |
| `secrets_test.py` / `secrets_test.js` | TruffleHog/GitLeaks flag AWS key, GitHub token, DB URL, private key |
| Secret masking | Secret values appear MASKED in the dashboard, comments and LLM input |
| `clean_file.py` | NO findings |
| `ignored_dir/ignored_issues.py` | NO findings (ignore_paths works) |
| Skipped scanners | None skipped (if "out of memory" appears, memory is still too low) |
| Explanations | Each finding has a plain-English explanation and fix, not just the raw message |
| GitHub output | Inline PR comments plus an overall pass/fail check (expected FAIL) |
| Dashboard | Severity summary correct, filters/search work, details drawer shows summary and fix |

## Extra checks
- Remove the problem files in a new commit: the next run should PASS.
- Re-send the webhook with a wrong signature: should be rejected (HMAC).
- Log in as each of the 4 roles: each sees only its permitted repositories.
- Pause the repository, push a commit: no new run should be created.
- Stop the LLM key/service: run should still complete with raw findings.
