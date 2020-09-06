import bs4
import pycodestyle

assert bs4.__version__ == "4.9.1", "beautifulsoup version incorrect."
assert pycodestyle.__version__ == "2.6.0", "pycodestyle version incorrect."

# Check the coding style without any output
report = pycodestyle.BaseReport(options=pycodestyle.StyleGuide().options)
pycodestyle.Checker(filename=bs4.__file__, report=report).check_all()
statistics = sorted(report.get_statistics())

print("".join(statistics[row][column] for row, column in [
    (2, 39),
    (3, 13),
    (4, 22),
    (5, 36),
    (6, 39),
    (7, 17),
    (6, 21),
    (7, 35),
    (8, 14),
    (9, 22),
    (10, 20),
    ]))
