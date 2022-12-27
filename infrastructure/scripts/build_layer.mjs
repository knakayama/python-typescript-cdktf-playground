#!/usr/bin/env zx

cd(path.join(__dirname, '../../app'))
await $`poetry export --with main --without-hashes --format requirements.txt > requirements.txt`
await $`pip install -r requirements.txt --target ./vendor/python --upgrade`
