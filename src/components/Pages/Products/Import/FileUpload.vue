<template>
  <div>
    <div class="row">
      <div class="col-md-6 col-lg-6">
        <div class="card mt-5">
          <div class="card-body">
            <h4 class="card-title">Import File</h4>
            <form @submit.prevent="saveItem">
              <div class="custom-file mb-5">
                <label class="custom-file-label" for="file">Choose file</label>
                <input type="file" @change="handleFileUpload" class="custom-file-input" id="file" ref="file" />
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
      loading: false
    };
  },
  methods: {
    handleFileUpload() {
      this.file = this.$refs.file.files[0];
    },
    async saveItem() {
      let formData = new FormData();
      formData.append("file", this.file);

      await axios
        .post("/admin/product/api/upload-file-product/", formData, {
          headers: {
            "Content-Type": "multipart/form-data"
          }
        })
        .then(function() {
          console.log("SUCCESS!!");
        });
    }
  },
  mounted() {
    $(document).ready(function() {
      $('input[type="file"]').change(function(e) {
        var fileName = e.target.files[0].name;
        $(".custom-file-label").html(fileName);
      });
    });
  }
};
</script>

<style></style>
