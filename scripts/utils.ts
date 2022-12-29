import { fileURLToPath } from 'url'
import 'zx/globals'

export const appDirs = async (): Promise<string[]> =>
  glob(path.join(path.dirname(fileURLToPath(import.meta.url)), '../app'), {
    onlyDirectories: true,
    deep: 1,
  })
