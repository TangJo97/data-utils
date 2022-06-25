import nox

python_versions = ["3.9", "3.10"]


@nox.session(python=python_versions)
def tests(session):
    session.install("coverage[toml]")
    session.run(
        "poetry",
        "export",
        "-f",
        "requirements.txt",
        "--output",
        "requirements.txt",
        external=True,
    )
    session.install("-r", "requirements.txt")
    session.run(
        "coverage",
        "run",
        "-m",
        "unittest",
        "discover",
        "-v",
        "tests",
        external=True,
    )  # we run coverage from external env
    session.run("coverage", "report", "-m", "--omit=*/tests/*", external=True)
