* First run the `prepare.sh` to copy the folders `src/`, `settings/` and `requirements.txt` into the package `routine/`:
```
./scripts/prepare.sh
```

* In a terminal, run the following command to deploy to Digital Ocean:
```
doctl serverless deploy .
```