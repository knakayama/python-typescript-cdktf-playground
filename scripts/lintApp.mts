#!/usr/bin/env zx

import { $ } from 'zx'
import 'zx/globals'
import { appDirs } from './utils.js'
;(await appDirs()).forEach(async (appDir) => {
  echo(chalk.blue(`cd to ${appDir}`))
  cd(appDir)
  await $`poetry run poe lint`
})
