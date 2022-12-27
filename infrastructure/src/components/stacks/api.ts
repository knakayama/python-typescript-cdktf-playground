import { Construct } from 'constructs'
import { S3Backend, TerraformStack } from 'cdktf'
import { FunctionBucket } from '../constructs/functionBucket'
import { AwsProvider } from '@cdktf/provider-aws/lib/provider'
import { backendStorageProps, project, region } from '../../modules/utils/constants'
import { Function } from '../constructs/function'

export class API extends TerraformStack {
  constructor(
    readonly scope: Construct,
    readonly name: string,
    ) {
    super(scope, name)

    new AwsProvider(this, 'aws', {
      region,
      defaultTags: {
        tags: {
          Name: project,
        },
      },
    })

    new S3Backend(this, {
      ...backendStorageProps,
      key: `${project}/api.tfstate`
    })

    const bucketName = 'knakayama-function-bucket'
    new FunctionBucket(this, 'function_bucket', {
      bucketName,
    })

    new Function(this, 'function', {
      bucketName,
    })
  }
}
