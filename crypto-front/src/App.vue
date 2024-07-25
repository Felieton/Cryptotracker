<template>
  <div id="app">
    <div style=margin-left:77%;margin-right:12%;margin-top:1%>
      <div v-if="!$auth.loading">
        <!-- show login when not authenticated -->
        <b-button variant="success" v-if="!$auth.isAuthenticated" @click="login" class="button is-dark"><strong>Sign in</strong></b-button>
        <!-- show logout when authenticated -->
        <b-button variant="success" v-if="$auth.isAuthenticated" @click="logout" class="button is-dark"><strong>Log out</strong></b-button>
        <div class="welcome-text" style=margin-right:80%;margin-top:3%> 
          <p v-if="$auth.isAuthenticated">Welcome, {{ $auth.user.nickname }}!</p>
        </div>
      </div>
    </div>
    <div style="display:inline-block;vertical-align:top;margin-left:20%;margin-top:-2%">
      <img src="crypto_icon.png">
    </div>
    <div style="display:inline-block;margin-top:-1%">
      <div class="name">ryptotracker</div>
    </div>
    <div id="nav">
      <router-link to="/">Home</router-link> | 
      <router-link to="/hot">Hot</router-link> | 
      <router-link to="/dashboard">Dashboard</router-link>
      <hr style="width:65%;text-align:left;margin-left:19%;margin-right:19%;margin-top:2%">
    </div>
    <router-view />
    
    <div>
    </div>
  </div>
</template>

<script>

export default {
    methods: {
      login() {
      this.$auth.loginWithRedirect();
    },
      logout() {
      this.$auth.logout({
        returnTo: window.location.origin
      });
    }
  },
  components: {
  },
}
</script>


<style>
  .name {
    margin-left: 8%;
    padding-top: 2%;
    font-size: 300%;
  }

  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;
  }
  #nav {
    padding: 30px;
    text-align: center;
    font-size: 150%;
  }
  #nav a {
    font-weight: bold;
    color: #2c3e50;
  }
  #nav a.router-link-exact-active {
    color: #42b983;
  }

</style>
