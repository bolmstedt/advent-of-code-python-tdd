python_sources(
    dependencies=[":templates", ":solutions", "vendor#more-itertools"],
)

python_tests(name="tests")

pex_binary(
    name="cli",
    entry_point="cli.py",
)

files(
    name="templates",
    sources=["templates/*"],
)

files(
    name="solutions",
    sources=["year_*/**/*"],
)
