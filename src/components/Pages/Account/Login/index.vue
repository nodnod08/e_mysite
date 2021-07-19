<template>
  <div class="login-body">
    <div class="container">
      <div class="row main-container d-flex justify-content-md-center ">
        <div class="box align-self-center col-md-6 col-lg-4">
          <div class="card">
            <div class="card-header">
              LOGIN
            </div>
            <div class="card-body">
              <div v-if="showError" class="alert alert-danger" role="alert">
                <h6 class="alert-heading"><i class="fa fa-exclamation-triangle"></i> Incorrect Credentials</h6>
                <p class="mb-0">
                  Email or Password is incorrect, unable to login
                </p>
              </div>
              <div class="form-group">
                <label for="exampleInputEmail1">Email address</label>
                <input type="email" class="form-control form-control-sm" id="exampleInputEmail1" aria-describedby="emailHelp" v-model="email" />
                <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
              </div>
              <div class="form-group">
                <label for="exampleInputPassword1">Password</label>
                <input type="password" class="form-control form-control-sm" id="exampleInputPassword1" v-model="password" />
              </div>
              <button @click="submitData" class="btn btn-primary" type="button" :disabled="loading">
                <span v-if="loading" class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
                {{ loading ? "Loading" : "Login" }}
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      email: "",
      password: "",
      loading: false,
      showError: false
    };
  },
  methods: {
    async submitData() {
      this.loading = true;
      await axios
        .post(`/admin/login/`, {
          email: this.email,
          password: this.password
        })
        .then(res => {
          if (res.data.success) {
            window.location.replace("/admin/dashboard/");
          } else {
            this.showError = true;
          }
          this.loading = false;
        });
    }
  }
};
</script>

<style>
.main-container {
  height: 100vh;
}
</style>
