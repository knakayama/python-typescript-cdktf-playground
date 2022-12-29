#!/usr/bin/env yarn run ts-node-esm --swc

import { $ } from 'zx'
import 'zx/globals'
import { appDirs } from './utils.js'
;(await appDirs()).forEach(async (appDir) => {
  echo(chalk.blue(`cd to ${appDir}`))
  cd(appDir)
  await $`poetry install`
})
