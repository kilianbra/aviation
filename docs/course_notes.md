# Course Notes

## Development Tools

- Consider adding an extension like `prettier`
- `sudo` = superuser do
- `bin` stands for binary
- Use of virtual environments (`venv`) is worth it!
- `source` is the bash utility that allows us to run files

## Git Commands

- Don't want to have git environment to be on the same
- Create new branch: `git switch -c BRANCH-NAME-HERE-REPLACE`
- Create empty file: `touch FILENAME` creates a file with that name

## MkDocs

- View all options: `mkdocs --help` or `mkdocs serve --help`
- Stop server: Control+C (Windows and Linux)
- `mkdocs.yml` is there for us to specify config for mkdocs

## Git PR Workflow

For a new PR push a local branch that doesn't have a PR to this to upstream tracking:

### Git Commands and Environment

- Keep Git environments separate for different projects
- Create new branch: `git switch -c <branch-name>`
- Create empty file: `touch <filename>`
- Push new branch upstream: `git push -u origin <branch-name>`

### Package Management

#### Legacy Package Management

- `requirements.txt` was traditionally used to specify dependencies
- Installed via `pip install -r requirements.txt`
- Now replaced by modern tools like `uv`

#### Semantic Versioning (e.g. 1.6.1)

- **Patch number** (last digit): Bug fixes and security updates that shouldn't break code
- **Minor version** (middle digit): New features and functionality
- **Major version** (first digit): Breaking changes

#### Version Specifiers

- Exact version: `mkdocs==1.6.1`
- Version range: `mkdocs>=1.6.1,<2` (pip selects newest compatible version)
- Dependencies between packages can cause version conflicts

### MkDocs Usage

- View all options: `mkdocs --help` or `mkdocs serve --help`
- Stop server: `Ctrl+C` (Windows and Linux)
- Configuration file: `mkdocs.yml` specifies MkDocs settings

### Pytest usage

Run tests with pytest:

- Run all tests: `uv run pytest`
- Run tests in specific file: `uv run pytest folder/specific_test.py`
- Run specific test: `uv run pytest folder/specific_test.py::test_name`

### Pytest Parametrization

- Use `import pytest` to enable parametrization
- Add `@pytest.mark.parametrize` decorator before test functions
- Example usage for testing function:
  ```python
  passengers_per_day(passengers_per_year, days_per_year)
  ```
- `@pytest.mark.parametrize` allows multiple test cases

#### Test Values

- Can use specific pre-calculated values
- Or run function once to determine expected values

#### Test File Naming

- Pytest won't find files named like `fleet_test.py`
- Must follow pytest naming conventions

#### Style Tips

- Adding trailing commas in lists enables cleaner diffs:
  ```python
  my_list = [
      'item1',
      'item2',
      'item3',  # Note trailing comma
  ]
  ```
- Double click failed tests in output to jump to location

#### Approximate Comparisons

- `pytest.approx` supports two types of tolerances:
  - Absolute tolerance (fixed number)
  - Relative tolerance (percentage of value, e.g. 10%)
