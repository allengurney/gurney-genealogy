# Repository maintenance tasks

Durable context for maintenance-shaped items tracked in the research-leads
catalog so they are not lost between cleanup threads.

## Remove the Social Security number from Git history

The current tree excludes
`sources/media/gurney-family-papers-g3-to-g2-certificates-clippings/Scanned_20260603-2257-12.jpg`
from GitHub and omits its Social Security number from the searchable corpus
extract. Earlier commits still contain the scan and identifier.

The eventual task (lead L-169) is a coordinated history rewrite that removes only scan 12
and the literal Social Security number from every reachable commit, followed
by a force-push and fresh-clone verification. The remaining 29 family-paper
scans are approved for GitHub and must not be removed. This is moderate
housekeeping rather than an emergency because the record concerns a
long-deceased person.
