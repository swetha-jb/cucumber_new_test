# BDD Selenium Framework

## How to Use

1. Install dependencies:
```
pip install -r requirements.txt
```

2. Run the tests:
```
behave
```

3. Generate Allure Report (optional):
```
behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results
allure serve reports/allure-results
```