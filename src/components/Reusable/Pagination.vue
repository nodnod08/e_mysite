<template>
  <div>
    <nav v-if="Number(paginateData.pages) > 1" aria-label="Page navigation example">
      <ul class="pagination pagination-sm">
        <li v-if="Number(paginateData.current) == 1" class="page-item disabled">
          <a class="page-link" href="#">&laquo;</a>
        </li>
        <li v-else class="page-item">
          <a class="page-link" v-on:click="changePage(Number(paginateData.current) - 1)" tabindex="-1">&laquo;</a>
        </li>
        <span v-if="Number(paginateData.pages) < 7 + adjacent * 2" class="pagination">
          <span v-for="(n, a) in Number(paginateData.pages)" :key="a" class="pagination">
            <li v-if="n == Number(paginateData.current)" class="page-item active">
              <a class="page-link" tabindex="-1">{{ n }}</a>
            </li>
            <li v-else class="page-item">
              <a class="page-link" v-on:click="changePage(n)" tabindex="-1">{{ n }}</a>
            </li>
          </span>
        </span>
        <span v-else-if="paginateData.pages > 5 + adjacent * 2" class="pagination">
          <span v-if="Number(paginateData.current) < 1 + adjacent * 2" class="pagination">
            <span v-for="(n, b) in 4 + adjacent * 2" :key="b" class="pagination">
              <li v-if="n == Number(paginateData.current)" class="page-item active">
                <a class="page-link" tabindex="-1">{{ n }}</a>
              </li>
              <li v-else class="page-item">
                <a class="page-link" v-on:click="changePage(n)" tabindex="-1">{{ n }}</a>
              </li>
            </span>
            <li class="page-item disabled">
              <a class="page-link" tabindex="-1">...</a>
            </li>
            <li class="page-item">
              <a class="page-link" v-on:click="changePage(Number(paginateData.pages) - 1)" tabindex="-1">{{ Number(paginateData.pages) - 1 }}</a>
            </li>
            <li class="page-item">
              <a class="page-link" v-on:click="changePage(Number(paginateData.pages))" tabindex="-1">{{ Number(paginateData.pages) }}</a>
            </li>
          </span>
          <span v-else-if="Number(paginateData.pages) - adjacent * 2 > Number(paginateData.current) && Number(paginateData.current) > adjacent * 2" class="pagination">
            <li class="page-item">
              <a class="page-link" v-on:click="changePage(1)" tabindex="-1">1</a>
            </li>
            <li class="page-item">
              <a class="page-link" v-on:click="changePage(2)" tabindex="-1">2</a>
            </li>
            <li class="page-item disabled">
              <a class="page-link" tabindex="-1">...</a>
            </li>
            <span v-for="(n, c) in pagePlusAdjacent" :key="c" class="pagination">
              <template v-if="n >= pageMinusAdjacent && n <= pagePlusAdjacent">
                <li v-if="n == Number(paginateData.current)" class="page-item active">
                  <a class="page-link" tabindex="-1">{{ n }}</a>
                </li>
                <li v-else class="page-item">
                  <a class="page-link" v-on:click="changePage(n)" tabindex="-1">{{ n }}</a>
                </li>
              </template>
            </span>
            <li class="page-item disabled">
              <a class="page-link" tabindex="-1">...</a>
            </li>
            <li class="page-item">
              <a class="page-link" v-on:click="changePage(Number(paginateData.pages) - 1)" tabindex="-1">{{ Number(paginateData.pages) - 1 }}</a>
            </li>
            <li class="page-item">
              <a class="page-link" v-on:click="changePage(Number(paginateData.pages))" tabindex="-1">{{ Number(paginateData.pages) }}</a>
            </li>
          </span>
          <span v-else class="pagination">
            <li class="page-item">
              <a class="page-link" v-on:click="changePage(1)" tabindex="-1">1</a>
            </li>
            <li class="page-item">
              <a class="page-link" v-on:click="changePage(2)" tabindex="-1">2</a>
            </li>
            <li class="page-item disabled">
              <a class="page-link" tabindex="-1">...</a>
            </li>
            <span v-for="(n, d) in Number(paginateData.pages)" :key="d" class="pagination">
              <template v-if="n >= AdjacentXTwoPlusTwoMinusLastPage">
                <li v-if="n == Number(paginateData.current)" class="page-item active">
                  <a class="page-link" tabindex="-1">{{ n }}</a>
                </li>
                <li v-else class="page-item">
                  <a class="page-link" v-on:click="changePage(n)" tabindex="-1">{{ n }}</a>
                </li>
              </template>
            </span>
          </span>
        </span>
        <li v-if="Number(paginateData.current) == Number(paginateData.pages)" class="page-item disabled">
          <a class="page-link" tabindex="-1">&raquo;</a>
        </li>
        <li v-else class="page-item">
          <a class="page-link" v-on:click="changePage(Number(paginateData.current) + 1)">&raquo;</a>
        </li>
      </ul>
    </nav>
  </div>
</template>

<script>
export default {
  props: ["paginateData"],
  data() {
    return {
      i: "",
      adjacent: 2,
      record_per_page: 10,
      page: "",
      pagePlusAdjacent: "",
      pageMinusAdjacent: "",
      AdjacentXTwoPlusTwoMinusLastPage: ""
    };
  },
  watch: {
    paginateData(newVal, oldVal) {
      this.paginateData = newVal;
      this.i = newVal.current > 5 ? newVal.current - 4 : 1;
      this.page = newVal.current - this.adjacent;
      this.pagePlusAdjacent = Number(newVal.current) + this.adjacent;
      this.pageMinusAdjacent = Number(newVal.current) - this.adjacent;
      this.AdjacentXTwoPlusTwoMinusLastPage = newVal.pages - (this.adjacent * 2 + 2);
    }
  },
  methods: {
    changePage(page) {
      this.$emit("functionPage", page);
    }
  },
  created() {
    this.i = this.paginateData.current > 5 ? this.paginateData.current - 4 : 1;
  }
};
</script>

<style>
.page-item {
  display: inline;
}
.page-item {
  cursor: pointer;
}

.disabled {
  cursor: default;
}
</style>
