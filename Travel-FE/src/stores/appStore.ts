import { defineStore } from 'pinia';

export const useAppStore = defineStore({
  id: 'app',
  state: () => ({
    rootUrl: 'http://localhost:5000',
    guid: localStorage.getItem('guid') ?localStorage.getItem('guid') : '',
    role: localStorage.getItem('role') ?localStorage.getItem('role') :  '',
    token:localStorage.getItem('token') ?localStorage.getItem('token') : '',
    email:localStorage.getItem('email') ?localStorage.getItem('email') : '',
    userIsLoggedIn: localStorage.getItem('token') ? true : false,
  }),
  actions: {
    initAppStore() {
      const token = localStorage.getItem('token')
      const userIsLoggedIn = localStorage.getItem('userIsLoggedIn')
      const guid = localStorage.getItem('guid')
      const role = localStorage.getItem('role')
      const email = localStorage.getItem('email')
      if (token) {
        this.setToken(token)
        this.setUserIsLoggedIn(true)
      }
      if (userIsLoggedIn) {
        this.setUserIsLoggedIn(userIsLoggedIn === 'true')
      }
      if (guid) {
        this.setGuid(guid)
      }
      if (role) {
        this.setRole(role)
      }
      if (email) {
        this.setEmail(email)
      }
    },
    setToken(token: string) {
      this.token = token
    },
    setUserIsLoggedIn(userIsLoggedIn: boolean) {
      this.userIsLoggedIn = userIsLoggedIn
    },
    setRootUrl(rootUrl: string) {
      this.rootUrl = rootUrl
    },
    setGuid(guid: string) {
      this.guid = guid
    },
    setRole(role: string) {
      this.role = role
    },
    setEmail(email: string) { 
      this.email = email
    },
    getToken() { 
      return this.token
    },
    getRootUrl() {
      return this.rootUrl
    },
    getGuid() {
      return this.guid
    },
    getRole() {
      return this.role
    },
    getUserIsLoggedIn() { 
      return this.userIsLoggedIn
    },
    logOutUser() {
      this.token = ''
      this.userIsLoggedIn = false
      this.guid = ''
      this.role = ''
    },
  },
});
