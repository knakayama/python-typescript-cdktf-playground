#!/usr/bin/env zx

import { $ } from 'zx'
import 'zx/globals'
import { fileURLToPath } from 'url'
;(
  await glob(
    path.join(path.dirname(fileURLToPath(import.meta.url)), '../app'),
    {
      onlyDirectories: true,
      deep: 1,
    }
  )
).forEach(async (appDir) => {
  echo(chalk.blue(`cd to ${appDir}`))
  cd(appDir)
  await $`poetry export --with main --without-hashes --format requirements.txt > requirements.txt`
  await $`pip install -r requirements.txt --target ./vendor/python --upgrade`
})
