import { Construct } from 'constructs'

export class Function extends Construct {
  constructor(
    readonly scope: Construct,
    readonly name: string,
  ) {
    super(scope, name)
  }
}
