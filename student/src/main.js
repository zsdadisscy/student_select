import router from "./router";
import { createApp } from 'vue';
import Antd from 'ant-design-vue';
import App from './App';
import 'ant-design-vue/dist/antd.css';
import store from './store'

const app = createApp(App).use(store).use(Antd).use(router);

app.mount('#app');
