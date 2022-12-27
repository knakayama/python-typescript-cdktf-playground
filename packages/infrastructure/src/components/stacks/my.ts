import { Construct } from 'constructs'
import { TerraformStack } from 'cdktf'
import { AwsProvider } from '@cdktf/provider-aws/lib/provider'
import {
  region,
} from '../../modules/utils/constants'
import { Function } from '../constructs/function'

export class MyStack extends TerraformStack {
  constructor(scope: Construct, name: string) {
    super(scope, name)

    new AwsProvider(this, 'aws', {
      region,
      defaultTags: {
        tags: {
          Name: 'my-stack',
        },
      },
    })

    new Function(this, 'function')
  }
}
