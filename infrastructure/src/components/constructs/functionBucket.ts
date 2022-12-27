import { S3Bucket } from '@cdktf/provider-aws/lib/s3-bucket'
import { S3BucketLoggingA } from '@cdktf/provider-aws/lib/s3-bucket-logging'
import { S3BucketOwnershipControls } from '@cdktf/provider-aws/lib/s3-bucket-ownership-controls'
import { S3BucketPublicAccessBlock } from '@cdktf/provider-aws/lib/s3-bucket-public-access-block'
import { S3BucketVersioningA } from '@cdktf/provider-aws/lib/s3-bucket-versioning'
import { Construct } from 'constructs'
import { uniqueId } from '../../modules/utils'

export interface FunctionBucketProps {
  bucketName: string
}

export class FunctionBucket extends Construct {
  constructor(
    readonly scope: Construct,
    readonly name: string,
    { bucketName }: FunctionBucketProps
  ) {
    super(scope, name)


    const bucket = new S3Bucket(
      this,
      uniqueId({
        prefix: S3Bucket,
        suffix: 'tf_state',
      }),
      {
        bucket: bucketName,
      }
    )

    new S3BucketOwnershipControls(
      this,
      uniqueId({
        prefix: S3BucketOwnershipControls,
        suffix: 'session_log',
      }),
      {
        bucket: bucket.id,
        rule: {
          objectOwnership: 'BucketOwnerEnforced',
        },
      }
    )

    new S3BucketVersioningA(
      this,
      uniqueId({
        prefix: S3BucketVersioningA,
        suffix: 'tf_state',
      }),
      {
        bucket: bucket.id,
        versioningConfiguration: {
          status: 'Enabled',
        },
      }
    )

    new S3BucketPublicAccessBlock(
      this,
      uniqueId({
        prefix: S3BucketPublicAccessBlock,
        suffix: 'tf_state',
      }),
      {
        bucket: bucket.id,
        blockPublicAcls: true,
        blockPublicPolicy: true,
        ignorePublicAcls: true,
        restrictPublicBuckets: true,
      }
    )

    new S3BucketLoggingA(
      this,
      uniqueId({
        prefix: S3BucketLoggingA,
        suffix: 'tf_state',
      }),
      {
        bucket: bucket.id,
        targetBucket: bucket.id,
        targetPrefix: 'access-log/',
      }
    )
  }
}
