import { Construct } from 'constructs'
import path = require('path')
import { uniqueId } from '../../modules/utils'
import { Lambda } from '../../lib/modules/lambda'

interface FunctionProps {
  bucketName: string
}

export class Function extends Construct {
  constructor(
    readonly scope: Construct,
    readonly name: string,
    { bucketName }: FunctionProps
  ) {
    super(scope, name)

    const layer = new Lambda(this, uniqueId({
      prefix: Lambda,
      suffix: 'lambda_layer',
    }), {
      createLayer: true,
      layerName: 'my-lambda-layer',
      description: 'My lambda layer',
      compatibleRuntimes: ['python3.9'],
      sourcePath: path.join(__dirname, '../../../../app/vendor'),
      storeOnS3: true,
      s3Bucket: bucketName,
      compatibleArchitectures: [
        "arm64",
        "x86_64",
      ]
    })

    new Lambda(this, uniqueId({
      prefix: Lambda,
      suffix: 'lambda',
    }), {
      functionName: 'my-lambda',
      description: 'This is my lambda',
      handler: 'handler.handle',
      runtime: 'python3.9',
      sourcePath: path.join(__dirname, '../../../../app/app'),
      layers: [
        layer.lambdaLayerArnOutput,
      ]
    })
  }
}
