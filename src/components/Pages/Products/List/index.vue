<template>
  <main role="main" class="col-md-9 ml-sm-auto col-lg-10 px-md-4 pt-5">
    <div class="mx-3">
      <div class="row">
        <div class="col-md-4 col-lg-4">
          <h4 class="menu-title">Manage Inventory</h4>
        </div>
      </div>
      <div class="row mt-5 mb-3">
        <!-- <div class="col-md-12 col-sm-12">
          <small>RESULT FROM {{ data.from }} - {{ data.to }} OF {{ data.total }}</small>
        </div> -->
        <div class="col-auto mr-auto">
          <small>RESULT FROM {{ data.from }} - {{ data.to }} OF {{ data.total }}</small>
        </div>
        <div class="col-auto">
          <button @click="filterOpen" class="btn btn-sm btn-primary"><i class="bi bi-filter-square"></i> Filter</button>
        </div>
      </div>
      <div class="row">
        <div class="col-md-12 col-lg-12">
          <table class="table table-bordered table-sm text-center">
            <thead>
              <tr>
                <th scope="col">Action</th>
                <th scope="col">PRODUCT NAME</th>
                <th scope="col">PRICE</th>
                <th scope="col">QUANTITY</th>
                <th scope="col">PRODUCT TYPE</th>
              </tr>
            </thead>
            <tbody>
              <template v-if="Object.keys(data).length">
                <template v-if="data.data.length">
                  <tr v-for="(item, i) in data.data" :key="i">
                    <td class="align-middle">
                      <i @click="doUpdate(item)" class="bi bi-pencil-square"></i>
                      <i @click="showImage(item.product_photo)" class="bi bi-card-image"></i>
                      <i @click="doDelete(item.id)" class="bi bi-trash"></i>
                    </td>
                    <td class="align-middle">{{ item.product_name }}</td>
                    <td class="align-middle">{{ item.product_price }}</td>
                    <td class="align-middle">{{ item.quantity }}</td>
                    <td class="align-middle">{{ item.product_type ? item.product_type.name : "No Type" }}</td>
                  </tr>
                </template>
                <template v-else>
                  <tr>
                    <td colspan="5">No data</td>
                  </tr>
                </template>
              </template>
            </tbody>
          </table>
        </div>
        <div class="col-md-12">
          <pagination :paginateData="data" @functionPage="getItems" />
        </div>
      </div>
    </div>
    <!-- delete start -->
    <div class="modal fade" id="deleteModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">Delete</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <small>Do you really want to delete this item?</small>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-sm btn-secondary" data-dismiss="modal">Close</button>
            <button type="button" class="btn btn-sm btn-primary">Yes</button>
          </div>
        </div>
      </div>
    </div>
    <!-- delete end -->

    <!-- filter start -->
    <div class="modal fade" id="filterModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">Advanced Filter</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <div class="form-group">
              <input type="text" v-model="name" placeholder="Search Name" class="form-control form-control-sm" />
            </div>
            <div class="form-row">
              <div class="col">
                <input type="number" class="form-control form-control-sm" v-model="min_price" placeholder="MIN PRICE" />
              </div>
              <div class="col">
                <input type="number" class="form-control form-control-sm" v-model="max_price" placeholder="MAX PRICE" />
              </div>
            </div>
            <div class="form-group mt-3">
              <select v-model="item_type" class="custom-select custom-select-sm" id="validationCustom04">
                <option selected disabled value="">Choose Type</option>
                <option v-for="(type, i) in product_types" :key="i" :value="type.id">{{ type.name }}</option>
              </select>
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" @click="reset" class="btn btn-sm btn-info">Reset</button>
            <button type="button" class="btn btn-sm btn-secondary" data-dismiss="modal">Close</button>
            <button type="button" @click="getItems(1)" class="btn btn-sm btn-primary">Submit</button>
          </div>
        </div>
      </div>
    </div>
    <!-- filter end -->

    <!-- edit start -->
    <div v-if="Object.keys(toUpdate).length" class="modal fade" id="editModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">Update this Item</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <div class="form-group">
              <input type="text" v-model="toUpdate.product_name" placeholder="Product Name" class="form-control form-control-sm" />
            </div>
            <div class="form-group">
              <input type="number" v-model="toUpdate.product_price" placeholder="Product Name" class="form-control form-control-sm" />
            </div>
            <div class="form-group">
              <input type="number" v-model="toUpdate.quantity" placeholder="Product Name" class="form-control form-control-sm" />
            </div>
            <div class="form-group mt-3">
              <select v-model="toUpdate.product_type.id" class="custom-select custom-select-sm" id="validationCustom04">
                <option selected disabled value="">Choose Type</option>
                <option v-for="(type, i) in product_types" :key="i" :value="type.id">{{ type.name }}</option>
              </select>
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-sm btn-secondary" data-dismiss="modal">Close</button>
            <button type="button" @click="saveItem" class="btn btn-sm btn-primary">Save</button>
          </div>
        </div>
      </div>
    </div>
    <!-- edit end -->
  </main>
</template>

<script>
export default {
  data() {
    return {
      data: {},
      page: 1,
      limit: 10,
      product_types: [],
      // filters
      item_type: "",
      name: "",
      min_price: "",
      max_price: "",
      toUpdate: {}
    };
  },
  created() {
    this.getItems();
    this.getProductTypes();
  },
  methods: {
    doDelete(id) {
      $("#deleteModal").modal("show");
    },
    filterOpen(id) {
      $("#filterModal").modal("show");
    },
    reset() {
      this.name = "";
      this.min_price = "";
      this.max_price = "";
      this.item_type = "";
    },
    showImage(image) {
      this.$viewerApi({
        images: [image]
      });
    },
    async getProductTypes() {
      await axios.get("/admin/product/api/get-product-types/").then(res => {
        this.product_types = res.data.result;
      });
    },
    doUpdate(item) {
      this.toUpdate = item;
      this.$nextTick(() => {
        $("#editModal").modal("show");
      });
    },
    async saveItem() {
      await axios.post("/admin/product/api/update-product/", this.toUpdate).then(res => {});
    },
    getItems(p) {
      let page;
      let urlParams = new URLSearchParams(window.location.search);
      page = urlParams.has("page") ? urlParams.get("page") : p ? p : this.page;

      if (p) {
        history.pushState(
          {
            id: "Product list"
          },
          "Product list",
          `${location.origin}${location.pathname}?page=${p}`
        );
        page = p;
      }

      axios
        .post(`/admin/product/api/get-items-paginate`, {
          page,
          limit: this.limit,
          filters: {
            name: this.name,
            min_price: this.min_price,
            max_price: this.max_price,
            item_type: this.item_type
          }
        })
        .then(res => {
          this.data = res.data.data;
        });
    }
  }
};
</script>

<style>
.bi {
  font-size: 17px;
  transition: 0.2s;
  cursor: pointer;
}

.bi-card-image:hover {
  color: #4287f5;
}

.bi-trash:hover {
  color: #f55742;
}

.bi-pencil-square:hover {
  color: #42f5a7;
}
</style>
