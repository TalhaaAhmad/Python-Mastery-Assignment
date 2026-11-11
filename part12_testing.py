# Name: Talha Ahmad | Roll No: TRN-2026-000347 | Date: 11-11-2026
# Part 12 - Debugging and testing (Warm-up: fix 3 bugs)
# The tests are in test_grades.py (Build) and test_bank.py (Challenge)

marks = [90, 25, 70]
passing = []
for m in range(len(marks)):          # Bug 1 fixed (was range(len(marks) - 1))
    if marks[m] >= 33:               # 33 is a pass in my Part 2 grade table
        passing.append(marks[m])     # Bug 2 fixed (was passing = [marks[m]])
print(sum(passing) / len(passing))   # Bug 3 fixed (was divided by len(marks))

# Bug 1: logic bug (off-by-one). The loop stopped one item early, so the
#        last mark (70) was never checked.
# Bug 2: logic bug. "passing = [...]" threw away the old list each time,
#        so it only kept one mark. It should add with append().
# Bug 3: logic bug. It divided by all marks (3) instead of only the
#        passing marks (2). Correct answer is (90 + 70) / 2 = 80.0
# (None of them stopped the program with an error, so they are not syntax
#  or runtime errors - they just gave a wrong answer.)
