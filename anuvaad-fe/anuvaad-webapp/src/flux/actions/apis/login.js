/**
 * Login API
 */
import API from "./api";
import C from "../constants";
import CONFIGS from "../../../configs/configs";
import ENDPOINTS from "../../../configs/apiendpoints";

export default class LoginAPI extends API {
  constructor(email, password, timeout = 2000) {
    super("POST", timeout, false);
    this.email = email;
    this.password = password;
    this.token = null;
    this.expires = null;
    this.userid = null;
    this.name = null;
    this.type = C.LOGIN;
    // this.endpoint = `${super.apiEndPointAuto()}${ENDPOINTS.login}`;
    this.endpoint = 'https://poczuul.anuvaad.org/anuvaad/user-mgmt/v1/users/login'
  }

  toString() {
    return `${super.toString()} email: ${this.email} token: ${this.token} expires: ${this.expires} userid: ${this.userid}, type: ${this.type}`;
  }

  processResponse(res) {
    super.processResponse(res);
    if (res.token) {
    debugger

      this.token = res.token;
      this.expires = res.expires;
      this.role = res.role;
      this.userid = res.userid;
      this.name = res.name;
      // sessionStorage.setItem('user', JSON.stringify(res.user))
    }
  }

  apiEndPoint() {
    return this.endpoint;
  }

  getBody() {
    return {
      userName: this.email,
      password: this.password,
      // role: this.role,
      // userid: this.userid,
      // name: this.name
    };
  }

  getHeaders() {
    this.headers = {
      headers: {
        "Content-Type": "application/json"
      }
    };
    return this.headers;
  }

  getPayload() {
    return {
      userName: this.email,
      password: this.password,
      // email: this.email,
      // token: this.token,
      // role: this.role,
      // name: this.name,
      // userid: this.userid
    };
  }

  // getCustomConfigs() {
  //   return {
  //     auth: {
  //       username: CONFIGS.DEV_SALT,
  //       password: CONFIGS.DEV_PEPPER
  //     },
  //     timeout: this.timeout
  //   };
  // }
}
