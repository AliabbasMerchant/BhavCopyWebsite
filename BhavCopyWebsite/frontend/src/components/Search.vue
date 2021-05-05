<template>
  <div class="row-container">
    <input
      v-model="searchText"
      @keyup="searchHandler"
      class="form-control form-control-lg mx-2"
      type="search"
      placeholder="Search Stocks By Name..."
      pattern=".{3,}"
      title="Please enter at least 3 characters"
    />
    <button class="btn btn-lg btn-success row-container" @click="onClick()">
      <span class="mr-1">
        <i class="fa fa-search h1"></i>
      </span>
      Search
    </button>

    <div
      class="modal fade bd-example-modal-sm"
      tabindex="-1"
      id="alertModal"
      role="dialog"
      aria-hidden="true"
    >
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header align-items-center">
            <h5 class="modal-title">Please enter at least 3 characters</h5>
            <button
              type="button"
              class="close"
              data-dismiss="modal"
              aria-label="Close"
            >
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Search",
  data() {
    return {
      searchText: "",
    };
  },
  methods: {
    onClick() {
      if (this.searchText.length < 3) {
        window.$("#alertModal").modal();
        return;
      }
      axios.get(`/api/search?q=${this.searchText}`).then((response) => {
        this.$emit("search", response.data);
      });
    },
    searchHandler(e) {
      if (e.keyCode === 13) {
        // Enter key
        this.onClick();
      }
    },
  },
};
</script>

<style scoped>
.h1 {
  font-size: x-large;
}
.row-container {
  display: flex;
  flex-direction: row;
  align-items: center;
}
</style>
