<template>
  <div style="display: flex; flex-direction: column">
    <div style="display: flex; justify-content: space-between">
      <div style="width: 400px; float: left">
        <div v-if="cfg.notice" v-html="cfg.notice"></div>
      </div>
      <div v-if="cfg.show_github" style="margin: 12px 20px">
        <a href="https://nimble.uno" target="_blank" style="float: right">
          <svg
            width="32"
            height="32"
            t="1718179802093"
            class="icon"
            viewBox="0 0 1024 1024"
            version="1.1"
            xmlns="http://www.w3.org/2000/svg"
            p-id="4235"
          >
            <path
              d="M13.9931 3.43368C12.8564 2.42331 11.1436 2.42331 10.0069 3.43368L2.33565 10.2526C1.92286 10.6195 1.88568 11.2516 2.2526 11.6644C2.61952 12.0771 3.25159 12.1143 3.66437 11.7474L4.00001 11.4491L4.00001 17.0658C3.99996 17.9523 3.99992 18.7161 4.08215 19.3278C4.17028 19.9833 4.36903 20.6117 4.87869 21.1213C5.38835 21.631 6.0167 21.8297 6.67222 21.9179C7.28388 22.0001 8.04769 22 8.93418 22H15.0658C15.9523 22 16.7161 22.0001 17.3278 21.9179C17.9833 21.8297 18.6117 21.631 19.1213 21.1213C19.631 20.6117 19.8297 19.9833 19.9179 19.3278C20.0001 18.7161 20.0001 17.9523 20 17.0659L20 11.4491L20.3356 11.7474C20.7484 12.1143 21.3805 12.0771 21.7474 11.6644C22.1143 11.2516 22.0772 10.6195 21.6644 10.2526L13.9931 3.43368ZM12 16C11.4477 16 11 16.4477 11 17V19C11 19.5523 10.5523 20 10 20C9.44772 20 9 19.5523 9 19V17C9 15.3431 10.3431 14 12 14C13.6569 14 15 15.3431 15 17V19C15 19.5523 14.5523 20 14 20C13.4477 20 13 19.5523 13 19V17C13 16.4477 12.5523 16 12 16Z"
              fill="#555555"
              p-id="4236"
            ></path>
          </svg>
        </a>
      </div>
    </div>
    <div class="login-container">
      <t-card class="login-card">
        <h2 class="login-title">
          <component :is="LogoOpenai" style="margin-bottom: 50px"></component>

          <div v-if="IsRegister">Buy an account</div>
          <div v-else>Hello!</div>
        </h2>
        <t-loading :loading="loading">
          <t-form :data="loginForm" :label-width="0" :rules="rules" ref="loginFormRef" @submit="onSubmit">
            <t-form-item name="username">
              <t-input v-model="loginForm.username" placeholder="Name"></t-input>
            </t-form-item>
            <t-form-item name="password">
              <t-input v-model="loginForm.password" type="password" autocomplete="on" placeholder="Password"></t-input>
            </t-form-item>

            <t-form-item v-if="loginType === 'register'" name="chatgpt_token">
              <div style="display: flex; flex-direction: column; width: 100%">
                <t-textarea
                  v-model="loginForm.chatgpt_token"
                  placeholder="ChatGPT Cookies Token"
                  size="large"
                ></t-textarea>
                <span style="font-size: 12px; color: #888">
                  Session Token Get Instructions：
                  <t-link target="_blank" theme="primary" size="small" :href="ChatgptTokenTutorialUrl">Manual access</t-link>
                  <!-- or
                  <t-link target="_blank" theme="primary" size="small" :href="ChatgptTokenAuthUrl">Auto-acquisition</t-link> -->
                </span>
              </div>
            </t-form-item>

            <t-form-item>
              <t-button theme="success" type="submit" size="large" class="login-button">
                <span v-if="IsRegister">Register</span>
                <span v-else> Login</span>
              </t-button>
            </t-form-item>
          </t-form>
        </t-loading>
        <div style="text-align: center; margin-top: 15px">
          <div v-if="IsRegister">
            Already have an account? <t-link :underline="false" href="/admin/#/login" style="color: #10a37f">Login</t-link> or
            <t-link :underline="false" style="color: red" @click="goFree">Free Trial</t-link>
          </div>
          <div v-else>
            No account yet?
            <t-link :underline="false" href="https://buy.nimble.uno" style="color: #10a37f">Buy here</t-link> or
            <t-link :underline="false" style="color: red" @click="goFree">Free Trial</t-link>
          </div>
        </div>
      </t-card>
    </div>
  </div>
</template>

<script setup lang="ts">
import { FormInstanceFunctions, FormProps, FormRule } from 'tdesign-vue-next';
import { computed, onMounted, reactive, ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';

import LogoOpenai from '@/assets/openai-logo.svg';
import { ChatgptTokenTutorialUrl } from '@/constants/index';
import { useUserStore } from '@/store';

const userStore = useUserStore();
const loading = ref(false);
const route = useRoute();
const router = useRouter();
const cfg = ref({ show_github: false, notice: '' });
const loginForm = reactive({
  username: '',
  password: '',
  chatgpt_token: undefined,
  invite_token: undefined,
  invite_id: undefined,
});

onMounted(async () => {
  await getVersionCfg();
});

const rules: Record<string, FormRule[]> = {
  username: [{ required: true, message: 'Please enter your username', trigger: 'blur' }],
  password: [{ required: true, message: 'Please enter your password', trigger: 'blur' }],
  chatgpt_token: [
    { required: true, message: 'Please enter Access Token or Session Token or Refresh Token', trigger: 'blur' },
  ],
};

const loginFormRef = ref<FormInstanceFunctions>(null);

const IsRegister = computed(() => {
  // console.log('route.path', route.path, route.path.endsWith('/register'));
  return !route.path.endsWith('/login');
});

const loginType = computed(() => {
  if (route.path.endsWith('/register')) {
    return 'register';
  }
  if (route.path.endsWith('/invite_register')) {
    return 'invite_register';
  }
  return 'login';
});

const onSubmit: FormProps['onSubmit'] = async ({ validateResult, firstError }) => {
  if (validateResult === true) {
    loading.value = true;
    let url;

    switch (loginType.value) {
      case 'register':
        url = '/0x/user/register';
        break;
      // case 'invite_register':
      //   url = '/api/invite-register';
      //   break;
      default:
        url = '/0x/user/login';
    }
    if (loginType.value === 'invite_register') {
      const { hash } = window.location;
      const paramsString = hash.split('?')[1];
      const params = new URLSearchParams(paramsString);
      loginForm.invite_token = params.get('invite_token');
      loginForm.invite_id = params.get('id');
    }

    // console.log(loginForm)
    const data = await userStore.login(url, loginForm);
    if (data.admin_token && data.is_admin) {
      router.push({ name: 'User' });
    } else if (data.admin_token) {
      return router.push({ name: 'LoginChatgpt' });
    }

    loading.value = false;
  } else {
    console.error('Form reference is not defined', firstError);
  }
};

const getVersionCfg = async () => {
  const response = await fetch('/0x/user/version-cfg');
  const data = await response.json();
  Object.assign(cfg.value, { ...data });
};

const goFree = async () => {
  loading.value = true;
  const data = await userStore.login('/0x/user/login-free', {});
  if (data.admin_token) {
    return router.push({ name: 'LoginChatgpt' });
  }

  loading.value = false;
};
</script>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 80vh;
}

.login-card {
  width: 400px;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}

.logo {
  width: 64px;
  margin-bottom: 20px;
}

.login-title {
  text-align: center;
  font-size: 36px;
  margin-bottom: 30px;
}

.login-button {
  width: 100%;
  height: 50px;
  background-color: #10a37f;
  border-color: #10a37f;
}

.login-button:hover {
  background-color: #0e8a6d;
  border-color: #0e8a6d;
}

:deep(.t-input) {
  height: 50px;
}
</style>
