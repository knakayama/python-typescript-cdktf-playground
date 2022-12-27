import { App } from 'cdktf'
import { MyStack } from './components/stacks/my'

const app = new App()
new MyStack(app, 'my_stack')
app.synth()
