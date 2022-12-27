import { S3BackendProps } from 'cdktf'
import { Except } from 'type-fest'

export type BackendStorageProps = Except<S3BackendProps, 'key'>
