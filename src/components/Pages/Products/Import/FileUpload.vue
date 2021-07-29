<template>
  <div>
    <div class="row">
      <div class="col-md-6 col-lg-6">
        <div class="card mt-5">
          <div class="card-body">
            <h4 class="card-title">Import File</h4>
            <form @submit.prevent="saveItem">
              <div class="custom-file mb-3">
                <label class="custom-file-label file" for="file">Choose file</label>
                <input type="file" @change="handleFileUpload" class="custom-file-input" id="file" ref="file" />
              </div>
              <div v-if="loading" class="progress mb-4">
                <div class="progress-bar bg-success" role="progressbar" :style="{ width: loaded + '%' }" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">{{ loaded }}%</div>
              </div>
              <button type="submit" :disabled="loading" class="btn btn-sm btn-primary">
                <i v-if="!loading" class="bi bi-save"></i>
                <span v-if="loading" class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
                {{ loading ? "Saving" : "Save Item" }}
              </button>
            </form>
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
      file: "",
      loading: false,
      loaded: 0
    };
  },
  methods: {
    handleFileUpload() {
      this.file = this.$refs.file.files[0];
    },
    async saveItem() {
      let formData = new FormData();
      formData.append("file", this.file);
      var vm = this;
      this.loading = true;
      await axios
        .post("/admin/product/api/upload-file-product/", formData, {
          headers: {
            "Content-Type": "multipart/form-data"
          },
          onUploadProgress: progressEvent => {
            let newLoad = parseInt(Math.round((progressEvent.loaded * 100) / progressEvent.total)) - (Math.floor(Math.random() * 50) + 1);
            if (newLoad > vm.loaded) {
              vm.loaded = newLoad;
            }
          }
        })
        .then(response => {
          if (response.data.success) {
            vm.loaded = 100;
          }
          setTimeout(() => {
            this.loading = false;
            vm.loaded = 0;
          }, 1000);
        });
    }
  },
  mounted() {
    $(document).ready(function() {
      $('input[id="file"]').change(function(e) {
        var fileName = e.target.files[0].name;
        $(".file").html(fileName);
      });
    });
  }
};
</script>

<style></style>
