import { BackendStorageProps } from "../types"

export const project = 'python-lambda-playground'
export const region = 'ap-northeast-1'
export const backendStorageProps: BackendStorageProps = {
  bucket: 'knakayama-tf-states-dev',
  encrypt: true,
  region,
  dynamodbTable: 'tf-lock-table-dev',
}
