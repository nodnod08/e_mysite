<template>
  <div class="mt-5">
    <div class="card">
      <div class="card-body">
        <div class="row">
          <div class="col-md-12 col-lg-6">
            <div v-if="result.show" class="alert" :class="{ 'alert-danger': !result.success, 'alert-success': result.success }" role="alert">
              <h6 class="alert-heading">
                <i v-if="result.success" class="bi bi-check-circle"></i>
                <i v-if="!result.success" class="bi bi-exclamation-diamond"></i>
                {{ result.success ? "Item Saved!" : "Failed!" }}
              </h6>
              <p class="mb-0">
                {{ result.message }}
              </p>
            </div>
            <form @submit.prevent="saveItem">
              <div class="form-group">
                <label for="exampleInputEmail1">Item Name</label>
                <input type="text" v-model="item_name" class="form-control form-control-sm" id="exampleInputEmail1" aria-describedby="emailHelp" />
              </div>
              <div class="form-group">
                <label for="exampleInputEmail1">Item Price</label>
                <input type="text" v-model="item_price" class="form-control form-control-sm" id="exampleInputEmail1" aria-describedby="emailHelp" />
              </div>
              <div class="form-group">
                <label for="exampleInputPassword1">Item Type</label>
                <select v-model="item_type" class="custom-select custom-select-sm" id="validationCustom04">
                  <option selected disabled value="">Choose Type</option>
                  <option v-for="(type, i) in product_types" :key="i" :value="type.id">{{ type.name }}</option>
                </select>
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
      product_types: [],
      item_name: "",
      item_price: "",
      item_type: 1,
      loading: false,
      result: {
        message: "",
        show: false
      }
    };
  },
  methods: {
    async getProductTypes() {
      await axios.get("/admin/product/api/get-product-types/").then(res => {
        this.product_types = res.data.result;
      });
    },
    async saveItem() {
      this.loading = true;
      await axios
        .post("/admin/product/api/save-product-manually/", {
          item_name: this.item_name,
          item_price: this.item_price,
          item_type: this.item_type
        })
        .then(res => {
          this.result.message = res.data.message;
          this.result.show = true;
          this.result.success = res.data.success;
          this.loading = false;
        });
    }
  },
  created() {
    this.getProductTypes();
  }
};
</script>

<style></style>
