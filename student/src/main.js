import { createApp } from 'vue';
import Antd from 'ant-design-vue';
import App from './App';
import 'ant-design-vue/dist/antd.css';
import store from './store'
import router from './router'

const app = createApp(App).use(router).use(store).use(Antd);

app.mount('#app');
