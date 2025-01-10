<template>
  <div style="display: flex; flex-direction: column">
    <div style="display: flex; justify-content: space-between">
      <div style="width: 400px; float: left">
        <div v-if="cfg.notice" v-html="cfg.notice"></div>
      </div>
      <div v-if="cfg.show_github" style="margin: 12px 20px">
        <a href="https://nimble.uno" target="_blank" style="float: right">
          <svg 
            xmlns="http://www.w3.org/2000/svg" 
            xmlns:xlink="http://www.w3.org/1999/xlink" 
            version="1.1" 
            x="0px" 
            y="0px" 
            width="32" 
            height="32" 
            viewBox="0 0 32 40" 
            enable-background="new 0 0 32 32" 
            xml:space="preserve"
          >
            <g>
              <g>
                <path d="M27.000061,18.5c0.152832,0,0.3060303-0.0350342,0.4471436-0.1055908C27.8114624,18.2122803,29,17.3571167,29,14    c0-6.7290039-5.7102661-12-13-12S3,7.2709961,3,14c0,2.8883667,1.0726929,4.4273071,1.1950073,4.5932617    c0.1728516,0.2345581,0.4393921,0.382019,0.7299194,0.4039307C4.9500122,18.9990845,4.9750977,19,5.000061,19H5v4    c0,2.7614136,2.2385864,5,5,5v2h12v-2c2.7614136,0,5-2.2385864,5-5C27,23,27,18.5,27.000061,18.5z M21,29H11v-1h10V29z M26,23    c0,2.2056274-1.7943726,4-4,4H10c-2.2056274,0-4-1.7943726-4-4v-4.6325073    c0.5228882-0.657959,1.5919189-2.2778931,1.9096069-4.864563C8.6886597,13.7863159,9.6511841,14,11,14    c2.1572876,0,4.3415527-0.5368652,6.4538574-1.0560303C19.428894,12.4584961,21.2944336,12,23,12c2.5219116,0,3,1.9329834,3,5.5    V23z M27,17.5c0-2.4702148,0-6.5-4-6.5c-3.7207031,0-8,2-12,2c-2,0-3-0.5-4-1c0,4-2,6-2,6s-1-1.3569336-1-4    C4,7.831543,9.2714844,3,16,3s12,4.831543,12,11C28,17,27,17.5,27,17.5z"/>
                <circle cx="13" cy="17" r="1"/>
                <circle cx="19" cy="17" r="1"/>
                <path d="M19.6464844,20.6464844C18.7861328,21.5068359,17.4570312,22,16,22s-2.7861328-0.4931641-3.6464844-1.3535156    c-0.1953125-0.1953125-0.5117188-0.1953125-0.7070312,0s-0.1953125,0.5117188,0,0.7070312    C12.6923828,22.3999023,14.2792969,23,16,23s3.3076172-0.6000977,4.3535156-1.6464844    c0.1953125-0.1953125,0.1953125-0.5117188,0-0.7070312S19.8417969,20.4511719,19.6464844,20.6464844z"/>
              </g>
            </g>
            <g display="none">
              <g display="inline">
                <path fill="#000000" d="M4.9624023,18.4990234c-0.1450195-0.0117188-0.2783203-0.0849609-0.3647461-0.2021484    C4.5527344,18.2353516,3.5,16.7753906,3.5,14C3.5,7.5512695,8.9907227,2.5,16,2.5c7.0097656,0,12.5,5.0512695,12.5,11.5    c0,3.1494141-1.0634766,3.8408203-1.2763672,3.9472656C27.1533203,17.9824219,27.0761719,18,27,18    c-0.0917969,0-0.1826172-0.0253906-0.2626953-0.0742188C26.5898438,17.8339844,26.5,17.6728516,26.5,17.5    c0-3.1621094-0.2675781-6-3.5-6c-1.7666016,0-3.6601562,0.465332-5.6650391,0.9584961    C15.2509766,12.9707031,13.0966797,13.5,11,13.5c-1.6523438,0-2.6669922-0.3256836-3.5249023-0.7148438    c-0.234375,3.6396484-2.0395508,5.4863281-2.121582,5.5683594C5.2592773,18.4472656,5.1323242,18.5,5,18.5    C4.9873047,18.5,4.9750977,18.5,4.9624023,18.4990234z"/>
                <path fill="#000000" d="M16,3c6.7285233,0,12,4.8315401,12,11c0,3-1,3.5-1,3.5c0-2.4702101,0-6.5-4-6.5c-3.7207031,0-8,2-12,2    c-2,0-3-0.5-4-1c0,4-2,6-2,6s-1-1.3569298-1-4C4,7.8315401,9.2714806,3,16,3 M16,2C8.7102814,2,3,7.2710299,3,14    c0,2.8883495,1.0726814,4.42729,1.1949883,4.5932598c0.1728516,0.2345505,0.4394035,0.38204,0.7299309,0.4039211    c0.0250931,0.0018883,0.0501595,0.0028229,0.0751305,0.0028229c0.264164,0,0.5188332-0.1046658,0.7070618-0.2928944    c0.0821953-0.0822048,1.7875557-1.8261375,2.2024765-5.2041397C8.688633,13.7863121,9.6511803,14,11,14    c2.15728,0,4.3415184-0.5368605,6.4538422-1.0560398C19.4288864,12.4585199,21.2944031,12,23,12c2.5219193,0,3,1.9329901,3,5.5    c0,0.3465805,0.179451,0.6684399,0.4742737,0.8506508c0.1605759,0.0992451,0.3429337,0.1493511,0.5257721,0.1493511    c0.1528473,0,0.3060226-0.0350018,0.4471664-0.1055717C27.8114777,18.2122898,29,17.3571301,29,14C29,7.2710299,23.2897186,2,16,2    L16,2z"/>
              </g>
            </g>
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
              <t-input v-model="loginForm.username" placeholder="Username"></t-input>
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
