<template>
  <main role="main" class="col-md-9 ml-sm-auto col-lg-10 px-md-4 pt-5">
    <div class="mx-3">
      <div class="row">
        <div class="col-md-4 col-lg-4">
          <h4 class="menu-title">Product Selection Interface</h4>
        </div>
      </div>
      <div class="row mt-5">
        <div v-for="(item, i) in items" :key="i" class="url col-md-4 col-sm-6 col-xs-12 col-lg-3" @click="goTo(item.url)">
          <div class="card mb-4">
            <div class="card-body">
              <h6 class="card-title"><i :class="item.icon"></i> {{ item.title }}</h6>
              <small>
                {{ item.subTitle }}
              </small>
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>

<script>
export default {
  data() {
    return {
      items: [
        {
          icon: "intro-icon bi bi-collection",
          title: "Product Types",
          url: "",
          subTitle: "Card titles are used by adding .card-title to a <h*> tag. In the same way, links are added and placed next to each other by adding"
        },
        {
          icon: "intro-icon bi bi-list-stars",
          title: "Inventory",
          url: "/admin/product/list",
          subTitle: "Card titles are used by adding .card-title to a <h*> tag. In the same way, links are added and placed next to each other by adding"
        },
        {
          icon: "intro-icon bi bi-file-earmark-arrow-up",
          title: "Product Imports",
          url: "/admin/product/import",
          subTitle: "Card titles are used by adding .card-title to a <h*> tag. In the same way, links are added and placed next to each other by adding"
        },
        {
          icon: "intro-icon bi bi-file-earmark-font",
          title: "Product Files",
          url: "",
          subTitle: "Card titles are used by adding .card-title to a <h*> tag. In the same way, links are added and placed next to each other by adding"
        },
        {
          icon: "intro-icon bi bi-trash",
          title: "Trash",
          url: "",
          subTitle: "Card titles are used by adding .card-title to a <h*> tag. In the same way, links are added and placed next to each other by adding"
        }
      ]
    };
  },
  methods: {
    goTo(url) {
      window.location.href = url;
    }
  }
};
</script>

<style>
.intro-icon {
  color: #404040;
}
.url {
  cursor: pointer;
}
</style>
