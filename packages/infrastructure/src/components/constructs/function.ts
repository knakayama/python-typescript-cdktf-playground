import { DataAwsIamPolicyDocument } from '@cdktf/provider-aws/lib/data-aws-iam-policy-document'
import { IamRole } from '@cdktf/provider-aws/lib/iam-role'
import { IamRolePolicyAttachment } from '@cdktf/provider-aws/lib/iam-role-policy-attachment'
import { LambdaFunction } from '@cdktf/provider-aws/lib/lambda-function'
import { S3Bucket } from '@cdktf/provider-aws/lib/s3-bucket'
import { S3Object } from '@cdktf/provider-aws/lib/s3-object'
import { AssetType, TerraformAsset } from 'cdktf'
import { Construct } from 'constructs'
import path = require('path')
import { uniqueId } from '../../modules/utils'

export class Function extends Construct {
  #suffix = 'function'

  constructor(
    readonly scope: Construct,
    readonly name: string,
  ) {
    super(scope, name)

    const asset = new TerraformAsset(
      this,
      uniqueId({
        prefix: TerraformAsset,
        suffix: 'lambda',
      }),
      {
        path: path.resolve(
          __dirname,
          '../../../../app/src'
        ),
        type: AssetType.ARCHIVE,
      }
    )

    const bucket = new S3Bucket(
      this,
      uniqueId({
        prefix: S3Bucket,
        suffix: 'asset',
      }),
      {
        bucketPrefix: `${this.#suffix}-`,
      }
    )

    const lambdaArchive = new S3Object(
      this,
      uniqueId({
        prefix: S3Object,
        suffix: 'asset',
      }),
      {
        bucket: bucket.bucket,
        key: `v8/${asset.fileName}`,
        source: asset.path,
      }
    )

    const role = new IamRole(
      this,
      uniqueId({
        prefix: IamRole,
        suffix: 'lambda',
      }),
      {
        assumeRolePolicy: new DataAwsIamPolicyDocument(
          this,
          uniqueId({
            prefix: DataAwsIamPolicyDocument,
            suffix: 'lambda',
          }),
          {
            statement: [
              {
                effect: 'Allow',
                actions: ['sts:AssumeRole'],
                principals: [
                  {
                    type: 'Service',
                    identifiers: ['lambda.amazonaws.com'],
                  },
                ],
              },
            ],
          }
        ).json,
      }
    )

    new IamRolePolicyAttachment(
      this,
      uniqueId({
        prefix: IamRolePolicyAttachment,
        suffix: 'basic',
      }),
      {
        policyArn:
          'arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole',
        role: role.name,
      }
    )

    new LambdaFunction(
      this,
      uniqueId({
        prefix: LambdaFunction,
        suffix: 'chat',
      }),
      {
        functionName: this.#suffix,
        s3Bucket: bucket.bucket,
        s3Key: lambdaArchive.key,
        handler: 'chatNotification.handler',
        runtime: 'nodejs16.x',
        role: role.arn,
      }
    )
  }
}
