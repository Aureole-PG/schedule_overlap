## Run project

Clone

```bash
  git clone https://github.com/Aureole-PG/schedule_overlap.git
```

Create environment

```bash
  python -m venv venv
```

Activate environment **Windows**

```bash
.\venv\scripts\activate
```

Activate environment **Linux**

```bash
source venv/bin/activate
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Run application

```bash
  python main.py
```

## Running Tests

To run tests, run the following command

```bash
python -m pytest -v
```

## Architecture

I used clean architecture to do this application and for the tests I used AAA patron with pytest

## Code

#### Domain

- User
- Schedule

#### Controller

**Parser:** it recibe a string as parameter, its use find function to find the separator between name and schedule then use split for schedules and saved with its classes

**Compare:** it use permutation to agrupate pair users then for each iteration counts coincidences between users.

for the coincidences should be have two parameters, `schedule` and `schedule_to_compare`, the function does iterate first one then filter the second one by day then it filter with schedule overlap contidion and return a number of coincidences in that day

#### Infrastructure

**Read file:** it reads txt file and return a string list

#### main.py

it generate a list with user and schedule data, then use compare function to get and shows the result
