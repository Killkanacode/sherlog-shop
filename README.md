# sherlog-shop

The demo shop that [Sherlog](https://github.com/Killkanacode/sherlog) watches: a small set of
services (gateway, orders, inventory, payments) whose code lives in Sherlog's `demo-app/`.

This repository is where Sherlog proposes code fixes. When a deploy ships a bug, Sherlog rolls it
back, then Muse Code writes a fix and a regression test. The fixer checks that the test fails on
the deployed code and passes with the fix, and opens a pull request here:

- `sherlog/deployed-<version>`: the code exactly as it was deployed.
- `sherlog/fix-incident-<id>-...`: the fix on top of it, for a human to review.

Nothing here is merged automatically.
