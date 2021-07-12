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
              <div class="form-group">
                <label for="exampleInputEmail1">Email address</label>
                <input
                  type="email"
                  class="form-control form-control-sm"
                  id="exampleInputEmail1"
                  aria-describedby="emailHelp"
                  v-model="email"
                />
                <small id="emailHelp" class="form-text text-muted"
                  >We'll never share your email with anyone else.</small
                >
              </div>
              <div class="form-group">
                <label for="exampleInputPassword1">Password</label>
                <input
                  type="password"
                  class="form-control form-control-sm"
                  id="exampleInputPassword1"
                  v-model="password"
                />
              </div>
              <button @click="submitData" class="btn btn-primary btn-sm">
                Submit
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
    };
  },
  methods: {
    async submitData() {
      const result = await axios.post(`/admin/login/`, {
        email: this.email,
        password: this.password,
      });

      console.log(result);
    },
  },
};
</script>

<style>
.main-container {
  height: 100vh;
}
</style>
