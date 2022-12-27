import { App } from 'cdktf'
import { API } from './components/stacks/api'

const app = new App()

new API(app, 'api')

app.synth()
