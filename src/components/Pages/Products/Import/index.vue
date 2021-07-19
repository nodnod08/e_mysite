<template>
  <main role="main" class="col-md-9 ml-sm-auto col-lg-10 px-md-4 pt-5">
    <div class="mx-3">
      <div class="row">
        <div class="col-md-4 col-lg-4">
          <h4 class="menu-title">Import Product / Item</h4>
        </div>
      </div>
      <div class="row mt-5">
        <div class="col-md-12 col-lg-12">
          <ul class="nav nav-tabs" id="myTab" role="tablist">
            <li class="nav-item" role="presentation">
              <a class="nav-link active" id="home-tab" data-toggle="tab" href="#manual" role="tab" aria-controls="home" aria-selected="true">Manually Import</a>
            </li>
            <li class="nav-item" role="presentation">
              <a class="nav-link" id="profile-tab" data-toggle="tab" href="#file" role="tab" aria-controls="profile" aria-selected="false">Import Via CSV / XLSX</a>
            </li>
          </ul>
          <div class="tab-content" id="myTabContent">
            <div class="tab-pane fade show active" id="manual" role="tabpanel" aria-labelledby="home-tab">
              <ManualImport />
            </div>
            <div class="tab-pane fade" id="file" role="tabpanel" aria-labelledby="profile-tab">
              ...
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>

<script>
import ManualImport from "./ManualImport.vue";

export default {
  components: {
    ManualImport
  },
  data() {
    return {};
  },
  methods: {
    goTo(url) {
      window.location.href = url;
    }
  }
};
</script>

<style></style>
