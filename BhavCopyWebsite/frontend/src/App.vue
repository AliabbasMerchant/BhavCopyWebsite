<template>
  <div id="home">
    <Search class="mb-3" @search="onSearchResult" />
    <template v-if="searchResults != undefined">
      <ResultsView :scrips="searchResults" />
      <div v-if="searchResults.length === 0">No Data</div>
    </template>
  </div>
</template>

<script>
import Search from "@/components/Search.vue";
import ResultsView from "@/components/ResultsView.vue";

export default {
  name: "App",
  data() {
    return {
      searchResults: undefined, // to indicate that no search has been performed as yet
    };
  },
  components: {
    Search,
    ResultsView,
  },
  methods: {
    onSearchResult(data) {
      this.searchResults = data;
    },
  },
};
</script>

<style>
#home {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  padding: 20px;
}
</style>
