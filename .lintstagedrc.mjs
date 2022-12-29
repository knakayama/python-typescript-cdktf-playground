import micromatch from 'micromatch'
import { globby } from 'globby'
import path from 'path'
import { fileURLToPath } from 'url'

const appDirs = async () =>
  globby(path.join(path.dirname(fileURLToPath(import.meta.url)), 'app'), {
    onlyDirectories: true,
    deep: 1,
  })

export default async (files) => [
  ...[
    'prettier --fix --ignore-unknown',
    'yarn lint:ec',
    'yarn gitleaks',
    'eslint --fix',
  ].map((cmd) => `${cmd} ${files.join(' ')}`),
  ...(await appDirs()).flatMap((appDir) =>
    [
      `poetry run -C ${appDir} ruff --fix`,
      `poetry run -C ${appDir} black`,
      `poetry run -C ${appDir} mypy`,
    ].map(
      (cmd) =>
        `${cmd} ${micromatch(files, path.join(appDir, '**/*.py')).join(' ')}`
    )
  ),
]
